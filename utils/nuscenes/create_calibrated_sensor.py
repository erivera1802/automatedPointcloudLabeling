import json
import os
import uuid
import argparse

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

# Function to read sensor.json and create calibrated_sensor.json
def create_calibrated_sensor(dataset_path, dataset_version):
    sensor_file_path = os.path.join(dataset_path, f'{dataset_version}/sensor.json')
    calibrated_sensor_file_path = os.path.join(dataset_path, f'{dataset_version}/calibrated_sensor.json')

    # Check if the sensor.json file exists
    if not os.path.exists(sensor_file_path):
        print(f"File not found: {sensor_file_path}")
        return

    # Read the sensor.json file
    with open(sensor_file_path, 'r') as f:
        sensor_data = json.load(f)

    # Example calibration data (replace this with your actual data)
    calibration_data = {
        "LIDAR_TOP": {
            "translation": [0.0, 0.0, 0.0],
            "rotation": [0.0, 0.0, 0.0, 1.0],
            "camera_intrinsic": []
        },
        "CAM_FRONT": {
            "translation": [1.0, 0.0, 1.5],
            "rotation": [0.0, 0.0, 0.0, 1.0],
            "camera_intrinsic": [
                [1266.417203046554, 0.0, 816.2670197447984],
                [0.0, 1266.417203046554, 491.5070657929476],
                [0.0, 0.0, 1.0]
            ]
        },
        # Add calibration data for other sensors as needed
    }

    # Create calibrated_sensor JSON structure
    calibrated_sensor_data = []
    for sensor in sensor_data:
        channel = sensor["channel"]
        if channel in calibration_data:
            calibrated_sensor_data.append({
                "token": create_token(),
                "sensor_token": sensor["token"],
                "translation": calibration_data[channel]["translation"],
                "rotation": calibration_data[channel]["rotation"],
                "camera_intrinsic": calibration_data[channel]["camera_intrinsic"]
            })
        else:
            print(f"No calibration data found for sensor channel: {channel}")

    # Write calibrated sensor data to calibrated_sensor.json file
    with open(calibrated_sensor_file_path, 'w') as f:
        json.dump(calibrated_sensor_data, f, indent=2)

    print(f"calibrated_sensor.json created successfully at {calibrated_sensor_file_path}")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="A simple script to read a command-line argument.")

    # Add an argument
    parser.add_argument('--dataset_path', type=str, help="The input argument to be processed")
    # Add an argument
    parser.add_argument('--dataset_version', type=str, help="The input argument to be processed")

    # Parse the arguments
    args = parser.parse_args()

    
    # Write visibility data to visibility.json file
    dataset_path = args.dataset_path
    dataset_version = args.dataset_version
    
    create_calibrated_sensor(dataset_path, dataset_version)

if __name__ == "__main__":
    main()
