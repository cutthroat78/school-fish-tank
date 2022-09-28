#!/bin/sh

sudo apt update
sudo apt upgrade -y
git clone https://github.com/jacksonliam/mjpg-streamer.git
sudo apt install cmake python-pil libjpeg-dev -y
cd mjpg-streamer/mjpg-streamer-experimental/
make CMAKE_BUILD_TYPE=Debug
sudo make install
