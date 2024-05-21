#!/bin/bash

python test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_voxel_rcnn_anchorhead_4f_xyzt_allcls.yaml \
                --ckpt ../model_zoo/waymo_pretrained/waymo_voxel_rcnn_anchorhead_4f_xyzt_allcls.pth \
                --eval_tag waymo4xyzt_waymo1xyzt_notta \
                --target_dataset waymo --sweeps 1 --batch_size 8 --use_tta 0 \
                --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none

python test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_voxel_rcnn_anchorhead_4f_xyzt_allcls.yaml \
                --ckpt ../model_zoo/waymo_pretrained/waymo_voxel_rcnn_anchorhead_4f_xyzt_allcls.pth \
                --eval_tag waymo4xyzt_waymo1xyzt_rwf_rwr \
                --target_dataset waymo --sweeps 1 --batch_size 8 --use_tta 3 \
                --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none 

# python test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_voxel_rcnn_anchorhead_4f_xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/waymo_pretrained/waymo_voxel_rcnn_anchorhead_4f_xyzt_allcls.pth \
#                 --eval_tag waymo4xyzt_waymo2xyzt_notta \
#                 --target_dataset waymo --sweeps 2 --batch_size 8 --use_tta 0 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none

# python test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_voxel_rcnn_anchorhead_4f_xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/waymo_pretrained/waymo_voxel_rcnn_anchorhead_4f_xyzt_allcls.pth \
#                 --eval_tag waymo4xyzt_waymo2xyzt_rwf_rwr \
#                 --target_dataset waymo --sweeps 2 --batch_size 8 --use_tta 3 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none                                

# python test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_voxel_rcnn_anchorhead_4f_xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/waymo_pretrained/waymo_voxel_rcnn_anchorhead_4f_xyzt_allcls.pth \
#                 --eval_tag waymo4xyzt_waymo4xyzt_notta \
#                 --target_dataset waymo --sweeps 4 --batch_size 8 --use_tta 0 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none

# python test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_voxel_rcnn_anchorhead_4f_xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/waymo_pretrained/waymo_voxel_rcnn_anchorhead_4f_xyzt_allcls.pth \
#                 --eval_tag waymo4xyzt_waymo4xyzt_rwf_rwr \
#                 --target_dataset waymo --sweeps 4 --batch_size 8 --use_tta 3 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none                                                             

# ---------------------