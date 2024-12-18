"""
MS3D Step 1

DESCRIPTION:
    Combine detection sets of the ensemble with KBF. Saves a pkl file containing a list of 
    dicts where each dict contains a single detection set (and optional metadata) for each frame

EXAMPLE:
    python ensemble_kbf.py --ps_cfg /MS3D/tools/cfgs/target_nuscenes/ms3d_ps_config_rnd1.yaml 
"""

import sys
sys.path.append('../')
import argparse
import yaml
from pcdet.utils import box_fusion_utils, ms3d_utils
from pcdet.config import cfg


def get_target_domain_cfg(cfg, dataset_name, sweeps, custom_target_scenes=False, use_tta=0):
    """
    Simplify the testing of a single pre-trained model on multiple target domains
    by adding in target dataset configs (i.e. DATA_CONFIG_TAR) rather than having
    to duplicate the yaml file and manually specify a DATA_CONFIG_TAR for each new 
    target domain.

    use_tta = 0: no_tta, 1: rwf, 2: rwr, 3: rwr+rwf
    """
    from easydict import EasyDict
    import yaml
    def load_yaml(fname):
        with open(fname, 'r') as f:
            try:
                ret = yaml.safe_load(f, Loader=yaml.FullLoader)
            except:
                ret = yaml.safe_load(f)
        return ret
    
    # Modify cfg in-place to add DATA_CONFIG_TAR
    cfg.DATA_CONFIG_TAR = {}        
        
    if dataset_name == 'nuscenes':
        target_base_config = load_yaml('/MS3D/tools/cfgs/dataset_configs/nuscenes_dataset_da.yaml')
        target_base_config['MAX_SWEEPS'] = sweeps
    elif dataset_name == 'waymo':
        target_base_config = load_yaml('/MS3D/tools/cfgs/dataset_configs/waymo_dataset_da.yaml')
        # target_base_config = load_yaml('/MS3D/tools/cfgs/dataset_configs/waymo_dataset_multiframe_da.yaml')
        target_base_config['SEQUENCE_CONFIG']['SAMPLE_OFFSET'] = [-int(sweeps-1), 0]
    elif dataset_name == 'kitti_raw':
        target_base_config = load_yaml('/MS3D/tools/cfgs/dataset_configs/kitti_raw_dataset_da.yaml')
        target_base_config['SEQUENCE_CONFIG']['SAMPLE_OFFSET'] = [-int(sweeps-1), 0]
    elif dataset_name == 'lyft':
        target_base_config = load_yaml('/MS3D/tools/cfgs/dataset_configs/lyft_dataset_da.yaml')
        target_base_config['MAX_SWEEPS'] = sweeps
    elif dataset_name == 'custom':
        target_base_config = load_yaml('/MS3D/tools/cfgs/dataset_configs/custom_dataset_da.yaml')
        target_base_config['MAX_SWEEPS'] = sweeps
    elif dataset_name == 'argo':
        target_base_config = load_yaml('/MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml')
        target_base_config['MAX_SWEEPS'] = sweeps
    elif dataset_name == 'kitti':
        target_base_config = load_yaml('/MS3D/tools/cfgs/dataset_configs/kitti_dataset.yaml')
        target_base_config['SEQUENCE_CONFIG']['SAMPLE_OFFSET'] = [-int(sweeps-1), 0]

    else:
        raise NotImplementedError

    cfg.DATA_CONFIG_TAR.update(EasyDict(target_base_config))    

    return cfg

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='arg parser')                   
    parser.add_argument('--ps_cfg', type=str, help='cfg file with MS3D parameters')
    parser.add_argument('--len', type=int, default=1, help='set length of data to reduce computation time for debugging')
    parser.add_argument('--save_dir', type=str, default=None, help='Overwrite save dir in the cfg file')
    parser.add_argument('--exp_name', type=str, default=None, help='Overwrite exp_name in the cfg file')
    parser.add_argument('--save_dir_label', type=str, default=None, help='Overwrite save dir in the cfg file')


    parser.add_argument('--target_dataset', type=str, default=None, help='select from: nuscenes, waymo_single, waymo_multi, lyft or custom')
    parser.add_argument('--sweeps', type=int, default=1, help='number of accumulated frames including current frame')

    args = parser.parse_args()


    ms3d_configs = yaml.load(open(args.ps_cfg,'r'), Loader=yaml.Loader)

    # Load detection sets
    det_annos = box_fusion_utils.load_src_paths_txt(ms3d_configs['DETS_TXT'])
    num_det_sets = len(det_annos)-1 # don't count det_annos[det_cls_weights] in the length
    detection_sets = box_fusion_utils.get_detection_sets(det_annos, score_th=0.1)
    print('Number of detection sets: ', num_det_sets)

    # Downsample for debugging
    if args.len > 1:
        detection_sets = detection_sets[:args.len]

    # Get class specific config
    cls_kbf_config = {}
    for enum, cls in enumerate(box_fusion_utils.SUPERCATEGORIES): # Super categories for MS3D compatibility across datasets
        if cls in cls_kbf_config.keys():
            continue
        cls_kbf_config[cls] = {}
        cls_kbf_config[cls]['cls_id'] = enum+1 # in OpenPCDet, cls_ids enumerate from 1
        cls_kbf_config[cls]['discard'] = ms3d_configs['ENSEMBLE_KBF']['DISCARD'][enum]
        cls_kbf_config[cls]['radius'] = ms3d_configs['ENSEMBLE_KBF']['RADIUS'][enum]
        cls_kbf_config[cls]['nms'] = ms3d_configs['ENSEMBLE_KBF']['NMS'][enum]
        cls_kbf_config[cls]['neg_th'] = ms3d_configs['PS_SCORE_TH']['NEG_TH'][enum]

    # Combine detection sets into a single set of initial pseudo-labels
    ps_dict = box_fusion_utils.get_initial_pseudo_labels(detection_sets, cls_kbf_config)
    # save_dir = ms3d_configs['SAVE_DIR'] if args.save_dir is None else args.save_dir
    save_dir = args.save_dir_label or ms3d_configs['SAVE_DIR']
    

    if args.target_dataset is not None:
        target_cfg = get_target_domain_cfg(cfg, args.target_dataset, args.sweeps)
        ms3d_utils.save_data(ps_dict, save_dir, name=f"{target_cfg.DATA_CONFIG_TAR.DATA_PATH.split('/')[-1]}.pkl")
    else:
        ms3d_utils.save_data(ps_dict, save_dir, name=f"initial_pseudo_labels.pkl")
    print(f" {save_dir} saved: initial_pseudo_labels.pkl\n")