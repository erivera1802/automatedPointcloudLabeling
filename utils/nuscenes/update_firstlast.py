import json
import os
import argparse

# Function to read and print scene.json
def read_scene_json(dataset_path, dataset_version):
    scene_file_path = os.path.join(dataset_path, f'{dataset_version}/scene.json')
    
    # Check if the file exists
    if not os.path.exists(scene_file_path):
        print(f"File not found: {scene_file_path}")
        return
    
    # Read the JSON file
    with open(scene_file_path, 'r') as f:
        scene_data = json.load(f)
    return scene_data

# Function to read and print sample.json
def read_sample_json(dataset_path, dataset_version):
    sample_file_path = os.path.join(dataset_path, f'{dataset_version}/sample.json')
    
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

def update_scenes(dataset_path, dataset_version):
    # Read and print sample.json
    scenes = read_scene_json(dataset_path, dataset_version)
    samples = read_sample_json(dataset_path, dataset_version)
    scenes = update_scene(scenes, samples)

    scene_file_path = os.path.join(dataset_path, f'{dataset_version}/scene.json')

     # Write scene data to scene.json file
    with open(scene_file_path, 'w') as f:
        json.dump(scenes, f, indent=2)

    print(f"scene.json updated successfully at {scene_file_path}")
def main():
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

    update_scenes(dataset_path, dataset_version)
    # Replace 'path_to_dataset_root' with the actual path to your dataset root directory
    
    
    

if __name__ == "__main__":
    main()