import subprocess
import os
import shutil
import argparse

## MUST BE EXECUTED INSIDE MS3D DOCKER !!!
## Generate lidar odom sh, info pkls, imagesets and train.txt 

def parse_config():
    parser = argparse.ArgumentParser(description='arg parser')
    parser.add_argument('--save_dir', type=str)
    args = parser.parse_args()

    return args

target_cfg = parse_config()
save_dir = target_cfg.save_dir


for rosbag_folder in os.listdir(save_dir):
    folder_path = save_dir+f"/{rosbag_folder}"
    #run from custom_data foder
    os.chdir(f"{folder_path}")
    command_lidar_odom =  "bash generate_lidar_odom.sh"
    subprocess.run(command_lidar_odom, shell=True, check=True)
    
