import pandas as pd
import numpy as np
import argparse
import os
from scipy.spatial.transform import Rotation
import uuid
import json


# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

def get_sample_data_entry_by_filename(dataset_root, filename):
    sample_data_file_path = os.path.join(dataset_root, 'v1.0-mini/sample_data.json')
    
    # Check if the file exists
    if not os.path.exists(sample_data_file_path):
        print(f"File not found: {sample_data_file_path}")
        return None
    
    # Read the JSON file
    with open(sample_data_file_path, 'r') as f:
        sample_data = json.load(f)
    
    # Find and return the entry with the matching filename
    for entry in sample_data:
        if entry['filename'] == filename:
            return entry
    
    print(f"No entry found with filename: {filename}")
    return None


def read_annotation(pointclouds_path, pickle_path,score_threshold):
    """Function to 3d visualize predicted boxes of a pcd file using the frame_id and score threshold.
    Used for MS3D data format(.pcd) and predictions(pickle)

    Args:
        pcd_path (string): Path to the .pcd file (pointcloud data) (e.g 1718127846_799991808.pcd)
        prediction_pickle_path (string): path to prediction pickle file. 
        This pickle file must be in MS3D generated format (consists of the rosbag predictions with all frame_ids)
        confidence_threshold (float): To visualize objects which are above a certain threshold.
    """    


    result = pd.read_pickle(pickle_path) 
    pcd_path = os.listdir(pointclouds_path)[0]
    file_name = pcd_path.split('/')[-1]
    if '_' in file_name:
            file_name = file_name.replace('_','')
    frame_id = file_name.split('.pcd.bin')[0]

    result_item = result[frame_id]["gt_boxes"] # pseudo pickle 
    print(result_item) 


    # 0,1,2 = x, y, z 
    # 3,4,5 = l, w, h
    # 6 = rotation_angle
    # 7 = class
    # 8 = score

    CLASS_NAMES= ['Vehicle', 'Pedestrian', 'Cyclist']

    labels = []
    sample_annotation_data = []
    for item in result_item:
        label = item[-2]
        labels.append(int(label))
        score = item[8]
        center = [item[0],item[1],item[2]]
        lwh = item[3:6] * 1
        axis_angles = np.array([0, 0, item[6] + 1e-10])
        ## TODO: CHECK
        rot = Rotation.from_euler('xyz', axis_angles, degrees=False)
        rot_quat = rot.as_quat()
        print(rot_quat)
        sample_data_token = get_sample_data_entry_by_filename(dataset_root="../muenchen",filename="")
        sample_annotation_entry = {
                "token": create_token(),
                "sample_token": sample_token,
                "instance_token": create_token(),  # Generate a new instance token for each annotation
                "visibility_token": create_token(),  # Assuming visibility info is available
                "attribute_tokens": [create_token()],  # Assuming attributes are available
                "translation": annotation.get('translation', [0.0, 0.0, 0.0]),
                "size": annotation.get('size', [1.0, 1.0, 1.0]),
                "rotation": annotation.get('rotation', [0.0, 0.0, 0.0, 1.0]),
                "num_lidar_pts": annotation.get('num_lidar_pts', 0),
                "num_radar_pts": annotation.get('num_radar_pts', 0),
                "next": None  # Update if there is a link to the next annotation
            }
        sample_annotation_data.append(sample_annotation_entry)

def main():
    parser = argparse.ArgumentParser(description="Visualize point cloud data and bounding boxes.")
    parser.add_argument('--pointclouds_path', type=str,default="../muenchen/samples/LIDAR_TOP/",help="Path to the .pcd.bin file containing pointcloud data.")
    parser.add_argument('--prediction_pickle_path', type=str,default="../muenchen/pcd_annotations/2024_07_22_muenchen_labeling_000.pkl", help="Path to the pickle file containing prediction results in ms3d format.")
    parser.add_argument('--confidence_threshold', type=float,default=0.4, help="The minimum confidence score required to display bounding boxes.")

    args = parser.parse_args()

    read_annotation(args.pointclouds_path, args.prediction_pickle_path, args.confidence_threshold)

if __name__ == '__main__':
    ## usage python3 pseudolabel_visualizer_3d.py --pointcloud_path /Users/begumaltunbas/Desktop/idp/VISUALIZATION_EVALUATION/lepeng09_new/1718127706_599949824.pcd --prediction_pickle_path /Users/begumaltunbas/Desktop/idp/VISUALIZATION_EVALUATION/lepeng09_new/lepeng_09_not_labeled.pkl --confidence_threshold 0.4
    main()