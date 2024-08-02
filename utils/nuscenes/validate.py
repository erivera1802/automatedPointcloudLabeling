from nuscenes.nuscenes import NuScenes
import os
print(os.getcwd())
nusc = NuScenes(version='v1.0-mini', dataroot='../muenchen', verbose=True)

nusc.list_scenes()
my_scene = nusc.scene[0]
last_sample_token = my_scene['last_sample_token']
my_sample = nusc.get('sample', last_sample_token)

nusc.render_sample_data(my_sample["data"]["LIDAR_TOP"])