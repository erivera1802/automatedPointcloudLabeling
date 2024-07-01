import os
from collections import defaultdict

# 

def count_matching_pcd_files(base_path):

    rosbags_with_common_pcd = {}
    
    for current_rosbag in os.listdir(base_path):

        temp_path = base_path + "/" + current_rosbag 
        
        for mcaps in os.listdir(temp_path):
            lidar_folder = os.path.join(temp_path, mcaps)
            
            if mcaps not in rosbags_with_common_pcd:
                rosbags_with_common_pcd[mcaps] = 1
            else:
                rosbags_with_common_pcd[mcaps] += 1
                print("WARNING", mcaps)
       
                

    # Step 4: Find files that appear in at least two sequence folders
    matching_files = [file for file, count in rosbags_with_common_pcd.items() if count >= 2]

    return matching_files

# Base path to the sequences
# base_path = '/home/altb/automatedpclabelling/data/manual_annotation_edgar/2024_06_11_garching_labelinggarching_000/sequences'
base_path= "/home/altb/rosbags"

# Get the list of matching PCD files
matching_pcd_files = count_matching_pcd_files(base_path)

# Output the result
print(f"PCD files that appear in at least two sequence folders: {matching_pcd_files}")
print(f"PCD files that appear in at least two sequence folders: {len(matching_pcd_files)}")

