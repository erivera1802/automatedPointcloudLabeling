import json
import uuid
import os

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

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

# Write category data to category.json file
if __name__ == "__main__":
    dataset_root = '../muenchen'
    with open(os.path.join(dataset_root, 'v1.0-mini/category.json'), 'w') as f:
        json.dump(category_data, f, indent=2)

    print(f"category.json created successfully at {os.path.join(dataset_root, 'v1.0-mini/category.json')}")
