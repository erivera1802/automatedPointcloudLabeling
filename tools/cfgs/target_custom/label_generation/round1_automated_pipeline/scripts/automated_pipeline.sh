#!/bin/bash
set -e  # Exit on error
trap 'echo "Error occurred! Exiting..."; exit 1;' ERR


#   PATH TO THE AUTOLABEL FOLDER
CUSTOM_PATH="/MS3D/tools/cfgs/target_custom/label_generation/round1_automated_pipeline"

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --save_dir_label)
      SAVE_DIR="$2"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done



echo "  "
echo "PSEDUO-LABELING YOUR CUSTOM DATA"
echo "  "

bash ${CUSTOM_PATH}/scripts/pretrained/lyft_pt_dets_pv_a.sh
bash ${CUSTOM_PATH}/scripts/pretrained/lyft_pt_dets_pv_c.sh
bash ${CUSTOM_PATH}/scripts/pretrained/lyft_pt_dets_vx_a.sh
bash ${CUSTOM_PATH}/scripts/pretrained/lyft_pt_dets_vx_c.sh

# bash ${CUSTOM_PATH}/scripts/pretrained/nusc_pt_dets_pv_a.sh
# bash ${CUSTOM_PATH}/scripts/pretrained/nusc_pt_dets_pv_c.sh
# bash ${CUSTOM_PATH}/scripts/pretrained/nusc_pt_dets_vx_a.sh
# bash ${CUSTOM_PATH}/scripts/pretrained/nusc_pt_dets_vx_c.sh

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
python3 ensemble_kbf.py --ps_cfg ${CUSTOM_PATH}/cfgs/ps_config.yaml --target_dataset custom --save_dir_label ${SAVE_DIR}


echo "  "
echo "CHECK OUT PS_LABELS FOLDER; YOU SHOULD HAVE THE INITIAL_PS_PKL"
echo "  "