from flask import Flask, render_template
from plant_monitor import PlantMonitor
pm = PlantMonitor()

app = Flask(__name__)

@app.route('/')

def index():
    templateData = {
            'wetness' : str(pm.get_wetness()),
            'temp' : str(pm.get_temp()),
            'humidity' : str(pm.get_humidity())
            }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
