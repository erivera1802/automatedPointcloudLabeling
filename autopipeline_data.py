import subprocess
import os
import shutil

#### MUST BE EXECUTED OUTSIDE OF MS3D DOCKER!

#rosbag_folder_path = "/home/altb/pointclouds_new/garching_10_06_2024" 
# rosbag_folder_path =  "/home/altb/pointclouds_new/garching_11_06"
rosbag_folder_path =  "/home/altb/pointclouds_new/to_pseudolabel"



#save_dir = "/home/altb/idp-ms3d/data/edgar"
#save_dir =  "/home/altb/automatedpclabelling/data/edgar_11_06"
save_dir = "/home/altb/automatedpclabelling/data/edgar/TO_PSEUDO_LABEL"


if not os.path.exists(save_dir):
    os.makedirs(save_dir, exist_ok=True)


for rosbag_folder in sorted(os.listdir(rosbag_folder_path)):
    folder_path = save_dir+f"/{rosbag_folder}"
    os.makedirs(folder_path,exist_ok=True)
   # print(folder_path)
    shutil.copy("/home/altb/automatedpclabelling/data/custom/generate_lidar_odom.sh",folder_path)
    print(f"Processing rosbag {rosbag_folder}")
    os.makedirs(save_dir+f"/{rosbag_folder}/ImageSets",exist_ok=True)
    os.makedirs(save_dir+f"/{rosbag_folder}/sequences",exist_ok=True)
    for id,mcap_file in enumerate(os.listdir( rosbag_folder_path+f"/{rosbag_folder}")):
        os.makedirs(save_dir+f"/{rosbag_folder}/sequences/sequence_{id}",exist_ok=True)
        pcd_file_path_source = rosbag_folder_path+f"/{rosbag_folder}"+f"/{mcap_file}/pcd"
        pcd_file_path_dest = save_dir+f"/{rosbag_folder}/sequences/sequence_{id}/lidar"
        os.makedirs(save_dir+f"/{rosbag_folder}/sequences/sequence_{id}/lidar",exist_ok=True)
        #print(pcd_file_path_source,pcd_file_path_dest)
        command_copy = f"cp -r {pcd_file_path_source}/* {pcd_file_path_dest}/"
        subprocess.run(command_copy, shell=True, check=True)

        #shutil.copytree(pcd_file_path_source,pcd_file_path_dest)

    os.chdir(folder_path)
    command_create_set = f'ls sequences > ImageSets/train.txt'
    subprocess.run(command_create_set, shell=True, check=True)
    #comman_lidar_odom =  "bash generate_lidar_odom.sh"
    # subprocess.run(comman_lidar_odom, shell=True, check=True)
    #create_info = "python3 -m pcdet.datasets.custom.custom_dataset create_infos /MS3D/data/custom_dataset_name"
    #subprocess.run(create_info)