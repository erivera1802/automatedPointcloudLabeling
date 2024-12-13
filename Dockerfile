#FROM nvidia/cuda:11.6.2-cudnn8-devel-ubuntu20.04
#FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04
FROM nvidia/cuda:11.6.2-devel-ubuntu20.04
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Install basics
RUN apt-get update -y \
    #&& add-apt-repository ppa:deadsnakes/ppa \
    && apt-get install build-essential \
    && apt-get install -y apt-utils git curl ca-certificates bzip2 tree htop wget \
    && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev bmon iotop g++ 

# Install cmake v3.13.2
RUN apt-get purge -y cmake && \
    mkdir /root/temp && \
    cd /root/temp && \
    wget https://github.com/Kitware/CMake/releases/download/v3.13.2/cmake-3.13.2.tar.gz && \
    tar -xzvf cmake-3.13.2.tar.gz && \
    cd cmake-3.13.2 && \
    bash ./bootstrap && \
    make && \
    make install && \
    cmake --version && \
    rm -rf /root/temp

# RUN apt-get install software-properties-common -y \
#     && apt-get update \
#     && add-apt-repository ppa:deadsnakes/ppa \
#     && apt-get install -y python3.7 python3.7-dev python3.7-distutils python3.7-venv

# Install python
RUN ln -sv /usr/bin/python3 /usr/bin/python && apt-get install -y python3-pip
RUN pip install --upgrade pip
# RUN python -m ensurepip --upgrade
# # RUN wget https://bootstrap.pypa.io/get-pip.py && \
# # 	python get-pip.py && \
# # 	rm get-pip.py

# # Install python packages
# RUN PIP_INSTALL="python -m pip --no-cache-dir install" && \
#     $PIP_INSTALL numpy==1.19.3 llvmlite numba 
RUN python -m pip --no-cache-dir install numpy==1.19.3 llvmlite numba

# # Install torch and torchvision
# # See https://pytorch.org/ for other options if you use a different version of CUDA
# #RUN pip install --user torch==1.6 torchvision==0.7.0 -f https://download.pytorch.org/whl/cu102/torch_stable.html
RUN pip install --user torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116

# # Install python packages
# RUN PIP_INSTALL="python -m pip --no-cache-dir install" && \
#     $PIP_INSTALL tensorboardX easydict pyyaml scikit-image tqdm SharedArray six
RUN python -m pip --no-cache-dir install tensorboardX easydict pyyaml scikit-image tqdm SharedArray six
# WORKDIR /root

# Install Boost geometry
RUN wget https://jaist.dl.sourceforge.net/project/boost/boost/1.68.0/boost_1_68_0.tar.gz && \
    tar xzvf boost_1_68_0.tar.gz && \
    cp -r ./boost_1_68_0/boost /usr/include && \
    rm -rf ./boost_1_68_0 && \
    rm -rf ./boost_1_68_0.tar.gz 

# A weired problem that hasn't been solved yet
RUN pip uninstall -y SharedArray && \
    pip install SharedArray

RUN pip install spconv-cu102
RUN pip install opencv-python-headless
RUN apt-get install -y libgl1-mesa-dev
RUN pip install av2==0.2.0
RUN pip install kornia==0.5.8
RUN pip install torch-scatter==2.1.2
RUN pip install kiss-icp
RUN pip install open3d



RUN mkdir -p /MS3D
RUN mkdir -p /data
COPY setup.py /MS3D
COPY pcdet/ /MS3D/pcdet
COPY pcdet.egg-info/ /MS3D/pcdet.egg-info/
COPY tracker/ /MS3D/tracker


WORKDIR /MS3D
RUN ls -la /MS3D
# Set CUDA environment variables
ENV CUDA_HOME=/usr/local/cuda
ENV PATH=$CUDA_HOME/bin:$PATH
ENV LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
ENV TORCH_CUDA_ARCH_LIST="7.5" 


RUN python setup.py develop
RUN cd tracker
RUN pip install -e . --user
RUN git config --global --add safe.directory /MS3D

# ENTRYPOINT ["/bin/bash"]


# COPY entrypoint.sh /usr/local/bin/entrypoint.sh
# RUN chmod +x /usr/local/bin/entrypoint.sh
# ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]