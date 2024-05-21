import pickle
import numpy as np

p_f_3 =   "/MS3D/output/MS3D/tools/cfgs/argo2_models/cbgs_voxel01_voxelnext/default/eval/epoch_2/val/argo1xyz_custom190_rwf_rwr/result.pkl"
#p_f_3 = '/MS3D/output/MS3D/tools/cfgs/argo2_models/converted_begum.pkl'

CLASS_MAPPING= {'Car': 'Vehicle',
                'car': 'Vehicle',                                
                'truck': 'Vehicle',
                'bus': 'Vehicle',
                'Vehicle': 'Vehicle',
                'Regular_vehicle': 'Vehicle',
                'Bus': 'Vehicle',
                'Box_truck': 'Vehicle',
                'Large_vehicle': 'Vehicle',
                'Truck': 'Vehicle',
                'School_bus': 'Vehicle',
                'Articulated_bus': 'Vehicle',
                'Message_board_trailer': 'Vehicle',
                'Truck_cab': 'Vehicle',
                'Vehicular_trailer': 'Vehicle',
                'bicycle': 'Cyclist',
                'Bicyclist': 'Cyclist',
                'motorcycle': 'Cyclist',
                'Cyclist': 'Cyclist',
                'Wheeled_rider': 'Cyclist',
                'Wheeled_device': 'Cyclist',
                'Wheelchair': 'Unknown',
                'Motorcyclist': 'Cyclist',
                'Motorcycle': 'Cyclist',
                'Bicycle': 'Cyclist',
                'pedestrian': 'Pedestrian',
                'Pedestrian': 'Pedestrian',
                'Bollard': 'Unknown',
                'Construction_cone': 'Unknown',
                'Sign': 'Unknown',
                'Stroller': 'Unknown',
                'Construction_barrel': 'Unknown',
                'Stop_sign': 'Unknown',
                'Mobile_pedestrian_crossing_sign': 'Unknown',
                'Dog': 'Unknown'}

class_to_int = {
    'Vehicle':0,
    'Pedestrian':2,
    'Cyclist':1,
    'Unknown':3}

with open(p_f_3, 'rb') as file:
    # Load the first object
    object3 = pickle.load(file)

#import pdb;pdb.set_trace()


new_dict = {}
for frame in object3:
    id = frame['frame_id']
    objects = []
    for obj_index in range(len(frame['boxes_lidar'])):
        box = frame['boxes_lidar'][obj_index] #length 7
        class_label = frame['name'][obj_index]
        mapped_class = CLASS_MAPPING[class_label] #map reg_vehcile to vehicle
        int_class = class_to_int[mapped_class] #map vehicle to 0
        score = frame['score'][obj_index]
        out = np.concatenate((box,np.array([int_class,score])),axis=None)
        objects.append(out)
    new_dict[id] = {'gt_boxes': objects }



    # boxes_lidar = frame['boxes_lidar']
    # scores =  frame['score']
    # label =  frame['name']
    # mapped_class = CLASS_MAPPING[label]
    # int_class = class_to_int[mapped_class]

    # new_dict[id]={'gt_boxes':[boxes_lidar],
    #               ''}

with open('/MS3D/output/MS3D/tools/cfgs/argo2_models/converted_begum.pkl', 'wb') as file:
    pickle.dump(new_dict, file)

print('debug')

