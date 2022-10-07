#!/bin/sh

sudo apt update
sudo apt upgrade -y
sudo apt install git python3-flask cmake python-pil libjpeg-dev -y
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental/
make CMAKE_BUILD_TYPE=Debug
sudo make install
