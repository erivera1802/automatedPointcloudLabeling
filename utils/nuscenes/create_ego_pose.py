import json
import uuid
import os
import argparse

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

# Example list of ego poses with their parameters (replace this with your actual data)

def create_ego_pose(dataset_path, dataset_version):
    ego_poses = [
        {
            "timestamp": 1532402928000000,  # Replace with actual timestamp in microseconds
            "translation": [0.0, 0.0, 0.0],  # Replace with actual translation values
            "rotation": [1.0, 0.0, 0.0, 0.0]  # Replace with actual rotation values (quaternion)
        }
    ]

    # Create ego_pose JSON structure
    ego_pose_data = []
    for ego_pose in ego_poses:
        ego_pose_data.append({
            "token": create_token(),
            "timestamp": ego_pose["timestamp"],
            "translation": ego_pose["translation"],
            "rotation": ego_pose["rotation"]
        })

    # Write ego pose data to ego_pose.json file
    with open(os.path.join(dataset_path, f'{dataset_version}/ego_pose.json'), 'w') as f:
        json.dump(ego_pose_data, f, indent=2)

    print(f"ego_pose.json created successfully at {os.path.join(dataset_path, f'{dataset_version}/ego_pose.json')}")


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="A simple script to read a command-line argument.")

    # Add an argument
    parser.add_argument('--dataset_path', type=str, help="The input argument to be processed")
    # Add an argument
    parser.add_argument('--dataset_version', type=str, help="The input argument to be processed")

    # Parse the arguments
    args = parser.parse_args()

    
    # Write visibility data to visibility.json file
    dataset_path = args.dataset_path
    dataset_version = args.dataset_version
    
    create_ego_pose(dataset_path, dataset_version)
