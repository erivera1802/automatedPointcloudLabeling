import json
import uuid
import os
import argparse

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

def create_attribute(dataset_path, dataset_version):

    # List of attributes with their descriptions
    attributes = [
        {"name": "vehicle.moving", "description": "The vehicle is moving."},
        {"name": "vehicle.parked", "description": "The vehicle is parked."},
        {"name": "vehicle.stopped", "description": "The vehicle is stopped."},
        {"name": "pedestrian.moving", "description": "The pedestrian is moving."},
        {"name": "pedestrian.standing", "description": "The pedestrian is standing."},
        {"name": "pedestrian.sitting_lying_down", "description": "The pedestrian is sitting or lying down."},
        {"name": "cycle.with_rider", "description": "The bicycle or motorcycle has a rider."},
        {"name": "cycle.without_rider", "description": "The bicycle or motorcycle does not have a rider."}
    ]

     # Create attribute JSON structure
    attribute_data = []
    for attribute in attributes:
        attribute_data.append({
            "token": create_token(),
            "name": attribute["name"],
            "description": attribute["description"]
        })

    with open(os.path.join(dataset_path, f'{dataset_version}/attribute.json'), 'w') as f:
        json.dump(attribute_data, f, indent=2)

    print(f"attribute.json created successfully at {os.path.join(dataset_path, f'{dataset_version}/attribute.json')}")


if __name__ =="__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="A simple script to read a command-line argument.")

    # Add an argument
    parser.add_argument('--dataset_path', type=str, help="The input argument to be processed")
    # Add an argument
    parser.add_argument('--dataset_version', type=str, help="The input argument to be processed")

    # Parse the arguments
    args = parser.parse_args()

   
    # Write attribute data to attribute.json file
    dataset_path = args.dataset_path
    dataset_version = args.dataset_version
    
    create_attribute(dataset_path, dataset_version)