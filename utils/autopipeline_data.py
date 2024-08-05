import argparse
import subprocess
import os
import shutil

def main(rosbag_folder_path,rosbag_folder_name, save_dir):
    
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    if rosbag_folder_name == "DO_ALL":
        rosbag_list = sorted(os.listdir(rosbag_folder_path))
    else:
        rosbag_list = [rosbag_folder_name]
        
    for rosbag_folder in rosbag_list:
        folder_path = os.path.join(save_dir, rosbag_folder)
        os.makedirs(folder_path, exist_ok=True)
        shutil.copy("/MS3D/utils/generate_lidar_odom.sh", folder_path)
        print(f"Processing rosbag {rosbag_folder}")
        
        image_sets_path = os.path.join(folder_path, "ImageSets")
        sequences_path = os.path.join(folder_path, "sequences")
        os.makedirs(image_sets_path, exist_ok=True)
        os.makedirs(sequences_path, exist_ok=True)
        seq_id = "000"
        sequence_folder = os.path.join(sequences_path, f"sequence_{seq_id}")
        os.makedirs(sequence_folder, exist_ok=True)
        lidar_folder = os.path.join(sequence_folder, "lidar")
        os.makedirs(lidar_folder, exist_ok=True)

        pcd_file_path_source = os.path.join(rosbag_folder_path, rosbag_folder, "pcd")
        command_copy = f"cp -r {pcd_file_path_source}/* {lidar_folder}/"
        subprocess.run(command_copy, shell=True, check=True)
        # for id, mcap_file in enumerate(sorted(os.listdir(os.path.join(rosbag_folder_path, rosbag_folder)))):
        #     seq_id = mcap_file.split("_")[-1]
        #     sequence_folder = os.path.join(sequences_path, f"sequence_{seq_id}")
        #     os.makedirs(sequence_folder, exist_ok=True)
        #     lidar_folder = os.path.join(sequence_folder, "lidar")
        #     os.makedirs(lidar_folder, exist_ok=True)
            
        #     pcd_file_path_source = os.path.join(rosbag_folder_path, rosbag_folder, mcap_file, "pcd")
        #     command_copy = f"cp -r {pcd_file_path_source}/* {lidar_folder}/"
        #     subprocess.run(command_copy, shell=True, check=True)
        
        os.chdir(folder_path)
        command_create_set = 'ls sequences > ImageSets/train.txt'
        subprocess.run(command_create_set, shell=True, check=True)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process rosbag folders and prepare data for pseudo labeling.')
    parser.add_argument('--rosbag_folder_path', type=str, required=False, default= '/MS3D/pointclouds_final', help='Path to the rosbag folder.')
    parser.add_argument('--rosbag_folder_name', type=str, required=False, default= 'DO_ALL', help='name of rosbag folder.')
    parser.add_argument('--save_dir', type=str, required=True, help='Directory where the processed data will be saved.')
    
    args = parser.parse_args()
    main(args.rosbag_folder_path, args.rosbag_folder_name, args.save_dir)


# python3 autopipeline_data.py --save_dir /MS3D/data/edgar/TO_PSEUDO_LABEL
# python3 autopipeline_data.py --rosbag_folder_name 2024_06_27_schwabing_daily_001 --save_dir /MS3D/data/edgar/TO_PSEUDO_LABEL
# python3 utils/autopipeline_data.py --rosbag_folder_name 2024_06_11_garching_labelinggarching_000_all --save_dir /MS3D/data/edgar/TO_PSEUDO_LABEL