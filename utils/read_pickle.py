import pickle

# # pickle_file_path = '/home/ubuntu/BegumGorkem/MS3D/output/model_zoo/lyft_pretrained/cfgs/lyft_uda_voxel_rcnn_anchorhead_3xyzt_allcls/default/eval/epoch_3/val/lyft3xyzt_custom2xyzt_rwf_rwr/result.pkl'
# pickle_file_path = '/home/ubuntu/perception_datasets/_Temp/Rivera/GorkemBegum/data_ms3d/output/model_zoo/lyft_pretrained/cfgs/lyft_uda_pv_rcnn_plusplus_resnet_anchorhead_1xyz_allcls/default/eval/epoch_1/val/lyft1xyz_waymo1xyz_custom190_notta/result.pkl'

# # pickle_file_path2 = '/home/ubuntu/BegumGorkem/MS3D/tools/cfgs/target_kitti/label_generation/round1/ps_labels/initial_pseudo_labels.pkl'
# pickle_file_path2 = '/home/ubuntu/perception_datasets/_Temp/Rivera/GorkemBegum/data_ms3d/waymo/waymo_processed_data_v0_5_0_infos_train.pkl'
# # waymo_processed_data_v0_5_0

#p_f_3 = "/home/ubuntu/BegumGorkem/MS3D/tools/cfgs/target_waymo/label_generation/round1/ps_labels/initial_pseudo_labels.pkl"
p_f_3 =   "/MS3D/output/MS3D/tools/cfgs/argo2_models/converted.pkl"

# p_f_3 = '/home/ubuntu/BegumGorkem/MS3D/output/model_zoo/lyft_pretrained/cfgs/lyft_uda_voxel_rcnn_centerhead_3xyzt_allcls/default/eval/epoch_3/val/lyft3xyzt_custom4xyzt_rwf_rwr/result.pkl'

# with open(pickle_file_path, 'rb') as file:
#     # Load the first object
#     object1 = pickle.load(file)
    
# with open(pickle_file_path2, 'rb') as file:
#     # Load the first object
#     object2 = pickle.load(file)

with open(p_f_3, 'rb') as file:
    # Load the first object
    object3 = pickle.load(file)
    

print('ok')


# import open3d as o3d

# # Load PCD file
# pcd_path = "/home/ubuntu/BegumGorkem/MS3D/data/custom_data/kitti/sequences/sequence_0/lidar/000000.pcd"
# pcd = o3d.io.read_point_cloud(pcd_path)

# # Print basic information about the point cloud
# print(pcd)

# # Visualize the point cloud
# # o3d.visualization.draw_geometries([pcd])



# # Example: Reading a binary file
# file_path = '/home/ubuntu/perception_datasets/_Temp/Rivera/GorkemBegum/data_ms3d/kitti/sequences/sequence_0/lidar/000000.bin'

# with open(file_path, 'rb') as file:
#     # Read the entire content of the file
#     binary_data = file.read()
#     print("x")
