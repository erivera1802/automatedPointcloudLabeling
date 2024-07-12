import subprocess
import os
import shutil
import json
import open3d as o3d
import numpy as np
import pandas as pd

def check_points_labels_files_same():
    labels_list = sorted(os.listdir("/OpenPCDet/data/custom/labels"))
    point_list = sorted(os.listdir("/OpenPCDet/data/custom/points"))
    for i in range(len(point_list)):
        file_name_point= point_list[i]
        file_root_point, file_ext = os.path.splitext(file_name_point)
        file_name_label= labels_list[i]
        file_root_label, file_ext_label = os.path.splitext(file_name_label)
        #import pdb;pdb.set_trace()
        if file_root_point  != file_root_label:
            print( "NOT SAME FILE NAME FOR INDEX !!", i , file_root_point, file_root_label)
            


def save_points_labels_in_openpcdet_format():
    for rosbag_folder in sorted(os.listdir(ms3d_data_path)):
        os.makedirs(f"{openpcdet_save_dir}/custom", exist_ok=True)
        sequences = f"{ms3d_data_path}/{rosbag_folder}/sequences"
        labels_path = f"/MS3D/tools/cfgs/target_custom/label_generation/round1_automated_pipeline/ps_labels/{rosbag_folder}.pkl"
        labels_save_dir = f"/OpenPCDet/data/custom/labels"
        os.makedirs(labels_save_dir,exist_ok=True)
        convert_labels(labels_path,labels_save_dir)
        for seq in sorted(os.listdir(sequences)):
             this_seq_lidar = f"{ms3d_data_path}/{rosbag_folder}/sequences/{seq}/lidar" # /MS3D/data/edgar/PSEUDO_LABELED/2024_04_11_bakery_weeklytest_004/sequences/sequence_0/lidar
             for pcd_file in sorted(os.listdir(this_seq_lidar)):
                 pcd_path = f"{this_seq_lidar}/{pcd_file}"
                 np_points = convert_pcd2npy(pcd_path)
                 pcd_file_root, file_ext = os.path.splitext(pcd_file)
                 #import pdb;pdb.set_trace()
                 if '_' in pcd_file_root:
                    pcd_file_root = pcd_file_root.replace('_', '')
                 save_path_npy = f"/OpenPCDet/data/custom/points/{pcd_file_root}.npy"
                 os.makedirs(f"/OpenPCDet/data/custom/points",exist_ok=True)
                 np.save(save_path_npy, np_points)

    print("----save_points_labels_in_openpcdet_format----- done -----")


def convert_labels(ps_labels_path,save_dir):
    ps_labels = pd.read_pickle(ps_labels_path)
    #save_dir ="/home/altb/utils/trial_openpcdet_data"
    #os.makedirs(save_dir,exist_ok=True)
    #import pdb;pdb.set_trace()
    # for sequence in sorted(ps_labels.keys()):
    for sequence,values in sorted(ps_labels.items()):
        num_str = str(sequence)
        # Insert an underscore after the 10th digit
        formatted_num = num_str[:10] + '_' + num_str[10:]
        file_path = save_dir + f'/{sequence}.txt'
        if os.path.exists(file_path):
            print("THIS PCD FILE NAME ALREADY EXISTS HENCE IT IT WILL APPEND")
        result_item = values['gt_boxes']

        if len(result_item) == 0:
            with open(file_path, 'a') as file:
                line = "empty"
                file.write(line)

        for i in range(len(result_item)):
            item = result_item[i]
            center_x, center_y, center_z = item[0],item[1],item[2]
            length, width, height = item[3], item[4], item[5]
            rotation_angle = item[6]
            label = item[-2] 
            if label == 2:
                class_name = "Pedestrian"
            elif label ==1 :
                class_name = "Cyclist"
            else:
                class_name = "Vehicle"

            with open(file_path, 'a') as file:
                # Write the header line
                line = f"{center_x} {center_y} {center_z} {length} {width} {height} {rotation_angle} {class_name} """"\n"""""
                file.write(line)

    print("----convert_labels----- done -----")


def convert_pcd2npy(pcd_file):
    pcd = o3d.io.read_point_cloud(pcd_file)
    # Convert to a NumPy array
    points = np.asarray(pcd.points)
    return points



def find_empty_files():
    count = 0
    empty_files=[]
    for file in sorted(os.listdir('/OpenPCDet/data/custom/labels')):
        with open(f'/OpenPCDet/data/custom/labels/{file}', 'r') as file:
            # Read all lines into a list
            lines = file.readlines()
            # Iterate over the list
            for line in lines:
                # Process the line (e.g., print it)
                word = (line.strip())
                #import pdb;pdb.set_trace()
                if word == 'empty':
                    count+=1
                    print(file.name)
                    empty_files.append(file.name)
    print(count)

    np.save('empty_list_array.npy', empty_files)

    print("----find_empty_files----- done ----- saved as empty_list_array.npy ")

    return empty_files



def find_rosbag_of_empty_frames(empty_files):
    for file in empty_files:
        file_name = file.split("/")[-1]
        file_name = file_name.split(".")[0]
        file_name = file_name[:10] + "_" + file_name[10:] + ".pcd"

        base_path = "/MS3D/data/edgar/TO_PSEUDO_LABEL"

        for rosbag_folder in os.listdir(base_path):

            for sequence in os.listdir(base_path+ "/" +rosbag_folder+"/sequences"):
  
                for pcd_file in os.listdir(base_path+ "/" +rosbag_folder+"/sequences" + "/" + sequence+"/lidar"):

                    if pcd_file == file_name:
                        count += 1
                        print(pcd_file ,"following rosbag_folder has the empty frame:", rosbag_folder , sequence)



def delete_empty_files():
    loaded_array = np.load('empty_list_array.npy')
    for current_file in loaded_array:
        os.remove(current_file) #DELETE FROM LABELS

        last_part = current_file.split("/")[-1].replace(".txt",".npy")
        os.remove("/OpenPCDet/data/custom/points/" + last_part) #DELETE FROM POINTS



if __name__ == '__main__':

    ms3d_data_path = '/MS3D/data/edgar/PSEUDO_LABELED'
    # ms3d_data_path = '/MS3D/data/edgar/TO_PSEUDO_LABEL'
    openpcdet_save_dir = '/OpenPCDet/data'

    # SAVE POINTS AND LABELS IN OPENPCDET FORMAT
    save_points_labels_in_openpcdet_format()


    # CHECK CODE IF ALL POINTS AND LABELS FILES MATCH
    check_points_labels_files_same()


    # FIND FRAMES WITHOUT ANY PREDICTION
    empty_files = find_empty_files()


    # FIND WHICH ROSBAG FOLDER AND SEQUENCES HAS EMPTY FRAMES
    # find_rosbag_of_empty_frames(empty_files)


    # DELETE EMPTY FILES
    delete_empty_files()


    #  GENERATE PICKLES
    # python -m pcdet.datasets.custom.custom_dataset create_custom_infos tools/cfgs/dataset_configs/custom_dataset.yaml