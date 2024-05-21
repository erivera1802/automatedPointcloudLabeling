#!/bin/bash

# CONVERT RAW ROSBAGS INTO PSEUDOLABEL FORMAT
python3 cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/auto_lidar_ms3d.py

# Loop through each folder in edgar/data
for mcap_folder in /MS3D/data/edgar/*; do
    # UPDATE [DATA_PATH key of custom_dataset_da.yaml] WITH REGARDING MCAP 
    python3 cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/update_custom_dataset_da_yaml.py --mcap_path "${mcap_folder}"

    # AUTO-LABEL THE MCAP
    bash cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/automated_pipeline.sh
done

echo '  '
echo 'ALL DATA IS AUTOLABELED'
echo '  '