#!/bin/bash

# Modify these paths and GPU ids
# DATA_PATH="/mnt/big-data/darren/data"
# CODE_PATH="/mnt/big-data/darren/code/MS3D"

DATA_PATH="/home/datasets/"
BEGUM_PATH="/home/altb/datasets/argo2"
# WAYMO_DATA_PATH="/home/altb/datasets/waymo_processed"
#CODE_PATH="/home/ubuntu/BegumGorkem/MS3D"
# CODE_PATH="/home/altb/idp-ms3d"

CODE_PATH="/home/altb/automatedpclabelling"
#CODE_PATH='/home/altb/OpenPCDet'

GPU_ID="0,1"

ENVS="  --env=NVIDIA_VISIBLE_DEVICES=$GPU_ID
        --env=CUDA_VISIBLE_DEVICES=$GPU_ID
        --env=NVIDIA_DRIVER_CAPABILITIES=all"

VOLUMES="       --volume=$DATA_PATH:/MS3D/data_temp
                --volume=$BEGUM_PATH:/MS3D/data_temp/argo"
                # --volume=$COPY_PATH:/pclabelling"
                # --volume=$WAYMO_DATA_PATH:/MS3D/data_temp/waymo
        


# Setup environmetns for pop-up visualization of point cloud (open3d)
VISUAL="        --env=DISPLAY
                --env=QT_X11_NO_MITSHM=1
                --volume=/tmp/.X11-unix:/tmp/.X11-unix
        "
xhost +local:docker

echo "Running the docker image [GPUS: ${GPU_ID}]"
#docker_image="darrenjkt/openpcdet:v0.6.0"
# docker_image="begumaltunbas/openpcdet:cuda11"
docker_image="begumaltunbas/openpcdet:cuda11_ms3d_v2"

# Start docker image
docker  run --name ms3d-container -d -it --rm \
$VOLUMES \
$ENVS \
$VISUAL \
--mount type=bind,source=$CODE_PATH,target=/MS3D \
--runtime=nvidia \
--gpus $GPU_ID \
--privileged \
--net=host \
--ipc=host \
--shm-size=30G \
--workdir=/MS3D \
$docker_image  
