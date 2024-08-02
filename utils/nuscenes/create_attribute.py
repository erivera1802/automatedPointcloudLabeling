import json
import uuid
import os

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

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

if __name__ =="__main__":
    # Create attribute JSON structure
    attribute_data = []
    for attribute in attributes:
        attribute_data.append({
            "token": create_token(),
            "name": attribute["name"],
            "description": attribute["description"]
        })

    # Write attribute data to attribute.json file
    dataset_root = '../muenchen'
    with open(os.path.join(dataset_root, 'v1.0-mini/attribute.json'), 'w') as f:
        json.dump(attribute_data, f, indent=2)

    print(f"attribute.json created successfully at {os.path.join(dataset_root, 'v1.0-mini/attribute.json')}")
