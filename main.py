#!/usr/bin/python3

from flask import Flask, render_template, Response
from plant_monitor import PlantMonitor
from picamera import PiCamera

pm = PlantMonitor()
camera = PiCamera()

app = Flask(__name__)

@app.route('/')

def index():
    templateData = {
            'wetness' : str(pm.get_wetness()),
            'temp' : str(pm.get_temp()),
            'humidity' : str(pm.get_humidity())
            }
    return render_template('index.html', **templateData)

def gen(camera):
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
