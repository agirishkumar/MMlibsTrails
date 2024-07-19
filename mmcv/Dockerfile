FROM pytorch/pytorch:2.3.1-cuda11.8-cudnn8-devel

WORKDIR /app

RUN apt-get update && \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxcb1 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-xinerama0 \
    libxkbcommon-x11-0 \
    libqt5x11extras5\
    apt-get install -y git && \
    apt-get install -y vim && \
    apt-get install -y x11-apps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -U openmim

RUN mim install mmcv

CMD ["/bin/bash"]


