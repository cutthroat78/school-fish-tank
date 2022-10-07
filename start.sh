#/bin/sh

export LD_LIBRARY_PATH=.
mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -hf" &
python3 ~/School-Fish-Tank/main.py
