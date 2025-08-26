# #!/bin/sh
# set -e # Exit immediately if a command exits with a non-zero status.

# # --- Check if a scene name was provided ---
# if [ -z "$1" ]; then
#   echo "Error: No scene name provided." >&2
#   echo "Usage: ./entrypoint.sh <scene_name>" >&2
#   exit 1
# fi

# # --- Assign the first command-line argument to SCENE_NAME ---
# SCENE_NAME=$1
# cd /MS3D
# python setup.py develop
# cd tracker
# pip install -e . --user
# cd ..
# cd tools/
# git config --global --add safe.directory /MS3D

# echo "Setup complete. Running pipeline for scene: ${SCENE_NAME}"

# bash /MS3D/tools/cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/automated_pipeline_general.sh --save_dir_label labels --rosbag_folder_name ${SCENE_NAME}


#!/bin/sh
set -e # Exit immediately if a command exits with a non-zero status.

# --- Check if a scene name was provided ---
if [ -z "$1" ]; then
  echo "Error: No scene name provided." >&2
  echo "Usage: ./entrypoint.sh <scene_name | DO_ALL>" >&2
  exit 1
fi

# --- Assign the first command-line argument to SCENE_NAME ---
SCENE_NAME=$1

# --- !!! IMPORTANT !!! ---
# --- Set the path to the parent folder containing all your scene directories ---
SCENES_PARENT_FOLDER="/MS3D/pointclouds_final"


# --- Your existing setup commands ---
cd /MS3D
python setup.py develop
cd tracker
pip install -e . --user
cd ..
cd tools/
git config --global --add safe.directory /MS3D


# --- Conditional Logic: Process one scene or all scenes ---
if [ "$SCENE_NAME" = "DO_ALL" ]; then
  echo "Setup complete. Processing all scenes in ${SCENES_PARENT_FOLDER}..."
  
  # Loop through all subdirectories in the scenes folder
  for scene_path in "$SCENES_PARENT_FOLDER"/*/; do
    # Get just the directory name from the full path
    current_scene_name=$(basename "$scene_path")
    echo "--- Processing scene: $current_scene_name ---"
    
    # Execute the pipeline script for the current scene
    bash /MS3D/tools/cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/automated_pipeline_general.sh --save_dir_label labels --rosbag_folder_name "$current_scene_name"
  done

  echo "--- All scenes processed. ---"
else
  echo "Setup complete. Running pipeline for scene: ${SCENE_NAME}"

  # Execute the pipeline script for the single specified scene
  bash /MS3D/tools/cfgs/target_custom/label_generation/round1_automated_pipeline/scripts/automated_pipeline_general.sh --save_dir_label labels --rosbag_folder_name "${SCENE_NAME}"
fi