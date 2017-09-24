FROM continuumio/miniconda3:4.3.21
MAINTAINER Victoriano Eco <eco.victoriano@gmail.com>

RUN ["/bin/bash", "-c", "apt-get update && apt-get install -y gcc && conda create -y -n barcode python=3.6.1 && source activate barcode && conda install -y opencv && pip install zbar-py && source deactivate"]

