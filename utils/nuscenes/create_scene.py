import json
import os
import uuid
import argparse


# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

def list_rides(rides_path):
    # List to store filenames without extension
    filenames_without_extension = []
    
    # Loop through all files in the directory
    for filename in os.listdir(rides_path):
        # Split the filename into name and extension
        name, extension = os.path.splitext(filename)
        
        # Append the name without extension to the list
        filenames_without_extension.append(name)
        filenames_without_extension.sort()

    return filenames_without_extension

def get_logtoken_by_logfile(logfile_name, json_data):
    # Loop through each log entry in the JSON data
    for entry in json_data:
        # Check if the logfile matches the input parameter
        if entry.get("logfile") == logfile_name:
            # Return the corresponding token
            return entry.get("token")
    
    # If no match is found, return None or an appropriate message
    return None


# Function to read log.json and create scene.json
def create_scene(dataset_path, dataset_version, rides_pcd_path):
    log_file_path = os.path.join(dataset_path, f'{dataset_version}/log.json')
    scene_file_path = os.path.join(dataset_path, f'{dataset_version}/scene.json')

    # Check if the log.json file exists
    if not os.path.exists(log_file_path):
        print(f"File not found: {log_file_path}")
        return

    # Read the log.json file
    with open(log_file_path, 'r') as f:
        log_data = json.load(f)
    rides = list_rides(rides_pcd_path)

    scene_data = []
    scene_index = 0
    # Example scene data (replace this with your actual data)
    for ride in rides:
        logtoken = get_logtoken_by_logfile(ride,log_data)
        for scene in os.listdir(os.path.join(rides_pcd_path,ride)):
    # Create scene JSON structure
            scene_data.append({
                "token": create_token(),
                "name": f"scene-{scene_index:04}",
                "description": scene,
                "log_token": logtoken,
                "nbr_samples": 5,
                "first_sample_token": create_token(),
                "last_sample_token": create_token(),
                "timestamp": scene_index
            })
            scene_index=scene_index+1
    # Write scene data to scene.json file
    with open(scene_file_path, 'w') as f:
        json.dump(scene_data, f, indent=2)

    print(f"scene.json created successfully at {scene_file_path}")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="A simple script to read a command-line argument.")

    # Add an argument
    parser.add_argument('--dataset_path', type=str, help="The input argument to be processed")
    # Add an argument
    parser.add_argument('--dataset_version', type=str, help="The input argument to be processed")
        # Add an argument
    parser.add_argument('--rides_pcd_path', type=str, help="Where the rides with the pcds are located")


    # Parse the arguments
    args = parser.parse_args()

    
    dataset_path = args.dataset_path
    dataset_version = args.dataset_version
    rides_pcd_path = args.rides_pcd_path
    
    create_scene(dataset_path, dataset_version, rides_pcd_path)

if __name__ == "__main__":
    main()
