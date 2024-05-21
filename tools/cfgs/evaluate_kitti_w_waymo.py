import numpy as np
import copy
import sys
sys.path.append('../')
# sys.path.append('/MS3D/pcdet')
import argparse
from tqdm import tqdm
import pickle
from pcdet.config import cfg, cfg_from_yaml_file
from pcdet.utils import common_utils
from pcdet.datasets import build_dataloader


SUPERCATEGORIES = ['Car','Pedestrian','Cyclist']
SUPER_MAPPING = {'car': 'Car',
                'Car': 'Car',
                'Veh': 'Car',
                'Regular_vehicle': 'Car',
                'truck': 'Car',
                'Truck': 'Car',
                'bus': 'Car',
                'Vehicle': 'Car',
                'pedestrian': 'Pedestrian',
                'Pedestrian': 'Pedestrian',
                'Wheelchair': 'Cyclist',
                'motorcycle': 'Cyclist',
                'Bicyclist': 'Cyclist',
                'Bicycle': 'Cyclist',
                'bicyclist': 'Cyclist',
                'bicycle': 'Cyclist',
                'Cyclist': 'Cyclist'}


def load_dataset(split):
    # Get target dataset    
    cfg.DATA_SPLIT.test = split
    cfg.SAMPLED_INTERVAL.test = 1
    logger = common_utils.create_logger('temp.txt', rank=cfg.LOCAL_RANK)
    target_set, _, _ = build_dataloader(
                dataset_cfg=cfg,
                class_names=cfg.CLASS_NAMES,
                batch_size=1, logger=logger, training=False, dist=False, workers=1
            )      
    return target_set

def pretty_print(ap_dict):
    item_key = 'SOURCE\tTARGET\t'
    item_res = f'{cfg.DATASET.replace("Dataset","")}\t{cfg.DATASET.replace("Dataset","")}\t'
    for k,v in ap_dict.items():
        if ('VEHICLE' in k) or ('PEDESTRIAN' in k) or ('CYCLIST' in k):
            key = k[11:].replace('LEVEL_','L').replace('PEDESTRIAN','PED').replace('VEHICLE','VEH').replace('CYCLIST','CYC').replace(' ','')
            item_key += f'{key}\t'
            item_res += f'{ap_dict[k][0]*100:0.2f}\t'
    item_key += '\n'
    item_res += '\n'
    print(item_key)
    print(item_res)
    return item_res

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='arg parser')
    parser.add_argument('--cfg_file', type=str, default='/MS3D/tools/cfgs/dataset_configs/kitti_raw_dataset_da.yaml',
                        help='just use the target dataset cfg file')
    parser.add_argument('--ps_dict', type=str, help='Use kbf ps_dict')
    parser.add_argument('--det_pkl', type=str, help='result.pkl from test.py')
    parser.add_argument('--interval', type=int, default=1, help='set interval')
    args = parser.parse_args()
    
    cfg_from_yaml_file(args.cfg_file, cfg)
    dataset = load_dataset(split='train')
    print('Evaluating for the classes: ', cfg.CLASS_NAMES)

    ps_dict = None
    if args.ps_dict:
        with open(args.ps_dict, 'rb') as f:
            ps_dict = pickle.load(f)

        # Evaluate
        pred_annos, gt_annos = [], []
        eval_gt_annos = copy.deepcopy(dataset.infos)
       
        for frame_id in tqdm(ps_dict.keys(), total=len(ps_dict.keys())):  
       # for frame_id in tqdm(ps_dict.keys(), total=10):  
            boxes = ps_dict[frame_id]['gt_boxes'].copy() # orig
            boxes[:,:3] -= dataset.dataset_cfg.SHIFT_COOR # Translate ground frame bboxes to dataset label sensor frame
            p_anno = {"frame_id": frame_id,
                    "name": np.array([cfg.CLASS_NAMES[int(abs(box[7]))] for box in boxes]), # TODO: map supercategory to dataset specific class names
                    "pred_labels": np.array([abs(box[7]) for box in boxes]),
                    "boxes_lidar": boxes[:,:7],
                    "score": boxes[:,8]}
           

            pred_annos.append(p_anno)
            gt_annos.append(eval_gt_annos[dataset.frameid_to_idx[frame_id]])

            # gt_annos.append(eval_gt_annos[frame_id]['annos'])

  

    ######
    # go over GT annos in order to add empty data for gt_boxes lidar and other classes to match the number of names (including the dont cares!!!) 
    for current_frame in gt_annos:
        missing_objects_len = len(current_frame['annos']['name']) - len(current_frame['annos']['gt_boxes_lidar'])
        if missing_objects_len != 0:
            zeros_list = [0] * 7
            current_frame['annos']['gt_boxes_lidar'] = np.append(current_frame['annos']['gt_boxes_lidar'], [zeros_list]*missing_objects_len, axis=0)

        
    #### WAYMO EVAL STARTS ####
    from tools.eval_utils.cross_domain_eval_tools import transform_to_waymo_format 

    mod_gt_annos = transform_to_waymo_format(cfg.DATASET, gt_annos, is_gt=True)
    mod_det_annos = transform_to_waymo_format(cfg.DATASET, pred_annos, is_gt=False)


    def waymo_eval(eval_det_annos, eval_gt_annos, class_names, **kwargs):
        from pcdet.datasets.waymo.waymo_eval import OpenPCDetWaymoDetectionMetricsEstimator
        eval = OpenPCDetWaymoDetectionMetricsEstimator()
        veh_iou_threshold = kwargs['veh_iou_threshold'] if 'veh_iou_threshold' in kwargs else 0.7
        ped_iou_threshold = kwargs['ped_iou_threshold'] if 'ped_iou_threshold' in kwargs else 0.5
        cyc_iou_threshold = kwargs['cyc_iou_threshold'] if 'cyc_iou_threshold' in kwargs else 0.3

        eval_breakdown = kwargs['eval_breakdown'] if 'eval_breakdown' in kwargs else 'RANGE'

        ap_dict = eval.waymo_evaluation(
            eval_det_annos, eval_gt_annos, class_name=class_names,
            distance_thresh=1000, fake_gt_infos=False, 
            veh_iou_threshold=veh_iou_threshold, ped_iou_threshold=ped_iou_threshold, cyc_iou_threshold=cyc_iou_threshold,
            breakdown_generator_ids=eval_breakdown
        )
        ap_result_str = '\n'
        for key in ap_dict:
            ap_dict[key] = ap_dict[key][0]
            ap_result_str += '%s: %.4f \n' % (key, ap_dict[key])

        return ap_result_str, ap_dict

    CLASS_NAMES= ['Vehicle', 'Pedestrian', 'Cyclist']

    ap_result_str, ap_dict = waymo_eval(mod_det_annos, mod_gt_annos, CLASS_NAMES, 
                                        veh_iou_threshold=0.5, ped_iou_threshold=0.3, cyc_iou_threshold=0.3, eval_breakdown='RANGE')

    print(ap_result_str)
    # print(ap_dict)

    with open('cfgs/target_kitti/ALL.txt', 'w') as f:
        f.write(ap_result_str)
    #### WAYMO EVAL ENDS ####

    # cd tools
    # python3 cfgs/evaluate_kitti_w_waymo.py --cfg_file /MS3D/tools/cfgs/dataset_configs/kitti_raw_dataset_da.yaml --ps_dict /MS3D/tools/cfgs/target_kitti/label_generation/round1/ps_labels/ALL_6_6_6.pkl