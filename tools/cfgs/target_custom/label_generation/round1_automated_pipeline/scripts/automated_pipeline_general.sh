#!/bin/bash
set -e  # Exit on error
trap 'echo "Error occurred! Exiting..."; exit 1;' ERR


DIR="/MS3D/data/edgar/TO_PSEUDO_LABEL"
# DIR="/MS3D/data/manual_annotation_edgar"
SAVE_DIR=""

# Process rosbag folders and prepare LiDAR data for pseudo-labeling.
python3 /MS3D/utils/autopipeline_data.py --save_dir "/MS3D/data/edgar/TO_PSEUDO_LABEL"


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


# Loop through each folder in edgar/data
for rosbag_folder in ${DIR}/*; do
    if [[ -d "$rosbag_folder" ]]; then
        echo "Processing folder: $rosbag_folder"

        # Step 1: Generate .pkl file
        echo "Generating .pkl file for $rosbag_folder"
        python3 -m pcdet.datasets.custom.custom_dataset create_infos "$rosbag_folder"

        # Step 2: Generate LiDAR odometry
        echo "Generating LiDAR odometry in $rosbag_folder"
        cd "$rosbag_folder"
        bash generate_lidar_odom.sh
        cd - > /dev/null

        # Step 3: Update YAML configuration
        echo "Updating YAML configuration for $rosbag_folder"
        python3 cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/update_custom_dataset_da_yaml.py --mcap_path "$rosbag_folder"

        # Step 4: Run the automated pipeline
        echo "Running automated pipeline for $rosbag_folder"
        bash cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/automated_pipeline.sh --save_dir_label "${SAVE_DIR}"

    else
        echo "Skipping $rosbag_folder (not a directory)"
    fi
done

echo '  '
echo 'ALL DATA IS AUTOLABELED'
echo '  '

# bash /MS3D/tools/cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/automated_pipeline_general.sh


# bash cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/automated_pipeline_general.sh --save_dir_label "/MS3D/test_label_location2"