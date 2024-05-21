#!/bin/bash

python3 ensemble_kbf.py --ps_cfg /MS3D/tools/cfgs/target_kitti/label_generation/round1/cfgs/ps_config.yaml

# --- It often helps to stop here and analyse the ensemble_kbf output pkl first to properly set pos_th and trk scores ----

# python generate_tracks.py --ps_cfg /MS3D/tools/cfgs/target_custom/label_generation/round1/cfgs/ps_config.yaml --cls_id 1
# python generate_tracks.py --ps_cfg /MS3D/tools/cfgs/target_custom/label_generation/round1/cfgs/ps_config.yaml --cls_id 1 --static_veh
# python generate_tracks.py --ps_cfg /MS3D/tools/cfgs/target_custom/label_generation/round1/cfgs/ps_config.yaml --cls_id 2
# python temporal_refinement.py --ps_cfg /MS3D/tools/cfgs/target_custom/label_generation/round1/cfgs/ps_config.yaml 


# bash cfgs/target_kitti/label_generation/round1/scripts/run_ms3d.sh

