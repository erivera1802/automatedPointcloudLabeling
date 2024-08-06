import json
import uuid
import os
import argparse

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())
def create_categories(dataset_path, dataset_version):

    # List of categories with their descriptions
    categories = [
        {"name": "vehicle.car", "description": "A regular car."},
        {"name": "human.pedestrian.adult", "description": "Pedestrian"},
        {"name": "vehicle.bicycle", "description": "cyclist"},
    ]

    # Create category JSON structure
    category_data = []
    for category in categories:
        category_data.append({
            "token": create_token(),
            "name": category["name"],
            "description": category["description"]
        })

    with open(os.path.join(dataset_path, f'{dataset_version}/category.json'), 'w') as f:
        json.dump(category_data, f, indent=2)

    print(f"category.json created successfully at {os.path.join(dataset_path, f'{dataset_version}/category.json')}")

# Write category data to category.json file
if __name__ == "__main__":
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
    create_categories(dataset_path, dataset_version)
