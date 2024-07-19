FROM pytorch/pytorch:2.3.1-cuda11.8-cudnn8-devel

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y vim && \
    apt-get install -y x11-apps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -U openmim

RUN mim install mmcv

CMD ["/bin/bash"]


