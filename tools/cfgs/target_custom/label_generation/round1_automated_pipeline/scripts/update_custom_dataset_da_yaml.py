import yaml
import argparse

def parse_config():
    parser = argparse.ArgumentParser(description='arg parser')
    parser.add_argument('--mcap_path', type=str)

    args = parser.parse_args()

    return args

target_cfg = parse_config()

# Define the file path
file_path = '/MS3D/tools/cfgs/dataset_configs/custom_dataset_da.yaml'

# Load the YAML file
with open(file_path, 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

data['DATA_PATH'] = target_cfg.mcap_path

# Write the updated data back to the YAML file
with open(file_path, 'w') as file:
    yaml.dump(data, file, default_flow_style=False, sort_keys=False)

print("custom_dataset_da YAML file updated successfully.")
