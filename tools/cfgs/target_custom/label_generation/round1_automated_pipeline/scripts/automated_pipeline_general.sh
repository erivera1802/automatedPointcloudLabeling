#!/bin/bash

# DIR="/MS3D/data/edgar"
DIR="/MS3D/data/edgar/TO_PSEUDO_LABEL"
#DIR="/MS3D/data/edgar_11_06"
# DIR="/MS3D/data/manual_annotation_edgar"

# CONVERT RAW ROSBAGS INTO PSEUDOLABEL FORMAT
python3 cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/auto_lidar_ms3d.py --save_dir "${DIR}"

# Loop through each folder in edgar/data
for mcap_folder in ${DIR}/*; do
    # UPDATE [DATA_PATH key of custom_dataset_da.yaml] WITH REGARDING MCAP 
    python3 cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/update_custom_dataset_da_yaml.py --mcap_path "${mcap_folder}"

    # AUTO-LABEL THE MCAP
    bash cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/automated_pipeline.sh
done

echo '  '
echo 'ALL DATA IS AUTOLABELED'
echo '  '

# bash /MS3D/tools/cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/automated_pipeline_general.sh