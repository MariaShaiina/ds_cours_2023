#!/bin/bash
echo Setting env vars

export ubuntu_ver=22.04
export cuda_ver=12-2
export qt_mm_ver=5.15
export qt_rev_ver=1
export ocv_ver=4.8.0
export build_thread_count=3
export image_tag=mariiashaina
export dockerfile=TarsierDockerfile

# Check if the Ubuntu image exists before pulling
if docker image inspect ubuntu:$ubuntu_ver 1>/dev/null; then
  echo "Docker image ubuntu:$ubuntu_ver is found."
else
  echo "Pulling docker image ubuntu:$ubuntu_ver..."
  docker pull ubuntu:$ubuntu_ver
fi

# Build the docker image
docker build --tag $image_tag \
             --build-arg ubuntu_ver=$ubuntu_ver \
             --build-arg cuda_ver=$cuda_ver \
        		 --build-arg cuda_distro=$cuda_distro \
        		 --build-arg cuda_arch=$cuda_arch \
             --build-arg qt_mm_ver=$qt_mm_ver \
             --build-arg qt_rev_ver=$qt_rev_ver \
             --build-arg ocv_ver=$ocv_ver \
             --build-arg build_thread_count=$build_thread_count \
             -f $dockerfile .
