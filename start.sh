#/bin/sh

export LD_LIBRARY_PATH=.
~/mjpg_streamer/mjpg-streamer-experimental/mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -hf"
