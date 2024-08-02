import json
import uuid
import os

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

# Example list of ego poses with their parameters (replace this with your actual data)
ego_poses = [
    {
        "timestamp": 1532402928000000,  # Replace with actual timestamp in microseconds
        "translation": [0.0, 0.0, 0.0],  # Replace with actual translation values
        "rotation": [0.0, 0.0, 0.0, 1.0]  # Replace with actual rotation values (quaternion)
    }
]

# Create ego_pose JSON structure
ego_pose_data = []
for ego_pose in ego_poses:
    ego_pose_data.append({
        "token": create_token(),
        "timestamp": ego_pose["timestamp"],
        "translation": ego_pose["translation"],
        "rotation": ego_pose["rotation"]
    })

# Write ego pose data to ego_pose.json file
dataset_root = '../muenchen'
with open(os.path.join(dataset_root, 'v1.0-mini/ego_pose.json'), 'w') as f:
    json.dump(ego_pose_data, f, indent=2)

print(f"ego_pose.json created successfully at {os.path.join(dataset_root, 'v1.0-mini/ego_pose.json')}")
