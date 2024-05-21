#!/bin/bash

python3 test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_uda_voxel_rcnn_anchorhead_1xyz_allcls.yaml \
                --ckpt ../model_zoo/waymo_pretrained/waymo_uda_voxel_rcnn_anchorhead_1xyz_allcls.pth \
                --eval_tag waymo1xyz_custom1xyz_notta \
                --target_dataset custom --sweeps 1 --batch_size 8 --use_tta 0 \
                --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none

python3 test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_uda_voxel_rcnn_anchorhead_1xyz_allcls.yaml \
                --ckpt ../model_zoo/waymo_pretrained/waymo_uda_voxel_rcnn_anchorhead_1xyz_allcls.pth \
                --eval_tag waymo1xyz_custom1xyz_rwf_rwr \
                --target_dataset custom --sweeps 1 --batch_size 8 --use_tta 3 \
                --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none 

# python3 test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_uda_voxel_rcnn_anchorhead_1xyz_allcls.yaml \
#                 --ckpt ../model_zoo/waymo_pretrained/waymo_uda_voxel_rcnn_anchorhead_1xyz_allcls.pth \
#                 --eval_tag waymo1xyz_custom2xyz_notta \
#                 --target_dataset custom --sweeps 2 --batch_size 8 --use_tta 0 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_uda_voxel_rcnn_anchorhead_1xyz_allcls.yaml \
#                 --ckpt ../model_zoo/waymo_pretrained/waymo_uda_voxel_rcnn_anchorhead_1xyz_allcls.pth \
#                 --eval_tag waymo1xyz_custom2xyz_rwf_rwr \
#                 --target_dataset custom --sweeps 2 --batch_size 8 --use_tta 3 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none                                

# python3 test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_uda_voxel_rcnn_anchorhead_1xyz_allcls.yaml \
#                 --ckpt ../model_zoo/waymo_pretrained/waymo_uda_voxel_rcnn_anchorhead_1xyz_allcls.pth \
#                 --eval_tag waymo1xyz_custom1xyz_notta \
#                 --target_dataset custom --sweeps 1 --batch_size 8 --use_tta 0 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_uda_voxel_rcnn_anchorhead_1xyz_allcls.yaml \
#                 --ckpt ../model_zoo/waymo_pretrained/waymo_uda_voxel_rcnn_anchorhead_1xyz_allcls.pth \
#                 --eval_tag waymo1xyz_custom1xyz_rwf_rwr \
#                 --target_dataset custom --sweeps 1 --batch_size 8 --use_tta 3 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none                                                             

# ---------------------