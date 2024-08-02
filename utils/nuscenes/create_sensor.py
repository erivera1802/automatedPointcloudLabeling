import json
import uuid
import os

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

# List of sensors with their channels and modalities
sensors = [
    {"channel": "LIDAR_TOP", "modality": "lidar"},
    {"channel": "CAM_FRONT", "modality": "camera"}
]

# Create sensor JSON structure
sensor_data = []
for sensor in sensors:
    sensor_data.append({
        "token": create_token(),
        "channel": sensor["channel"],
        "modality": sensor["modality"]
    })

# Write sensor data to sensor.json file
dataset_root = '../muenchen'
with open(os.path.join(dataset_root, 'v1.0-mini/sensor.json'), 'w') as f:
    json.dump(sensor_data, f, indent=2)

print(f"sensor.json created successfully at {os.path.join(dataset_root, 'v1.0-mini/sensor.json')}")
