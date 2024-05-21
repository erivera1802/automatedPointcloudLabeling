#!/bin/bash

# ---- single frame ----
python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.yaml \
                --ckpt ../model_zoo/lyft_pretrained/lyft_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.pth \
                --eval_tag lyft1xyz_custom190_notta \
                --target_dataset custom --sweeps 1 --use_tta 0 --custom_target_scenes \
                --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 2 MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.yaml \
#                 --ckpt ../model_zoo/lyft_pretrained/lyft_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.pth \
#                 --eval_tag lyft1xyz_custom190_rwr \
#                 --target_dataset custom --sweeps 1 --use_tta 2 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 2 MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.yaml \
#                 --ckpt ../model_zoo/lyft_pretrained/lyft_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.pth \
#                 --eval_tag lyft1xyz_custom190_rwf \
#                 --target_dataset custom --sweeps 1 --use_tta 1 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 2 MODEL.POST_PROCESSING.EVAL_METRIC none

python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.yaml \
                --ckpt ../model_zoo/lyft_pretrained/lyft_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.pth \
                --eval_tag lyft1xyz_custom190_rwf_rwr \
                --target_dataset custom --sweeps 1 --use_tta 3 --custom_target_scenes \
                --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 2 MODEL.POST_PROCESSING.EVAL_METRIC none                                                              

# ---- multi frame ----

# python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_pv_rcnn_plusplus_resnet_centerhead_3f_xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/lyft_pretrained/lyft_pv_rcnn_plusplus_resnet_centerhead_3f_xyzt_allcls.pth \
#                 --eval_tag lyft3xyzt_waymo3xyzt_custom190_notta \
#                 --target_dataset custom --sweeps 3 --use_tta 0 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 2 MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_pv_rcnn_plusplus_resnet_centerhead_3f_xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/lyft_pretrained/lyft_pv_rcnn_plusplus_resnet_centerhead_3f_xyzt_allcls.pth \
#                 --eval_tag lyft3xyzt_waymo3xyzt_custom190_rwf_rwr \
#                 --target_dataset custom --sweeps 3 --use_tta 3 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 2 MODEL.POST_PROCESSING.EVAL_METRIC none  

# python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_pv_rcnn_plusplus_resnet_centerhead_3f_xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/lyft_pretrained/lyft_pv_rcnn_plusplus_resnet_centerhead_3f_xyzt_allcls.pth \
#                 --eval_tag lyft3xyzt_waymo5xyzt_custom190_notta \
#                 --target_dataset custom --sweeps 5 --use_tta 0 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 2 MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_pv_rcnn_plusplus_resnet_centerhead_3f_xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/lyft_pretrained/lyft_pv_rcnn_plusplus_resnet_centerhead_3f_xyzt_allcls.pth \
#                 --eval_tag lyft3xyzt_waymo5xyzt_custom190_rwf_rwr \
#                 --target_dataset custom --sweeps 5 --use_tta 3 --custom_target_scenes \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 2 MODEL.POST_PROCESSING.EVAL_METRIC none                                

# ---------------------