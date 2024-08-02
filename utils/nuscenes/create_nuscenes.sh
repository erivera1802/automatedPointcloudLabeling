rm -r ../muenchen/v1.0-mini
mkdir ../muenchen/v1.0-mini
python create_visibility.py
python create_attribute.py
python create_categories.py
python create_instance.py
python create_sensor.py
python create_log.py
python create_map.py
python create_ego_pose.py
python create_calibrated_sensor.py
python create_scene.py
python create_samples_samplesdata_samplesannotation.py
python update_firstlast.py
