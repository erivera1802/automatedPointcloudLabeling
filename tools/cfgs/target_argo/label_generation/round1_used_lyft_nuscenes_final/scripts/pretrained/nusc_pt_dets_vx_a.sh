#!/bin/bash

# ---- single frame ----
python3 test.py --cfg_file ../model_zoo/nuscenes_pretrained/cfgs/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.yaml \
                --ckpt ../model_zoo/nuscenes_pretrained/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.pth \
                --eval_tag nusc10xyzt_argo190_notta \
                --target_dataset argo --sweeps 1 --use_tta 0 --custom_target_scenes \
                # --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 1 MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/nuscenes_pretrained/cfgs/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/nuscenes_pretrained/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.pth \
#                 --eval_tag nusc10xyzt_argo190_rwr \
#                 --target_dataset argo --sweeps 1 --use_tta 2 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 1 MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/nuscenes_pretrained/cfgs/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/nuscenes_pretrained/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.pth \
#                 --eval_tag nusc10xyzt_argo190_rwf \
#                 --target_dataset argo --sweeps 1 --use_tta 1 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 1 MODEL.POST_PROCESSING.EVAL_METRIC none

python3 test.py --cfg_file ../model_zoo/nuscenes_pretrained/cfgs/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.yaml \
                --ckpt ../model_zoo/nuscenes_pretrained/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.pth \
                --eval_tag nusc10xyzt_argo190_rwf_rwr \
                --target_dataset argo --sweeps 1 --use_tta 3 --custom_target_scenes \
                # --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 1 MODEL.POST_PROCESSING.EVAL_METRIC none          

# # ---- multi frame ----
# python3 test.py --cfg_file ../model_zoo/nuscenes_pretrained/cfgs/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/nuscenes_pretrained/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.pth \
#                 --eval_tag nusc10xyzt_waymo2xyzt_argo190_notta \
#                 --target_dataset argo --sweeps 2 --use_tta 0 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 1 MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/nuscenes_pretrained/cfgs/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/nuscenes_pretrained/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.pth \
#                 --eval_tag nusc10xyzt_waymo2xyzt_argo190_rwf_rwr \
#                 --target_dataset argo --sweeps 2 --use_tta 3 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 1 MODEL.POST_PROCESSING.EVAL_METRIC none   

# python3 test.py --cfg_file ../model_zoo/nuscenes_pretrained/cfgs/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/nuscenes_pretrained/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.pth \
#                 --eval_tag nusc10xyzt_waymo3xyzt_argo190_notta \
#                 --target_dataset argo --sweeps 3 --use_tta 0 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 1 MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/nuscenes_pretrained/cfgs/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/nuscenes_pretrained/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.pth \
#                 --eval_tag nusc10xyzt_waymo3xyzt_argo190_rwf_rwr \
#                 --target_dataset argo --sweeps 3 --use_tta 3 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 1 MODEL.POST_PROCESSING.EVAL_METRIC none   

# python3 test.py --cfg_file ../model_zoo/nuscenes_pretrained/cfgs/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/nuscenes_pretrained/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.pth \
#                 --eval_tag nusc10xyzt_waymo4xyzt_argo190_notta \
#                 --target_dataset argo --sweeps 4 --use_tta 0 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 1 MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/nuscenes_pretrained/cfgs/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/nuscenes_pretrained/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.pth \
#                 --eval_tag nusc10xyzt_waymo4xyzt_argo190_rwf_rwr \
#                 --target_dataset argo --sweeps 4 --use_tta 3 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 1 MODEL.POST_PROCESSING.EVAL_METRIC none                                                

# python3 test.py --cfg_file ../model_zoo/nuscenes_pretrained/cfgs/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/nuscenes_pretrained/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.pth \
#                 --eval_tag nusc10xyzt_waymo5xyzt_argo190_notta \
#                 --target_dataset argo --sweeps 5 --use_tta 0 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 1 MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/nuscenes_pretrained/cfgs/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/nuscenes_pretrained/nuscenes_uda_voxel_rcnn_anchorhead_10xyzt_allcls.pth \
#                 --eval_tag nusc10xyzt_waymo5xyzt_argo190_rwf_rwr \
#                 --target_dataset argo --sweeps 5 --use_tta 3 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 1 MODEL.POST_PROCESSING.EVAL_METRIC none

# ---------------------

