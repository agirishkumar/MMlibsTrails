# MMlibsTrails
Playground experimenting different OpenMMLab libraries


## MMCV

To the docker image from dockerfile, run: `docker build -t mmcv-dev:latest .`

To attach the full project directory, access the gpu, gui and create a container with name: 
`docker run -it \
  --gpus all \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v $(pwd):/app/MMlibsTrails \
  -w /app/MMlibsTrails/mmcv \
  --name mmcv-container \
  mmcv-dev:latest`

  To start the conatiner: `docker start mmcv-container`
  To get into the container: `docker exec -it   -e DISPLAY=$DISPLAY   mmcv-container   /bin/bash`
