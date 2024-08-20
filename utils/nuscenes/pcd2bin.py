import os
import numpy as np
import open3d as o3d
import argparse

# Function to convert PCD to BIN
def convert_pcd_to_bin(pcd_file_path, bin_file_path):
    # Load the PCD file
    cloud = o3d.io.read_point_cloud(pcd_file_path)

    # Extract the points from the PCD file
    points = np.asarray(cloud.points, dtype=np.float32)
    # Check the shape of the array
    num_rows = points.shape[0]
    
    # Create a column of zeros
    zeros_column = np.zeros((num_rows, 1), dtype=points.dtype)
    
    # Concatenate the original array with the zeros column
    points = np.hstack((points, zeros_column, zeros_column))
    # Save the points to a BIN file
    points.tofile(bin_file_path)

    print(f"Converted {pcd_file_path} to {bin_file_path}")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="A simple script to read a command-line argument.")

    # Add an argument
    parser.add_argument('--dataset_path', type=str, help="The input argument to be processed")
    # Add an argument
    parser.add_argument('--dataset_version', type=str, help="The input argument to be processed")
    # Add an argument
    parser.add_argument('--rides_pcd_path', type=str, help="The input argument to be processed")


    # Parse the arguments
    args = parser.parse_args()

    
    # Write visibility data to visibility.json file
    dataset_path = args.dataset_path
    rides_pcd_path = args.rides_pcd_path
    # Replace these with your actual file paths
    output_dir = os.path.join(dataset_path, "samples/LIDAR_TOP")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert all PCD files in the directory to BIN files

    for ride in os.listdir(rides_pcd_path):
        scenes_list = os.path.join(rides_pcd_path, ride)
        for scene in os.listdir(scenes_list):
            pcds_path = os.path.join(rides_pcd_path, ride, scene,"pcd")
            for filename in os.listdir(pcds_path):
                if filename.endswith('.pcd'):
                    pcd_file_path = os.path.join(pcds_path, filename)
                    new_filename = f"{ride}+{scene}+{filename.split('.')[0]}.pcd.bin"
                    bin_file_path = os.path.join(output_dir, new_filename)
                    convert_pcd_to_bin(pcd_file_path, bin_file_path)

if __name__ == "__main__":
    main()