#!/bin/bash

python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls.yaml \
                --ckpt ../model_zoo/lyft_pretrained/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls.pth \
                --eval_tag lyft3xyzt_kitti_raw1xyzt_notta \
                --target_dataset kitti_raw --sweeps 1 --batch_size 4 --use_tta 0 \
                #--set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC kitti 

python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls.yaml \
                --ckpt ../model_zoo/lyft_pretrained/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls.pth \
                --eval_tag lyft3xyzt_kitti_rawxyzt_rwf_rwr \
                --target_dataset kitti_raw --sweeps 1 --batch_size 4 --use_tta 3 \
               # --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC kitti 

# python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/lyft_pretrained/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls.pth \
#                 --eval_tag lyft3xyzt_custom2xyzt_notta \
#                 --target_dataset kitti_raw --sweeps 2 --batch_size 4 --use_tta 0 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC kitti 

# python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/lyft_pretrained/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls.pth \
#                 --eval_tag lyft3xyzt_custom2xyzt_rwf_rwr \
#                 --target_dataset kitti_raw --sweeps 2 --batch_size 4 --use_tta 3 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC kitti      

# python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/lyft_pretrained/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls.pth \
#                 --eval_tag lyft3xyzt_custom4xyzt_notta \
#                 --target_dataset kitti_raw --sweeps 4 --batch_size 4 --use_tta 0 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC kitti 

# python3 test.py --cfg_file ../model_zoo/lyft_pretrained/cfgs/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls.yaml \
#                 --ckpt ../model_zoo/lyft_pretrained/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls.pth \
#                 --eval_tag lyft3xyzt_custom4xyzt_rwf_rwr \
#                 --target_dataset kitti_raw --sweeps 4 --batch_size 4 --use_tta 3 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC kitti 

# ---------------------