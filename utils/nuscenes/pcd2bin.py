import os
import numpy as np
import open3d as o3d

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
    # Replace these with your actual file paths
    dataset_root = '../muenchen/samples/LIDAR_TOP_bkp'
    output_dir = '../muenchen/samples/LIDAR_TOP'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert all PCD files in the directory to BIN files
    for filename in os.listdir(dataset_root):
        if filename.endswith('.pcd'):
            pcd_file_path = os.path.join(dataset_root, filename)
            bin_file_path = os.path.join(output_dir, filename.replace('.pcd', '.pcd.bin'))
            convert_pcd_to_bin(pcd_file_path, bin_file_path)

if __name__ == "__main__":
    main()