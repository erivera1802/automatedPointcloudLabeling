import json
import uuid
import os

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

def get_first_log_token(dataset_root):
    log_file_path = os.path.join(dataset_root, 'v1.0-mini/log.json')
    
    # Check if the file exists
    if not os.path.exists(log_file_path):
        print(f"File not found: {log_file_path}")
        return None
    
    # Read the JSON file
    with open(log_file_path, 'r') as f:
        log_data = json.load(f)
    
    # Return the token of the first log entry if it exists
    if log_data:
        return log_data[0]['token']
    
    print("No log entries found")
    return None

# Example list of maps with their parameters (replace this with your actual data)
maps = [
    {
        "filename": "maps/muenchen.png",  # Replace with actual map file name
        "log_token": create_token(),  # Replace with actual log token
        "category": "drivable_area"  # Replace with actual category
    }
]

dataset_root = '../muenchen'
# Create map JSON structure
map_data = []
for map_entry in maps:
    map_data.append({
        "token": create_token(),
        "filename": map_entry["filename"],
        "log_tokens": [get_first_log_token(dataset_root)],
        "category": map_entry["category"]
    })

# Write map data to map.json file

with open(os.path.join(dataset_root, 'v1.0-mini/map.json'), 'w') as f:
    json.dump(map_data, f, indent=2)

print(f"map.json created successfully at {os.path.join(dataset_root, 'v1.0-mini/map.json')}")
