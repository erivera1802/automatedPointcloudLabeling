import json
import os
import uuid

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

# Function to read log.json and create scene.json
def create_scene_json(dataset_root):
    log_file_path = os.path.join(dataset_root, 'v1.0-mini/log.json')
    scene_file_path = os.path.join(dataset_root, 'v1.0-mini/scene.json')

    # Check if the log.json file exists
    if not os.path.exists(log_file_path):
        print(f"File not found: {log_file_path}")
        return

    # Read the log.json file
    with open(log_file_path, 'r') as f:
        log_data = json.load(f)

    # Example scene data (replace this with your actual data)
    scenes = [
        {
            "name": "scene-0001",
            "description": "First example scene.",
            "nbr_samples": 5,
            "first_sample_token": create_token(),  # Replace with actual first sample token
            "last_sample_token": create_token(),  # Replace with actual last sample token
            "timestamp": 1532402928000000  # Replace with actual timestamp
        }
    ]

    # Create scene JSON structure
    scene_data = []
    for i, scene in enumerate(scenes):
        scene_data.append({
            "token": create_token(),
            "name": scene["name"],
            "description": scene["description"],
            "log_token": log_data[i]["token"],  # Assuming log_data index matches scenes index
            "nbr_samples": scene["nbr_samples"],
            "first_sample_token": scene["first_sample_token"],
            "last_sample_token": scene["last_sample_token"],
            "timestamp": scene["timestamp"]
        })

    # Write scene data to scene.json file
    with open(scene_file_path, 'w') as f:
        json.dump(scene_data, f, indent=2)

    print(f"scene.json created successfully at {scene_file_path}")

def main():
    # Replace 'path_to_dataset_root' with the actual path to your dataset root directory
    dataset_root = '../muenchen'
    create_scene_json(dataset_root)

if __name__ == "__main__":
    main()
