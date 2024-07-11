import os

# List of python3 commands to run
python3_commands = [
    "python3 /MS3D/tools/visualize_bev_for_argo.py --cfg_file /MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml --ps_pkl /MS3D/tools/cfgs/target_argo/label_generation/round1_used_ALL_final/ps_labels/lyft_and_nuscenes_used.pkl --split val --idx 0 ",
          
    "python3 /MS3D/tools/visualize_bev_for_argo.py --cfg_file /MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml --ps_pkl /MS3D/tools/cfgs/target_argo/label_generation/round1_used_ALL_final/ps_labels/lyft_and_nuscenes_used.pkl --split val --idx 1 ",

    "python3 /MS3D/tools/visualize_bev_for_argo.py --cfg_file /MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml --ps_pkl /MS3D/tools/cfgs/target_argo/label_generation/round1_used_ALL_final/ps_labels/lyft_and_nuscenes_used.pkl --split val --idx 10 ",

    "python3 /MS3D/tools/visualize_bev_for_argo.py --cfg_file /MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml --ps_pkl /MS3D/tools/cfgs/target_argo/label_generation/round1_used_ALL_final/ps_labels/lyft_and_nuscenes_used.pkl --split val --idx 50 ",

    "python3 /MS3D/tools/visualize_bev_for_argo.py --cfg_file /MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml --ps_pkl /MS3D/tools/cfgs/target_argo/label_generation/round1_used_ALL_final/ps_labels/lyft_and_nuscenes_used.pkl --split val --idx 100 ",

    "python3 /MS3D/tools/visualize_bev_for_argo.py --cfg_file /MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml --ps_pkl /MS3D/tools/cfgs/target_argo/label_generation/round1_used_ALL_final/ps_labels/lyft_and_nuscenes_used.pkl --split val --idx 150 ",

    "python3 /MS3D/tools/visualize_bev_for_argo.py --cfg_file /MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml --ps_pkl /MS3D/tools/cfgs/target_argo/label_generation/round1_used_ALL_final/ps_labels/lyft_and_nuscenes_used.pkl --split val --idx 200 ",

    "python3 /MS3D/tools/visualize_bev_for_argo.py --cfg_file /MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml --ps_pkl /MS3D/tools/cfgs/target_argo/label_generation/round1_used_ALL_final/ps_labels/lyft_and_nuscenes_used.pkl --split val --idx 250 ",

    "python3 /MS3D/tools/visualize_bev_for_argo.py --cfg_file /MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml --ps_pkl /MS3D/tools/cfgs/target_argo/label_generation/round1_used_ALL_final/ps_labels/lyft_and_nuscenes_used.pkl --split val --idx 300 ",

    "python3 /MS3D/tools/visualize_bev_for_argo.py --cfg_file /MS3D/tools/cfgs/dataset_configs/argo2_dataset.yaml --ps_pkl /MS3D/tools/cfgs/target_argo/label_generation/round1_used_ALL_final/ps_labels/lyft_and_nuscenes_used.pkl --split val --idx 500 ",

]

# Run each python3 command in the list 
for command in python3_commands:
    os.system(command)
