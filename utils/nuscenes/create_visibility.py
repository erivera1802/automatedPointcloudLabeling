import json
import uuid
import os
import argparse

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())
def create_visibility(dataset_path, dataset_version):

    # List of visibility levels with their descriptions
    visibility_levels = [
        {"level": "1", "description": "Visibility is good."},
        {"level": "2", "description": "Visibility is reduced due to light or weather conditions."},
        {"level": "3", "description": "Visibility is poor."},
        {"level": "4", "description": "Visibility is very poor."}
    ]

    # Create visibility JSON structure
    visibility_data = []
    for visibility in visibility_levels:
        visibility_data.append({
            "token": create_token(),
            "level": visibility["level"],
            "description": visibility["description"]
        })
    with open(os.path.join(dataset_path, f'{dataset_version}/visibility.json'), 'w') as f:
        json.dump(visibility_data, f, indent=2)
    
    print(f"visibility.json created successfully at {os.path.join(dataset_path, f'{dataset_version}/visibility.json')}")


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
    
    create_visibility(dataset_path, dataset_version)
