#!/bin/bash

# Check if the .env file exists
if [ ! -f .env ]; then
    echo ".env file not found!"
    exit 1
fi

# Load environment variables from the .env file
source .env

# Print the environment variables
echo "ROOT: $DATASET_ROOT"
echo "NAME: $DATASET_NAME"
echo "VERSION": "$DATASET_VERSION"
echo "ANNO": "$ANNOTATIONS_PATH"
DATASET_PATH="$DATASET_ROOT/$DATASET_NAME"
DATASET_FOLDER="$DATASET_PATH/$DATASET_VERSION"
echo "VAR2: $DATASET_FOLDER"
rm -r $DATASET_FOLDER
mkdir -p $DATASET_FOLDER
#python3 pcd2bin.py --dataset_path $DATASET_PATH --rides_pcd_path $PCD_FOLDER_LOCATION
python3 create_visibility.py --dataset_path $DATASET_PATH --dataset_version $DATASET_VERSION
python3 create_attribute.py --dataset_path $DATASET_PATH --dataset_version $DATASET_VERSION
python3 create_categories.py --dataset_path $DATASET_PATH --dataset_version $DATASET_VERSION
python3 create_sensor.py --dataset_path $DATASET_PATH --dataset_version $DATASET_VERSION
python3 create_log.py --dataset_path $DATASET_PATH --dataset_version $DATASET_VERSION  --rides_pcd_path $PCD_FOLDER_LOCATION
python3 create_map.py --dataset_path $DATASET_PATH --dataset_version $DATASET_VERSION
python3 create_ego_pose.py --dataset_path $DATASET_PATH --dataset_version $DATASET_VERSION
python3 create_calibrated_sensor.py --dataset_path $DATASET_PATH --dataset_version $DATASET_VERSION
python3 create_scene.py --dataset_path $DATASET_PATH --dataset_version $DATASET_VERSION --rides_pcd_path $PCD_FOLDER_LOCATION
python3 create_samples_samplesdata_samplesannotation.py --dataset_path $DATASET_PATH --dataset_version $DATASET_VERSION --annotations_path $ANNOTATIONS_PATH
python3 update_firstlast.py --dataset_path $DATASET_PATH --dataset_version $DATASET_VERSION

