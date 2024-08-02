import json
import uuid
import os

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

def get_category_token(dataset_root, category_name):
    category_file_path = os.path.join(dataset_root, 'v1.0-mini/category.json')
    
    # Check if the file exists
    if not os.path.exists(category_file_path):
        print(f"File not found: {category_file_path}")
        return None
    
    # Read the JSON file
    with open(category_file_path, 'r') as f:
        category_data = json.load(f)
    
    # Find and return the token of the entry with the matching category name
    for entry in category_data:
        if entry['name'] == category_name:
            return entry['token']
    
    print(f"No entry found with category name: {category_name}")
    return None

# Function to find first and last annotation tokens for an instance
def find_annotation_tokens(instance_token):
    tokens = [create_token() for ann in annotations if ann["instance_token"] == instance_token]
    if tokens:
        return tokens[0], tokens[-1]
    else:
        return "", ""
# Example data (replace this with your actual data)
instances = [
    {"category_name": "vehicle.car", "nbr_annotations": 5},
    {"category_name": "vehicle.bicycle", "nbr_annotations": 3},
    {"category_name": "human.pedestrian.adult", "nbr_annotations": 4},
]

# Example annotations (replace this with your actual data)
annotations = [
    {"instance_token": "instance_token_1"},
    {"instance_token": "instance_token_1"},
    {"instance_token": "instance_token_2"},
    {"instance_token": "instance_token_3"},
    {"instance_token": "instance_token_3"}
]


dataset_root = '../muenchen'

# Create instance JSON structure
instance_data = []
for instance in instances:
    instance_token = create_token()
    first_annotation_token, last_annotation_token = find_annotation_tokens(instance_token)
    instance_data.append({
        "token": instance_token,
        "category_token": get_category_token(dataset_root=dataset_root, category_name=instance["category_name"]),
        "nbr_annotations": instance["nbr_annotations"],
        "first_annotation_token": first_annotation_token,
        "last_annotation_token": last_annotation_token
    })

# Write instance data to instance.json file

with open(os.path.join(dataset_root, 'v1.0-mini/instance.json'), 'w') as f:
    json.dump(instance_data, f, indent=2)

print(f"instance.json created successfully at {os.path.join(dataset_root, 'v1.0-mini/instance.json')}")
