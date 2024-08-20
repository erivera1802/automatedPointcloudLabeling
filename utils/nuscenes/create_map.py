import json
import uuid
import os
import argparse

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

def get_log_tokens(dataset_path, dataset_version):
    log_file_path = os.path.join(dataset_path, f'{dataset_version}/log.json')
    
    # Check if the file exists
    if not os.path.exists(log_file_path):
        print(f"File not found: {log_file_path}")
        return None
    
    # Read the JSON file
    with open(log_file_path, 'r') as f:
        log_data = json.load(f)
    
    # Return the token of the first log entry if it exists
    log_tokens = []
    if log_data:
        for entry in log_data:
            log_tokens.append(entry['token'])
        return log_tokens
    
    print("No log entries found")
    return None

def create_map(dataset_path, dataset_version):
    # Example list of maps with their parameters (replace this with your actual data)
    maps = [
        {
            "filename": "maps/muenchen.png",  # Replace with actual map file name
            "log_token": create_token(),  # Replace with actual log token
            "category": "drivable_area"  # Replace with actual category
        }
    ]

    # Create map JSON structure
    map_data = []
    for map_entry in maps:
        map_data.append({
            "token": create_token(),
            "filename": map_entry["filename"],
            "log_tokens": get_log_tokens(dataset_path, dataset_version),
            "category": map_entry["category"]
        })

    # Write map data to map.json file

    with open(os.path.join(dataset_path, f'{dataset_version}/map.json'), 'w') as f:
        json.dump(map_data, f, indent=2)

    print(f"map.json created successfully at {os.path.join(dataset_path, f'{dataset_version}/map.json')}")

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
    
    create_map(dataset_path, dataset_version)
