import os
import argparse
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


def parse_config():
    parser = argparse.ArgumentParser(description='arg parser')
    parser.add_argument('--target_dataset', type=str, default=None, help='select from: nuscenes, waymo_single, waymo_multi, lyft or custom')
    parser.add_argument('--sweeps', type=int, default=1, help='number of accumulated frames including current frame')

    args = parser.parse_args()
    
    if args.target_dataset is not None:
        _ = get_target_domain_cfg(cfg, args.target_dataset, args.sweeps)
        
    return _


def main():
    target_cfg = parse_config()

    # Define the base directory (assuming it changes)
    base_dir = "/MS3D/output/model_zoo_" + target_cfg.DATA_CONFIG_TAR.DATA_PATH.split('/')[-1] 

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Define the output file path
    parent_dir = os.path.dirname(script_dir)
    output_file = os.path.join(parent_dir, 'cfgs', 'ensemble_detections.txt')

    # Ensure the cfgs directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)


    # Initialize a list to store the paths
    result_paths = []

    # Walk through the directory tree
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file == 'result.pkl':
                # Get the full path of the result.pkl file
                full_path = os.path.join(root, file)
                # Append it to the result paths list
                result_paths.append(full_path)

    # Write the paths to the output file
    with open(output_file, 'w') as f:
        for path in result_paths:
            f.write(f"{path}\n")

    print(f"Ensemble detections file created with {len(result_paths)} paths.")




if __name__ == '__main__':
    main()
