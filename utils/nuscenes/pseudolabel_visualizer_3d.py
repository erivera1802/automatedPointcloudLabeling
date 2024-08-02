import open3d as o3d
import numpy as np
import pandas as pd
import argparse

def visualize_3d(pcd_path,pickle_path,score_threshold):
    """Function to 3d visualize predicted boxes of a pcd file using the frame_id and score threshold.
    Used for MS3D data format(.pcd) and predictions(pickle)

    Args:
        pcd_path (string): Path to the .pcd file (pointcloud data) (e.g 1718127846_799991808.pcd)
        prediction_pickle_path (string): path to prediction pickle file. 
        This pickle file must be in MS3D generated format (consists of the rosbag predictions with all frame_ids)
        confidence_threshold (float): To visualize objects which are above a certain threshold.
    """    

    pcd = o3d.io.read_point_cloud(pcd_path)

    result = pd.read_pickle(pickle_path) 
    
    file_name = pcd_path.split('/')[-1]
    if '_' in file_name:
            file_name = file_name.replace('_','')
    frame_id = file_name.split('.pcd')[0]

    result_item = result[frame_id]["gt_boxes"] # pseudo pickle 
    print(result_item) 


    # 0,1,2 = x, y, z 
    # 3,4,5 = l, w, h
    # 6 = rotation_angle
    # 7 = class
    # 8 = score

    CLASS_NAMES= ['Vehicle', 'Pedestrian', 'Cyclist']

    to_draw = []

    positions_for_labels= []
    labels = []
    for i in range(len(result_item)):
        item = result_item[i]
        label = item[-2]
        labels.append(int(label))
        score = item[8]
        center = [item[0],item[1],item[2]]
        lwh = item[3:6] * 1
        axis_angles = np.array([0, 0, item[6] + 1e-10])
        rot = o3d.geometry.get_rotation_matrix_from_axis_angle(axis_angles)
        sample_box = o3d.geometry.OrientedBoundingBox(center, rot, lwh)
        if label == 0: #vehicle - red
            sample_box.color = [1,0,0]
        elif label == 1: #pedestrian - black
            sample_box.color = [0,0,0]
        elif label == 2: #cyclist - blue
            sample_box.color = [0,0,1]
        if score > score_threshold: 
            to_draw.append(sample_box)

        pos = o3d.geometry.OrientedBoundingBox.get_box_points(sample_box)[0]
        positions_for_labels.append(pos)

    mesh_frame = o3d.geometry.TriangleMesh().create_coordinate_frame(size=1, origin=[0, 0, 0])

    o3d.visualization.draw_geometries([pcd,*[bbox for bbox in to_draw], mesh_frame],front=[0.4699189535486108, -0.62764022425775134, 0.62068021233921933],
                lookat=[ -0.97243714332580566, -0.1751408576965332, 0.51464511454105377 ],
                up=[ -0.36828927493940194, 0.49961995188329117, 0.78405542766104697 ],
                zoom=0.05) 

def main():
    parser = argparse.ArgumentParser(description="Visualize point cloud data and bounding boxes.")
    parser.add_argument('--pointcloud_path', default="../muenchen/samples/LIDAR_TOP_bkp/1721650431_400103680.pcd" ,type=str, help="Path to the .pcd file containing pointcloud data.")
    parser.add_argument('--prediction_pickle_path',default="../muenchen/pcd_annotations/2024_07_22_muenchen_labeling_000.pkl" ,type=str, help="Path to the pickle file containing prediction results in ms3d format.")
    parser.add_argument('--confidence_threshold', default=0.4,type=float, help="The minimum confidence score required to display bounding boxes.")

    args = parser.parse_args()

    visualize_3d(args.pointcloud_path, args.prediction_pickle_path, args.confidence_threshold)

if __name__ == '__main__':
    ## usage python3 pseudolabel_visualizer_3d.py --pointcloud_path /Users/begumaltunbas/Desktop/idp/VISUALIZATION_EVALUATION/lepeng09_new/1718127706_599949824.pcd --prediction_pickle_path /Users/begumaltunbas/Desktop/idp/VISUALIZATION_EVALUATION/lepeng09_new/lepeng_09_not_labeled.pkl --confidence_threshold 0.4
    main()
