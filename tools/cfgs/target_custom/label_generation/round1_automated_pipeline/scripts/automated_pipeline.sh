#!/bin/bash

#   PATH TO THE AUTOLABEL FOLDER
CUSTOM_PATH="/MS3D/tools/cfgs/target_custom/label_generation/round1_automated_pipeline"

echo "  "
echo "PSEDUO-LABELING YOUR CUSTOM DATA"
echo "  "

bash ${CUSTOM_PATH}/scripts/pretrained/lyft_pt_dets_pv_a.sh
bash ${CUSTOM_PATH}/scripts/pretrained/lyft_pt_dets_pv_c.sh
bash ${CUSTOM_PATH}/scripts/pretrained/lyft_pt_dets_vx_a.sh
bash ${CUSTOM_PATH}/scripts/pretrained/lyft_pt_dets_vx_c.sh

bash ${CUSTOM_PATH}/scripts/pretrained/nusc_pt_dets_pv_a.sh
bash ${CUSTOM_PATH}/scripts/pretrained/nusc_pt_dets_pv_c.sh
bash ${CUSTOM_PATH}/scripts/pretrained/nusc_pt_dets_vx_a.sh
bash ${CUSTOM_PATH}/scripts/pretrained/nusc_pt_dets_vx_c.sh

bash ${CUSTOM_PATH}/scripts/pretrained/waymo_pt_dets_pv_a.sh
bash ${CUSTOM_PATH}/scripts/pretrained/waymo_pt_dets_pv_c.sh
bash ${CUSTOM_PATH}/scripts/pretrained/waymo_pt_dets_vx_a.sh
bash ${CUSTOM_PATH}/scripts/pretrained/waymo_pt_dets_vx_c.sh


echo "  "
echo "SAVING RESULT PREDICTIONS TO THE ENSEMBLE_DETECTIONS.TXT"
echo "  "
python3 cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/ensemble_preds.py --target_dataset custom 


echo "  "
echo "ENSEMBLING THE DETECTIONS"
echo "  "
python3 ensemble_kbf.py --ps_cfg ${CUSTOM_PATH}/cfgs/ps_config.yaml --target_dataset custom 


echo "  "
echo "CHECK OUT PS_LABELS FOLDER; YOU SHOULD HAVE THE INITIAL_PS_PKL"
echo "  "