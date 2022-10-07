#!/bin/sh

sudo apt update
sudo apt upgrade -y
git clone https://github.com/jacksonliam/mjpg-streamer.git
sudo apt install cmake python-pil libjpeg-dev -y
cd mjpg-streamer/mjpg-streamer-experimental/
make CMAKE_BUILD_TYPE=Debug
sudo make install
sudo apt install ngrok python3-flask node

curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
