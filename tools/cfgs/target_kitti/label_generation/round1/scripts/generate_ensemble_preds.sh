#!/bin/bash

# We set sweeps based on the assumption that your lidar data is at 10Hz
# bash cfgs/target_kitti/label_generation/round1/scripts/pretrained/lyft_pt_dets_pv_a.sh
# bash cfgs/target_kitti/label_generation/round1/scripts/pretrained/lyft_pt_dets_pv_c.sh
# bash cfgs/target_kitti/label_generation/round1/scripts/pretrained/lyft_pt_dets_vx_a.sh
# bash cfgs/target_kitti/label_generation/round1/scripts/pretrained/lyft_pt_dets_vx_c.sh

bash cfgs/target_kitti/label_generation/round1/scripts/pretrained/nusc_pt_dets_pv_a.sh
bash cfgs/target_kitti/label_generation/round1/scripts/pretrained/nusc_pt_dets_pv_c.sh
bash cfgs/target_kitti/label_generation/round1/scripts/pretrained/nusc_pt_dets_vx_a.sh
bash cfgs/target_kitti/label_generation/round1/scripts/pretrained/nusc_pt_dets_vx_c.sh

# bash cfgs/target_kitti/label_generation/round1/scripts/pretrained/waymo_pt_dets_pv_a.sh
# bash cfgs/target_kitti/label_generation/round1/scripts/pretrained/waymo_pt_dets_pv_c.sh
# bash cfgs/target_kitti/label_generation/round1/scripts/pretrained/waymo_pt_dets_vx_a.sh
# bash cfgs/target_kitti/label_generation/round1/scripts/pretrained/waymo_pt_dets_vx_c.sh

# bash cfgs/target_kitti/label_generation/round1/scripts/generate_ensemble_preds.sh
