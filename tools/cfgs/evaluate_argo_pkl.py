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

# SUPERCATEGORIES = ['Vehicle','Pedestrian','Cyclist']
# SUPER_MAPPING = {'car': 'Vehicle',
#                 'Car': 'Vehicle',
#                 'Veh': 'Vehicle',
#                 'Regular_vehicle': 'Vehicle',
#                 'truck': 'Vehicle',
#                 'bus': 'Vehicle',
#                 'Vehicle': 'Vehicle',
#                 'pedestrian': 'Pedestrian',
#                 'Pedestrian': 'Pedestrian',
#                 'motorcycle': 'Cyclist',
#                 'Bicyclist': 'Cyclist',
#                 'Bicycle': 'Cyclist',
#                 'bicyclist': 'Cyclist',
#                 'bicycle': 'Cyclist',
#                 'Cyclist': 'Cyclist'}

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
    parser.add_argument('--cfg_file', type=str, default='/MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml',
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
        
        eval_gt_annos_with_sample_idx_keys = {}
        for current_frame in eval_gt_annos:
            eval_gt_annos_with_sample_idx_keys[current_frame['sample_idx']] = current_frame
                
        # for frame_id in tqdm(ps_dict.keys(), total=len(ps_dict.keys())):  
        for frame_id in tqdm(ps_dict.keys(), total=10):  
            boxes = ps_dict[frame_id]['gt_boxes'].copy() # orig
            boxes[:,:3] -= dataset.dataset_cfg.SHIFT_COOR # Translate ground frame bboxes to dataset label sensor frame
            p_anno = {"frame_id": frame_id,
                    "name": np.array([cfg.CLASS_NAMES[int(abs(box[7]))] for box in boxes]), # TODO: map supercategory to dataset specific class names
                    "pred_labels": np.array([abs(box[7]) for box in boxes]),
                    "boxes_lidar": boxes[:,:7],
                    "score": boxes[:,8]}
           

            # if len(p_anno['name']) != 0:
            #     veh_mask = np.zeros(len(p_anno['name']), dtype=bool)
            #     cls_veh_mask = p_anno['name'] == 'Car'
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

            pred_annos.append(p_anno)
            # gt_annos.append(eval_gt_annos[dataset.argo2_infos.frameid_to_idx[frame_id]]['annos'])

            gt_annos.append(eval_gt_annos_with_sample_idx_keys[frame_id]['annos'])

  


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

    with open('cfgs/target_argo/nuscenes_only_1_1_1_discard.txt', 'w') as f:
        f.write(ap_result_str)
    #### WAYMO EVAL ENDS ####

    # cd tools
    # python3 cfgs/evaluate_argo_pkl.py --cfg_file /MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml --ps_dict /MS3D/tools/cfgs/target_argo/label_generation/round1_used_only_nuscenes_final/ps_labels/nuscenes_only_1_1_1_discard.pkl







    #### KITTI EVAL STARTS ####
    # from pcdet.datasets.kitti.kitti_utils import transform_annotations_to_kitti_format,transform_argo_GT_to_kitti_format
    # pred_annos_in_kitti_format = transform_annotations_to_kitti_format(pred_annos,SUPER_MAPPING) #transform pred_annos
    # gt_annos_in_kitti_format = transform_argo_GT_to_kitti_format(gt_annos,SUPER_MAPPING) #transform gt_annos
    # from pcdet.datasets.kitti.kitti_object_eval_python import eval as kitti_eval
    # ap_result_str, ap_dict = kitti_eval.get_official_eval_result([gt_annos_in_kitti_format[0]], [pred_annos_in_kitti_format[0]], cfg.CLASS_NAMES)
    # # ap_result_str, ap_dict = kitti_eval.get_official_eval_result(gt_annos[:20], pred_annos_in_kitti_format[:20], cfg.CLASS_NAMES)
    #### KITTI EVAL ENDS ####


    ### ALTERNATIVE WAY STARTS###
    # from pcdet.datasets.waymo.waymo_eval import OpenPCDetWaymoDetectionMetricsEstimator
    # eval = OpenPCDetWaymoDetectionMetricsEstimator()

    # ap_dict = eval.waymo_evaluation(
    # mod_det_annos, mod_gt_annos, class_name=cfg.CLASS_NAMES,
    # distance_thresh=1000, fake_gt_infos=dataset.dataset_cfg.get('INFO_WITH_FAKELIDAR', False)
    # )

    # item_result = pretty_print(ap_dict)
    # if args.ps_dict:        
    #     print('Evaluated: ', args.ps_dict)
    #     item_result += f'Evaluated: {args.ps_dict}\n'
    # if args.det_pkl:
    #     print('Evaluated: ', args.det_pkl)        
    #     item_result += f'Evaluated: {args.det_pkl}\n'

    # with open('/MS3D/tools/cfgs/target_argo/E1_final_results_with_lyft_nuscenes.txt', 'a') as f:
    #     f.write(item_result)
    ### ALTERNATIVE WAY ENDS###