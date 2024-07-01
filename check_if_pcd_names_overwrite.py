import os
from collections import defaultdict

def count_matching_pcd_files(base_path):

    counter_dict = {}
    pcd_belong_to_which_rosbag = {}
    rosbags_with_common_pcd = {}

    all_rosbags_pcd_belongs = {}
    
    for current_rosbag in os.listdir(base_path):

        temp_path = base_path + "/" + current_rosbag + "/sequences"
        # Step 1: List sequence folders
        sequence_folders = [os.path.join(temp_path, folder) for folder in os.listdir(temp_path) if os.path.isdir(os.path.join(temp_path, folder))]

        for sequence_folder in sequence_folders:
            lidar_folder = os.path.join(sequence_folder, 'lidar')
            if os.path.exists(lidar_folder) and os.path.isdir(lidar_folder):

                sequence_str= sequence_folder.split("/")[-1]
                # Step 2: List PCD files in the lidar folder
                for file in os.listdir(lidar_folder):
                    if file.endswith('.pcd'):
                        if file not in counter_dict:
                            counter_dict[file] = 1
                            pcd_belong_to_which_rosbag[file] = current_rosbag
                            all_rosbags_pcd_belongs[file] = [current_rosbag+"_"+sequence_str]

                        else: 
                            counter_dict[file] += 1
                            all_rosbags_pcd_belongs[file].append([current_rosbag+"_"+sequence_str])

                            if current_rosbag+"_"+sequence_str not in rosbags_with_common_pcd:
                                rosbags_with_common_pcd[current_rosbag+"_"+sequence_str] = 1
                                
                            else:
                                rosbags_with_common_pcd[current_rosbag+"_"+sequence_str] += 1
                            
                            if pcd_belong_to_which_rosbag[file]+"_"+sequence_str not in rosbags_with_common_pcd:
                                rosbags_with_common_pcd[pcd_belong_to_which_rosbag[file]+"_"+sequence_str] = 1

                            else:
                                rosbags_with_common_pcd[pcd_belong_to_which_rosbag[file]+"_"+sequence_str] += 1

    
    # Step 4: Find files that appear in at least two sequence folders
    matching_files = [file for file, count in counter_dict.items() if count >= 2]

    return matching_files

# Base path to the sequences
# base_path = '/home/altb/automatedpclabelling/data/manual_annotation_edgar/2024_06_11_garching_labelinggarching_000/sequences'
base_path= "/home/altb/automatedpclabelling/data/edgar/seq_ordered"
# base_path= "/home/altb/pointclouds_final"

# Get the list of matching PCD files
matching_pcd_files = count_matching_pcd_files(base_path)

# Output the result
print(f"PCD files that appear in at least two sequence folders: {matching_pcd_files}")
print(f"PCD files that appear in at least two sequence folders: {len(matching_pcd_files)}")

