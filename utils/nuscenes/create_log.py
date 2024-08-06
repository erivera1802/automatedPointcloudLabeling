import json
import uuid
import os
import argparse


# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

def create_log(dataset_path, dataset_version):
    # Example list of logs with their parameters (replace this with your actual data)
    logs = [
        {
            "logfile": "logs/log1",
            "vehicle": "EDGAR",
            "date_captured": "2023-07-30",
            "location": "muenchen"
        }
    ]

    # Create log JSON structure
    log_data = []
    for log in logs:
        log_data.append({
            "token": create_token(),
            "logfile": os.path.join("..", "muenchen", log["logfile"]),
            "vehicle": log["vehicle"],
            "date_captured": log["date_captured"],
            "location": log["location"]
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

    # Parse the arguments
    args = parser.parse_args()

    
    # Write visibility data to visibility.json file
    dataset_path = args.dataset_path
    dataset_version = args.dataset_version
    
    create_log(dataset_path, dataset_version)
