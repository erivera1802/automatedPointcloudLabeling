import numpy as np
import copy
import sys
sys.path.append('/MS3D')
import argparse
from tqdm import tqdm
import pickle
from pcdet.config import cfg, cfg_from_yaml_file
from pcdet.utils import common_utils
from pcdet.datasets import build_dataloader
from pcdet.datasets.kitti.kitti_object_eval_python.kitti_common import get_label_annos
from pcdet.datasets.kitti.kitti_utils import transform_annotations_to_kitti_format


SUPERCATEGORIES= ['Car', 'Pedestrian', 'Cyclist']
SUPER_MAPPING= {'Car': 'Car',
                'car': 'Car',                                
                'truck': 'Car',
                'bus': 'Car',
                'Vehicle': 'Car',
                'bicycle': 'Cyclist',
                'motorcycle': 'Cyclist',
                'Cyclist': 'Cyclist',
                'pedestrian': 'Pedestrian',
                'Pedestrian': 'Pedestrian'}


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
    parser.add_argument('--cfg_file', type=str,help='just use the target dataset cfg file')
    parser.add_argument('--ps_dict', type=str, help='Use kbf ps_dict')
    parser.add_argument('--det_pkl', type=str, help='result.pkl from test.py')
    parser.add_argument('--interval', type=int, default=1, help='set interval')
    args = parser.parse_args()
    
    cfg_from_yaml_file(args.cfg_file, cfg)
    dataset = load_dataset(split='test')
    print('Evaluating for the classes: ', cfg.CLASS_NAMES)

    ps_dict = None
    if args.ps_dict:
        with open(args.ps_dict, 'rb') as f:
            ps_dict = pickle.load(f)

        # Evaluate
        pred_annos, gt_annos = [], []

        # eval_gt_annos = copy.deepcopy(dataset.infos)
        gt_annos = [copy.deepcopy(info['annos']) for info in dataset.infos] 

        for curr_idx, frame_id in enumerate(tqdm(ps_dict.keys(), total=len(ps_dict.keys()))):  
            boxes = ps_dict[frame_id]['gt_boxes'].copy() # orig
            boxes[:,:3] -= dataset.dataset_cfg.SHIFT_COOR # Translate ground frame bboxes to dataset label sensor frame 
            p_anno = {"frame_id": frame_id,
                    "boxes_lidar": boxes[:,:7],
                    'score': boxes[:,8],
                    'name': np.array([cfg.CLASS_NAMES[int(abs(box[7]))] for box in boxes]), 
                    }
            
            # min threshold filter
            # if len(p_anno['name']) != 0:
            #     veh_mask = np.zeros(len(p_anno['name']), dtype=bool)
            #     cls_veh_mask = p_anno['name'] == 'Vehicle'
            #     veh_mask.flat[np.flatnonzero(cls_veh_mask)[p_anno['score'][cls_veh_mask] > 0.6]] = True

            #     ped_mask = np.zeros(len(p_anno['name']), dtype=bool)
            #     cls_ped_mask = p_anno['name'] == 'Pedestrian'
            #     ped_mask.flat[np.flatnonzero(cls_ped_mask)[p_anno['score'][cls_ped_mask] > 0.4]] = True

            #     cyc_mask = np.zeros(len(p_anno['name']), dtype=bool)
            #     cls_cyc_mask = p_anno['name'] == 'Cyclist'
            #     cyc_mask.flat[np.flatnonzero(cls_cyc_mask)[p_anno['score'][cls_cyc_mask] > 0.4]] = True
                        
            #     combined_mask = np.logical_or.reduce((veh_mask, ped_mask, cyc_mask))
            #     for key in p_anno.keys():
            #         if key == 'frame_id':
            #             continue
            #         p_anno[key] = p_anno[key][combined_mask]
            # print(len(eval_gt_annos), eval_gt_annos[0])

            pred_annos.append(p_anno)

    # if args.det_pkl:

    #     with open(args.det_pkl, 'rb') as f:
    #         det_pkl = pickle.load(f)

    #     det_pkl = det_pkl[::args.interval] # ::2 is 18840 -> 9420

    #     # Evaluate single pred annos
    #     pred_annos, gt_annos = [], []
    #     eval_gt_annos = copy.deepcopy(dataset.infos)
    #     for p_anno in tqdm(det_pkl, total=len(det_pkl)):  
    #         p_anno['boxes_lidar'][:,:3] -= dataset.dataset_cfg.SHIFT_COOR # Translate ground frame bboxes to dataset label sensor frame
    #         pred_annos.append(p_anno)
    #         gt_annos.append(eval_gt_annos[dataset.frameid_to_idx[p_anno['frame_id']]]['annos'])            


    ##### 

    # class_names=[ 'Car', 'Pedestrian', 'Cyclist']

    # print('xx',gt_annos[0]['name'] )
    # print('yy',len(pred_annos[0]) )
    # print('gt??????????',gt_annos[0]['location'])
    # print('dt??????????',pred_annos[0]['location'])

    # print(gt_annos[0].keys(), pred_annos[0].keys())

    # result_dict = {}

    # for key, value in pred_annos[0].items():
    #     # Extract the last element from the value
    #     last_element = value[-1]
        
    #     # Store the last element in the result dictionary
    #     result_dict[key] = np.array([last_element])

    # print('dt!',result_dict['name'])
    # print('gt!',gt_annos[0]['name'])
    # for gt,dt in zip(result_dict.items(),gt_annos[0].items()):
    #     print('gt',gt)
    #     print('dt',dt)
    pred_annos= transform_annotations_to_kitti_format(pred_annos,SUPER_MAPPING)

    from pcdet.datasets.kitti.kitti_object_eval_python import eval as kitti_eval
    
    ap_result_str, ap_dict = kitti_eval.get_official_eval_result(gt_annos, pred_annos, cfg.CLASS_NAMES)
    # ap_result_str, ap_dict = kitti_eval.get_official_eval_result([gt_annos[0]], [result_dict], cfg.CLASS_NAMES)

    # item_result = pretty_print(ap_dict)

    # print(ap_result_str)
    # print(ap_dict)

    with open('cfgs/target_kitti/E1_17_results_new.txt', 'w') as f:
        f.write(ap_result_str)


    # cd tools
    #python cfgs/evaluate_initial_ps.py --cfg_file /MS3D/tools/cfgs/dataset_configs/kitti_raw_dataset_da.yaml --ps_dict /MS3D/tools/cfgs/target_kitti/label_generation/round1/ps_labels/initial_pseudo_labels.pkl















    # from pcdet.datasets.waymo.waymo_eval import OpenPCDetWaymoDetectionMetricsEstimator
    # eval = OpenPCDetWaymoDetectionMetricsEstimator()

    # ap_dict = eval.waymo_evaluation(
    #     pred_annos, gt_annos, class_name=cfg.CLASS_NAMES,
    #     distance_thresh=1000, fake_gt_infos=dataset.dataset_cfg.get('INFO_WITH_FAKELIDAR', False)
    # )
    # item_result = pretty_print(ap_dict)
    # if args.ps_dict:        
    #     print('Evaluated: ', args.ps_dict)
    #     item_result += f'Evaluated: {args.ps_dict}\n'
    # if args.det_pkl:
    #     print('Evaluated: ', args.det_pkl)        
    #     item_result += f'Evaluated: {args.det_pkl}\n'

    # with open('/MS3D/tools/cfgs/target_kitti/E1_17_results.txt', 'w') as f:
    #     f.write(item_result)

