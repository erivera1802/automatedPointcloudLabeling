import os
import shutil

source_directory = '/home/ubuntu/perception_datasets/_Temp/Rivera/GorkemBegum/data_ms3d/kitti/training/calib'

# Get the list of files in the source directory
file_list = os.listdir(source_directory)

# Iterate through the files and delete them
for file_name in file_list:
    file_path = os.path.join(source_directory, file_name)
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

print("Directory cleaned.")


# Source and destination directories
source_directory = "/home/ubuntu/BegumGorkem/OpenPCDet/data/kitti/training/calib"
destination_directory = "/home/ubuntu/perception_datasets/_Temp/Rivera/GorkemBegum/data_ms3d/kitti/training/calib"

# Iterate through each file in the source directory
for filename in sorted(os.listdir(source_directory))[:200]:
    source_path = os.path.join(source_directory, filename)

    # Check if the path is a file and not a directory
    if os.path.isfile(source_path):
        # Extract the sequence number from the filename (assuming it's a number)
        #sequence_number = int(''.join(filter(str.isdigit, filename)))

        # Create the destination directory if it doesn't exist
        #destination_sequence_directory = os.path.join(destination_directory,sequence_number)
        #os.makedirs(destination_sequence_directory, exist_ok=True)

        # Create the lidar directory inside the sequence directory
        #lidar_directory = os.path.join(destination_sequence_directory, "lidar")
        #os.makedirs(lidar_directory, exist_ok=True)

        # Copy the file to the lidar directory
        shutil.copyfile(source_path, os.path.join(destination_directory, filename))

print("Files copied successfully.")
