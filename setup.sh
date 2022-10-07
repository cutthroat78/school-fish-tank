#!/bin/sh

sudo apt update
sudo apt upgrade -y
sudo apt install git python3-flask cmake python-pil libjpeg-dev -y
sudo pip3 install camera
mkdir ~/data
