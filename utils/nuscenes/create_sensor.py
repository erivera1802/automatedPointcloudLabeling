import json
import uuid
import os
import argparse

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

def create_sensors(dataset_path, dataset_version):
    # List of sensors with their channels and modalities
    sensors = [
        {"channel": "LIDAR_TOP", "modality": "lidar"},
        {"channel": "CAM_FRONT", "modality": "camera"}
    ]

    # Create sensor JSON structure
    sensor_data = []
    for sensor in sensors:
        sensor_data.append({
            "token": create_token(),
            "channel": sensor["channel"],
            "modality": sensor["modality"]
        })

    # Write sensor data to sensor.json file
    with open(os.path.join(dataset_path, f'{dataset_version}/sensor.json'), 'w') as f:
        json.dump(sensor_data, f, indent=2)

    print(f"sensor.json created successfully at {os.path.join(dataset_path, f'{dataset_version}/sensor.json')}")

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
    
    create_sensors(dataset_path, dataset_version)