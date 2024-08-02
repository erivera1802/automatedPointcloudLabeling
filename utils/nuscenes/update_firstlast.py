import json
import os

# Function to read and print scene.json
def read_scene_json(dataset_root):
    scene_file_path = os.path.join(dataset_root, 'v1.0-mini/scene.json')
    
    # Check if the file exists
    if not os.path.exists(scene_file_path):
        print(f"File not found: {scene_file_path}")
        return
    
    # Read the JSON file
    with open(scene_file_path, 'r') as f:
        scene_data = json.load(f)
    return scene_data

# Function to read and print sample.json
def read_sample_json(dataset_root):
    sample_file_path = os.path.join(dataset_root, 'v1.0-mini/sample.json')
    
    # Check if the file exists
    if not os.path.exists(sample_file_path):
        print(f"File not found: {sample_file_path}")
        return
    
    # Read the JSON file
    with open(sample_file_path, 'r') as f:
        sample_data = json.load(f)
    return sample_data

def update_scene(scenes, samples):
    scenes[0]["first_sample_token"]=samples[0]["token"]
    scenes[0]["last_sample_token"]=samples[-1]["token"]
    
    return scenes
def main():
    # Replace 'path_to_dataset_root' with the actual path to your dataset root directory
    dataset_root = '../muenchen'
    
    # Read and print sample.json
    scenes = read_scene_json(dataset_root)
    samples = read_sample_json(dataset_root)
    scenes = update_scene(scenes, samples)

    scene_file_path = os.path.join(dataset_root, 'v1.0-mini/scene.json')

     # Write scene data to scene.json file
    with open(scene_file_path, 'w') as f:
        json.dump(scenes, f, indent=2)

    print(f"scene.json updated successfully at {scene_file_path}")
    

if __name__ == "__main__":
    main()