# Barcode: Docker + Python + OpenCV + ZBar on Windows 7

This was created to help windows 7 users to run a python based barcode image decoder using **opencv** and **zbar**.

`barcode.sh` is ran inside a Docker container that is based from `continuumio/miniconda3` image

## Pre-requisites
1. This only applies to Windows 7 users
2. Install **Docker Toolbox**
3. You should have `bash` terminal *(Git bash or anything similar)*

## Instructions
1. Open the **Docker Toolbox** terminal
2. `cd` into your `~/Desktop` folder (`cd ~/Desktop`)
3. Clone the repo: `git clone https://github.com/ecovictoriano/barcode-docker-python-zbar-opencv-win7.git`
4. Build the image by running `./docker-build.sh`
5. Run and execute the `barcode.sh` script in an instance of the newly created image