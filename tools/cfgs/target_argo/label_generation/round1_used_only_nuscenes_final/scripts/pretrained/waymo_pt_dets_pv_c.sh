#!/bin/bash

# waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.yaml
# waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.pth

python3 test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.yaml \
                --ckpt ../model_zoo/waymo_pretrained/waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.pth \
                --eval_tag waymo4xyzt_argo1xyzt_notta \
                --target_dataset argo --sweeps 1 --batch_size 8 --use_tta 0 \
                --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 100 MODEL.POST_PROCESSING.EVAL_METRIC none

python3 test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.yaml \
                --ckpt ../model_zoo/waymo_pretrained/waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.pth \
                --eval_tag waymo4xyzt_argo1xyzt_rwf_rwr \
                --target_dataset argo --sweeps 1 --batch_size 8 --use_tta 3 \
                --set DATA_CONFIG_TAR.DATA_SPLIT.test train DATA_CONFIG_TAR.SAMPLED_INTERVAL.test 100 MODEL.POST_PROCESSING.EVAL_METRIC none 

# python3 test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.yaml \
#                 --ckpt ../model_zoo/waymo_pretrained/waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.pth \
#                 --eval_tag waymo4xyzt_argo2xyzt_notta \
#                 --target_dataset argo --sweeps 2 --batch_size 8 --use_tta 0 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.yaml \
#                 --ckpt ../model_zoo/waymo_pretrained/waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.pth \
#                 --eval_tag waymo4xyzt_argo2xyzt_rwf_rwr \
#                 --target_dataset argo --sweeps 2 --batch_size 8 --use_tta 3 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none                                

# python3 test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.yaml \
#                 --ckpt ../model_zoo/waymo_pretrained/waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.pth \
#                 --eval_tag waymo4xyzt_argo4xyzt_notta \
#                 --target_dataset argo --sweeps 4 --batch_size 8 --use_tta 0 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none

# python3 test.py --cfg_file ../model_zoo/waymo_pretrained/cfgs/waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.yaml \
#                 --ckpt ../model_zoo/waymo_pretrained/waymo_uda_pv_rcnn_plusplus_resnet_centerhead_1xyz_allcls.pth \
#                 --eval_tag waymo4xyzt_argo4xyzt_rwf_rwr \
#                 --target_dataset argo --sweeps 4 --batch_size 8 --use_tta 3 \
#                 --set DATA_CONFIG_TAR.DATA_SPLIT.test train MODEL.POST_PROCESSING.EVAL_METRIC none                                             

# ---------------------