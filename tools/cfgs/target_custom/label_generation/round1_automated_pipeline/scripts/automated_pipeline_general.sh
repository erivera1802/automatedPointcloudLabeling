#!/bin/bash
set -e  # Exit on error
trap 'echo "Error occurred! Exiting..."; exit 1;' ERR


DIR="/MS3D/data/edgar/TO_PSEUDO_LABEL"
# DIR="/MS3D/data/manual_annotation_edgar"
SAVE_DIR=""

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

echo "Save directory for labels: ${SAVE_DIR}"

# CONVERT RAW ROSBAGS INTO PSEUDOLABEL FORMAT
python3 cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/auto_lidar_ms3d.py --save_dir "${DIR}"

# Loop through each folder in edgar/data
for mcap_folder in ${DIR}/*; do
    # UPDATE [DATA_PATH key of custom_dataset_da.yaml] WITH REGARDING MCAP 
    python3 cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/update_custom_dataset_da_yaml.py --mcap_path "${mcap_folder}"

    # AUTO-LABEL THE MCAP
    bash cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/automated_pipeline.sh --save_dir_label ${SAVE_DIR}
done

echo '  '
echo 'ALL DATA IS AUTOLABELED'
echo '  '

# bash /MS3D/tools/cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/automated_pipeline_general.sh


# bash cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/automated_pipeline_general.sh --save_dir_label "/MS3D/test_label_location2"