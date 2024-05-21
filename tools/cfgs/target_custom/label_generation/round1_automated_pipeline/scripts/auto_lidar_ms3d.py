import subprocess
import os
import shutil

## MUST BE EXECUTED INSIDE MS3D DOCKER !!!

save_dir = "/MS3D/data/edgar"

for rosbag_folder in os.listdir(save_dir):
    folder_path = save_dir+f"/{rosbag_folder}"
    #run from custom_data foder
    os.chdir(f"{folder_path}")
    command_lidar_odom =  "bash generate_lidar_odom.sh"
    subprocess.run(command_lidar_odom, shell=True, check=True)
    
    #run from ms3d folder
    os.chdir("/MS3D")
    python_executable = "python3" 
    module_path = "pcdet.datasets.custom.custom_dataset"
    rosbag_folder_path = f"/MS3D/data/edgar/{rosbag_folder}"
    command = [python_executable, "-m", module_path, "create_infos", rosbag_folder_path]

    subprocess.run(command)