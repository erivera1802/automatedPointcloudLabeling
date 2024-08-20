import json
import uuid
import os
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

def create_log(dataset_path, dataset_version,rides_pcd_path):
    # Example list of logs with their parameters (replace this with your actual data)
    rides = list_rides(rides_pcd_path)
    # Create log JSON structure
    log_data = []
    for log in rides:
        log_data.append({
            "token": create_token(),
            "logfile": log,
            "vehicle": "EDGAR",
            "date_captured": log[0:10],
            "location": log.split("_")[3]
        })

    # Write log data to log.json file
    with open(os.path.join(dataset_path, f'{dataset_version}/log.json'), 'w') as f:
        json.dump(log_data, f, indent=2)

    print(f"log.json created successfully at {os.path.join(dataset_path, f'{dataset_version}/log.json')}")

if __name__ == "__main__":
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

    
    # Write visibility data to visibility.json file
    dataset_path = args.dataset_path
    dataset_version = args.dataset_version
    rides_pcd_path = args.rides_pcd_path
    
    create_log(dataset_path, dataset_version, rides_pcd_path)
