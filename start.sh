#/bin/sh

export LD_LIBRARY_PATH=.
cd ~/mjpg_streamer/mjpg-streamer-experimental/
sh ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -hf"
