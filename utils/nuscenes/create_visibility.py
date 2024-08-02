import json
import uuid
import os

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

# List of visibility levels with their descriptions
visibility_levels = [
    {"level": "1", "description": "Visibility is good."},
    {"level": "2", "description": "Visibility is reduced due to light or weather conditions."},
    {"level": "3", "description": "Visibility is poor."},
    {"level": "4", "description": "Visibility is very poor."}
]

if __name__ == "__main__":
    # Create visibility JSON structure
    visibility_data = []
    for visibility in visibility_levels:
        visibility_data.append({
            "token": create_token(),
            "level": visibility["level"],
            "description": visibility["description"]
        })

    # Write visibility data to visibility.json file
    dataset_root = '../muenchen'
    with open(os.path.join(dataset_root, 'v1.0-mini/visibility.json'), 'w') as f:
        json.dump(visibility_data, f, indent=2)

    print(f"visibility.json created successfully at {os.path.join(dataset_root, 'v1.0-mini/visibility.json')}")
