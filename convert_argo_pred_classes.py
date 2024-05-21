import pickle
import numpy as np

p_f_3 =   "/MS3D/output/MS3D/tools/cfgs/argo2_models/cbgs_voxel01_voxelnext/default/eval/epoch_2/val/argo1xyz_custom190_rwf_rwr/result.pkl"

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

with open(p_f_3, 'rb') as file:
    # Load the first object
    object3 = pickle.load(file)



for frame in object3:
    temp = []
    for name in frame['name']:
        temp.append(CLASS_MAPPING[name])

    frame['name'] = np.array(temp)


with open('/MS3D/output/MS3D/tools/cfgs/argo2_models/converted.pkl', 'wb') as file:
    pickle.dump(object3, file)

print('debug')

