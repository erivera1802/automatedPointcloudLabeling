import json
import os
import uuid
import pandas as pd
import numpy as np
import argparse
import os
from scipy.spatial.transform import Rotation
import uuid
import json

#ANNOTATIONS_PATH = "../muenchen/pcd_annotations/2024_07_22_muenchen_labeling_000.pkl"
ANNOTATIONS_PATH = "../muenchen/pcd_annotations/"
LABEL_DICT = {0:"vehicle.car", 1: "human.pedestrian.adult",2:"vehicle.bicycle"}
# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

# Function to read and print all unique sensor names in samples
def read_sensor_names(dataset_path, dataset_version):
    sample_data_file_path = os.path.join(dataset_path, f'{dataset_version}/sample_data.json')
    
    # Check if the file exists
    if not os.path.exists(sample_data_file_path):
        print(f"File not found: {sample_data_file_path}")
        return
    
    # Read the JSON file
    with open(sample_data_file_path, 'r') as f:
        sample_data = json.load(f)
    
    # Extract unique sensor names
    sensor_names = set()
    for sample in sample_data:
        sensor_names.add(sample["channel"])
    
    return sensor_names

def read_calibrated_sensor_json(dataset_path, dataset_version):
    calibrated_sensor_file_path = os.path.join(dataset_path, f'{dataset_version}/calibrated_sensor.json')
    
    # Check if the file exists
    if not os.path.exists(calibrated_sensor_file_path):
        print(f"File not found: {calibrated_sensor_file_path}")
        return
    
    # Read the JSON file
    with open(calibrated_sensor_file_path, 'r') as f:
        calibrated_sensor_data = json.load(f)
    
    # Print the contents in a human-readable format
    return calibrated_sensor_data


# Function to read and print sensor.json
def read_sensor_json(dataset_path, dataset_version):
    sensor_file_path = os.path.join(dataset_path, f'{dataset_version}/sensor.json')
    
    # Check if the file exists
    if not os.path.exists(sensor_file_path):
        print(f"File not found: {sensor_file_path}")
        return
    
    # Read the JSON file
    with open(sensor_file_path, 'r') as f:
        sensor_data = json.load(f)
    
    # Print the contents in a human-readable format
    return sensor_data


def read_ego_pose_json(dataset_path, dataset_version):
    ego_pose_file_path = os.path.join(dataset_path, f'{dataset_version}/ego_pose.json')
    
    # Check if the file exists
    if not os.path.exists(ego_pose_file_path):
        print(f"File not found: {ego_pose_file_path}")
        return
    
    # Read the JSON file
    with open(ego_pose_file_path, 'r') as f:
        ego_pose_data = json.load(f)
    
    # Print the contents in a human-readable format
    return ego_pose_data

def read_attribute_json(dataset_path, dataset_version):
    attribute_file_path = os.path.join(dataset_path, f'{dataset_version}/attribute.json')
    
    # Check if the file exists
    if not os.path.exists(attribute_file_path):
        print(f"File not found: {attribute_file_path}")
        return
    
    # Read the JSON file
    with open(attribute_file_path, 'r') as f:
        attribute_data = json.load(f)
    return attribute_data

# Function to read and print instance.json
def read_instance_json(dataset_path, dataset_version):
    instance_file_path = os.path.join(dataset_path, f'{dataset_version}/instance.json')
    
    # Check if the file exists
    if not os.path.exists(instance_file_path):
        print(f"File not found: {instance_file_path}")
        return
    
    # Read the JSON file
    with open(instance_file_path, 'r') as f:
        instance_data = json.load(f)
    return instance_data

#read_instance_json(dataset_path)[0]["token"]
def get_instance_token_from_category(instance_data,category_token):
    for entry in instance_data:
        if entry['category_token'] == category_token:
            return entry['token']
    
    print(f"No entry found with category token: {category_token}")
    return None
# def get_instance_token(dataset_path,dataset_version, label):
#     label_name = LABEL_DICT[label]
#     category_token = get_category_token(dataset_path=dataset_path, dataset_version=dataset_version, category_name=label_name)
#     instance_data = read_instance_json(dataset_path=dataset_path, dataset_version=dataset_version)
#     instance_token = get_instance_token_from_category(instance_data, category_token)
#     return instance_token
def get_category_token(dataset_path, dataset_version, category_name):
    category_file_path = os.path.join(dataset_path, f'{dataset_version}/category.json')
    
    # Check if the file exists
    if not os.path.exists(category_file_path):
        print(f"File not found: {category_file_path}")
        return None
    
    # Read the JSON file
    with open(category_file_path, 'r') as f:
        category_data = json.load(f)
    
    # Find and return the token of the entry with the matching category name
    for entry in category_data:
        if entry['name'] == category_name:
            return entry['token']
    
    print(f"No entry found with category name: {category_name}")
    return None

def read_visibility_json(dataset_path, dataset_version):
    visibility_file_path = os.path.join(dataset_path, f'{dataset_version}/visibility.json')
    
    # Check if the file exists
    if not os.path.exists(visibility_file_path):
        print(f"File not found: {visibility_file_path}")
        return
    
    # Read the JSON file
    with open(visibility_file_path, 'r') as f:
        visibility_data = json.load(f)
    return visibility_data
# Function to get the token of channel
def get_sensor_token(dataset_path, dataset_version, channel="LIDAR_TOP"):
    sensor_data = read_sensor_json(dataset_path, dataset_version)
    
    if sensor_data is None:
        return None
    
    for sensor in sensor_data:
        if sensor['channel'] == channel:
            return sensor['token']
    
    print("f{channel} channel not found in sensor.json")
    return None

# Function to get the modality of channel
def get_sensor_modality(dataset_path, dataset_version, channel="LIDAR_TOP"):
    sensor_data = read_sensor_json(dataset_path, dataset_version)
    
    if sensor_data is None:
        return None
    
    for sensor in sensor_data:
        if sensor['channel'] == channel:
            return sensor['modality']
    
    print(f"{channel} channel not found in sensor.json")
    return None

# Function to get the token of channel
def get_calibrated_sensor_token(dataset_path, dataset_version, sensor_token):
    calibrated_sensor_data = read_calibrated_sensor_json(dataset_path, dataset_version)
    
    if calibrated_sensor_data is None:
        return None
    
    for sensor in calibrated_sensor_data:
        if sensor['sensor_token'] == sensor_token:
            return sensor['token']
    
    print("f{channel} channel not found in calibrated_sensor.json")
    return None

def get_scene_token(scene_name, json_data):
    # Loop through each log entry in the JSON data
    for entry in json_data:
        # Check if the logfile matches the input parameter
        if entry.get("description") == scene_name:
            # Return the corresponding token
            return entry.get("token")
        

def read_annotation(pickle_path):
    """Function to 3d visualize predicted boxes of a pcd file using the frame_id and score threshold.
    Used for MS3D data format(.pcd) and predictions(pickle)

    Args:
        pcd_path (string): Path to the .pcd file (pointcloud data) (e.g 1718127846_799991808.pcd)
        prediction_pickle_path (string): path to prediction pickle file. 
        This pickle file must be in MS3D generated format (consists of the rosbag predictions with all frame_ids)
        confidence_threshold (float): To visualize objects which are above a certain threshold.
    """
    # Check if the PCD file exists
    if not os.path.exists(pickle_path):
        print(f"Folder not found: {pickle_path}")
        return     
    result = pd.read_pickle(pickle_path)
    return result

def read_multiple_annotations(pickles_path):
    # Check if the PCD file exists
    if not os.path.exists(pickles_path):
        print(f"Folder not found: {pickles_path}")
        return
    annotations = {}     
    for filename in os.listdir(pickles_path):
        pickle_filepath = os.path.join(pickles_path,filename)
        annotation = read_annotation(pickle_filepath)
        annotations.update(annotation)
    return annotations
def get_pointcloud_id(pcd_path):
    file_name = pcd_path.split('/')[-1]
    if '_' in file_name:
            file_name = file_name.replace('_','')
    frame_id = file_name.split('.pcd.bin')[0].split("+")[-1]
    return frame_id
    
def process_box_annotation(annotation):
    label = np.float64(annotation[-2])
    score = np.float64(annotation[8])
    center = [np.float64(annotation[0]),np.float64(annotation[1]),np.float64(annotation[2])]
    lwh = np.float64(annotation[3:6] * 1)
    wlh = lwh[[1, 0, 2]].tolist()
    axis_angles = np.array([0, 0, annotation[6] + 1e-10])
    ## TODO: CHECK
    rot = Rotation.from_euler('xyz', axis_angles, degrees=False)
    rot_quat = rot.as_quat(scalar_first=True).tolist()
    return center, wlh, rot_quat, label, score

def process_sample_annotations(dataset_path, dataset_version, sample_annotation, sample_token,visibility_token,attribute_token, threshold=0.4):
    sample_annotation_data = []
    instance_data = []
    for box_annotation in sample_annotation:
        center,lwh,rot,label,score = process_box_annotation(box_annotation)
        ##
        
        if score < threshold:
            continue
        category_token = get_category_token(dataset_path, dataset_version,LABEL_DICT[label])
        instance_token = create_token()
        sample_annotation_box_token = create_token()
        sample_annotation_box = {
                "token": sample_annotation_box_token,
                "sample_token": sample_token,
                "instance_token": instance_token,  # Generate a new instance token for each annotation
                "visibility_token": visibility_token,  # Assuming visibility info is available
                "attribute_tokens": [attribute_token],  # Assuming attributes are available
                "translation": center,
                "size": lwh,
                "rotation": rot,
                "num_lidar_pts": 10,
                "num_radar_pts": 10,
                "prev":"",
                "next": ""  # Update if there is a link to the next annotation
            }
        instance_box = {
            "token": instance_token,
            "category_token": category_token,
            "nbr_annotations": 1,
            "first_annotation_token": sample_annotation_box_token,
            "last_annotation_token": sample_annotation_box_token
        }

        sample_annotation_data.append(sample_annotation_box)
        instance_data.append(instance_box)
    return sample_annotation_data, instance_data

# def category_token(dataset_path,dataset_version, label):
#     label_name = LABEL_DICT[label]
#     category_token = get_category_token(dataset_path=dataset_path, dataset_version=dataset_version, category_name=label_name)
#     return category_token


# Function to create sample.json and sample_data.json and sample_annotation.json
def create_sample_files(dataset_path, dataset_version, annotations_path):
    
    scene_file_path = os.path.join(dataset_path, f'{dataset_version}/scene.json')
    pcd_folder_path = os.path.join(dataset_path, 'samples/LIDAR_TOP')
    sample_file_path = os.path.join(dataset_path, f'{dataset_version}/sample.json')
    sample_data_file_path = os.path.join(dataset_path, f'{dataset_version}/sample_data.json')
    sample_annotation_file_path = os.path.join(dataset_path, f'{dataset_version}/sample_annotation.json')
    instance_file_path = os.path.join(dataset_path, f'{dataset_version}/instance.json')
    lidar_name = "LIDAR_TOP"
    camera_name = "CAM_FRONT"
    lidar_sensor_token = get_sensor_token(dataset_path=dataset_path, dataset_version=dataset_version, channel=lidar_name)
    lidar_sensor_modality = get_sensor_modality(dataset_path=dataset_path,dataset_version=dataset_version, channel=lidar_name)
    lidar_calibrated_sensor_token= get_calibrated_sensor_token(dataset_path=dataset_path, dataset_version=dataset_version, sensor_token=lidar_sensor_token)

    camera_sensor_token = get_sensor_token(dataset_path=dataset_path, dataset_version=dataset_version, channel=camera_name)
    camera_sensor_modality = get_sensor_modality(dataset_path=dataset_path,dataset_version=dataset_version, channel=camera_name)
    camera_calibrated_sensor_token= get_calibrated_sensor_token(dataset_path=dataset_path, dataset_version=dataset_version, sensor_token=camera_sensor_token)
    # Check if the scene.json file exists
    if not os.path.exists(scene_file_path):
        print(f"File not found: {scene_file_path}")
        return

    # Check if the PCD folder exists
    if not os.path.exists(pcd_folder_path):
        print(f"Folder not found: {pcd_folder_path}")
        return

    # Read the scene.json file
    with open(scene_file_path, 'r') as f:
        scene_data = json.load(f)

    annotation_file = read_multiple_annotations(pickles_path=annotations_path)

    # List all PCD files in the folder
    pcd_files = sorted([f for f in os.listdir(pcd_folder_path) if f.endswith('.pcd.bin')])

    sample_data_entries = []
    sample_entries = []
    sample_annotation_entries = []
    instance_entries = []
    prev_sample_token = ""
    prev_sample_data_token = ""
    prev_sample_data_camera_token = ""
    
    number_pcds = len(pcd_files)
    half = int(number_pcds/2)
    for i, pcd_file in enumerate(pcd_files):
        ride,scene,file = pcd_file.split("+")
        sample_token = create_token()
        sample_data_token = create_token()
        sample_data_camera_token = create_token()
        scene_token = get_scene_token(scene, scene_data)
        # if i < half:
        #     scene_token = scene_data[0]['token'] 
        # else:
        #     scene_token = scene_data[1]['token'] 
        pcd_name = get_pointcloud_id(pcd_path=pcd_file)
        # Create sample_data entry
        sample_data_entry = {
            "token": sample_data_token,
            "sample_token": sample_token,
            "ego_pose_token": read_ego_pose_json(dataset_path, dataset_version)[0]["token"],  # Replace with actual ego pose token if available
            "calibrated_sensor_token": lidar_calibrated_sensor_token,  # Replace with actual calibrated sensor token
            "filename": f"samples/{lidar_name}/{pcd_file}",
            "fileformat": "PCD",
            "width": 0,
            "height": 0,
            #"timestamp": int(pcd_file.split("_")[0]+pcd_file.split("_")[1].split(".")[0]),  # Increment timestamp for simplicity
            "timestamp":i,
            "is_key_frame": True,
            "next": "",
            "prev": prev_sample_data_token,
            "sensor_modality": lidar_sensor_modality,
            "channel": lidar_name
        }

        sample_data_entries.append(sample_data_entry)

        ## Adding camera
        sample_data_camera_entry = {
            "token": sample_data_camera_token,
            "sample_token": sample_token,
            "ego_pose_token": read_ego_pose_json(dataset_path, dataset_version)[0]["token"],  # Replace with actual ego pose token if available
            "calibrated_sensor_token": camera_calibrated_sensor_token,  # Replace with actual calibrated sensor token
            "filename": f"samples/{camera_name}/traffic.jpg", ## TODO HARDCODED
            "fileformat": "JPG",
            "width": 1280,
            "height": 1024,
            "timestamp": int(pcd_file.split("_")[0]),  # Increment timestamp for simplicity
            "is_key_frame": True,
            "next": "",
            "prev": prev_sample_data_camera_token,
            "sensor_modality": camera_sensor_modality,
            "channel": camera_name
        }
        sample_data_entries.append(sample_data_camera_entry)

        # Create sample entry
        sample_entry = {
            "token": sample_token,
            "timestamp": sample_data_entry["timestamp"],
            "prev": prev_sample_token,
            "next": "",
            "scene_token": scene_token
        }

        sample_entries.append(sample_entry)

        sample_annotation_entry, instance_entry= process_sample_annotations(dataset_path,
                                                             dataset_version,
                                                             annotation_file[pcd_name]["gt_boxes"],
                                                             sample_token=sample_token,
                                                             visibility_token=read_visibility_json(dataset_path, dataset_version)[0]["token"],
                                                             attribute_token=read_attribute_json(dataset_path, dataset_version)[0]["token"],
                                                             threshold=0.4)
        sample_annotation_entries.extend(sample_annotation_entry)
        instance_entries.extend(instance_entry)
        if prev_sample_token!="":
            sample_entries[-2]["next"] = sample_token
            sample_data_entries[-2]["next"] = sample_data_token
        prev_sample_token = sample_token
        prev_sample_data_token = sample_data_token
        prev_sample_data_camera_token = sample_data_camera_token

    # Write sample_data.json
    with open(sample_data_file_path, 'w') as f:
        json.dump(sample_data_entries, f, indent=2)

    print(f"sample_data.json created successfully at {sample_data_file_path}")

    # Write sample.json
    with open(sample_file_path, 'w') as f:
        json.dump(sample_entries, f, indent=2)

    print(f"sample.json created successfully at {sample_file_path}")

    # Write sample_annotation.json
    with open(sample_annotation_file_path, 'w') as f:
        json.dump(sample_annotation_entries, f, indent=2)

    print(f"sample_annotation.json created successfully at {sample_annotation_file_path}")

    # Write instance.json
    with open(instance_file_path, 'w') as f:
        json.dump(instance_entries, f, indent=2)

    print(f"instance.json created successfully at {instance_file_path}")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="A simple script to read a command-line argument.")

    # Add an argument
    parser.add_argument('--dataset_path', type=str, help="The input argument to be processed")
    # Add an argument
    parser.add_argument('--dataset_version', type=str, help="The input argument to be processed")
    # Add an argument
    parser.add_argument('--annotations_path', type=str, help="Where the pkls are")

    # Parse the arguments
    args = parser.parse_args()

    
    # Write visibility data to visibility.json file
    dataset_path = args.dataset_path
    dataset_version = args.dataset_version
    annotations_path = args.annotations_path
    
    create_sample_files(dataset_path, dataset_version, annotations_path)

if __name__ == "__main__":
    main()
