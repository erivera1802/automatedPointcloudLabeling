#!/bin/bash

# bash /MS3D/tools/cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/pretrained/lyft_pt_dets_pv_a.sh
# bash /MS3D/tools/cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/pretrained/lyft_pt_dets_pv_c.sh
# bash /MS3D/tools/cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/pretrained/lyft_pt_dets_vx_a.sh
# bash /MS3D/tools/cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/pretrained/lyft_pt_dets_vx_c.sh

# bash /MS3D/tools/cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/pretrained/nusc_pt_dets_pv_a.sh
# bash /MS3D/tools/cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/pretrained/nusc_pt_dets_pv_c.sh
# bash /MS3D/tools/cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/pretrained/nusc_pt_dets_vx_a.sh
# bash /MS3D/tools/cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/pretrained/nusc_pt_dets_vx_c.sh

bash /MS3D/tools/cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/pretrained/waymo_pt_dets_pv_a.sh
bash /MS3D/tools/cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/pretrained/waymo_pt_dets_pv_c.sh
bash /MS3D/tools/cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/pretrained/waymo_pt_dets_vx_a.sh
bash /MS3D/tools/cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/pretrained/waymo_pt_dets_vx_c.sh

# pipeline:
# bash cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/generate_ensemble_preds.sh
# bash cfgs/target_argo/label_generation/round1_used_waymo_final/scripts/run_ms3d.sh
# python cfgs/evaluate_initial_ps.py --cfg_file /MS3D/tools/cfgs/dataset_configs/kitti_raw_dataset_da.yaml --ps_dict /MS3D/tools/cfgs/target_kitti/label_generation/round1_used_waymo_final/ps_labels/initial_pseudo_labels.pkl
