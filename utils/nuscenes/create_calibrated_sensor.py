import json
import os
import uuid

# Function to create a unique token
def create_token():
    return str(uuid.uuid4())

# Function to read sensor.json and create calibrated_sensor.json
def create_calibrated_sensor_json(dataset_root):
    sensor_file_path = os.path.join(dataset_root, 'v1.0-mini/sensor.json')
    calibrated_sensor_file_path = os.path.join(dataset_root, 'v1.0-mini/calibrated_sensor.json')

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
    # Replace 'path_to_dataset_root' with the actual path to your dataset root directory
    dataset_root = '../muenchen'
    create_calibrated_sensor_json(dataset_root)

if __name__ == "__main__":
    main()
