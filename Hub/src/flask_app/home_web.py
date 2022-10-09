from datetime import datetime
import logging
from json_tool import convert_json_input
from flask import(Flask, render_template, request, jsonify) 

app = Flask(__name__)

logging.basicConfig(filename = 'log/SenseHome.log',
                        level = logging.DEBUG,
                        format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

date_time, converted = 'No record available', 'No record available'

@app.route('/SenseHome')
def index():
    return render_template('index.html')
@app.route('/SenseHome/data_stream', methods=('GET','POST'))
def data_stream():
    if request.method == 'POST':
        global date_time
        global converted
        date_time = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        content = request.get_json(silent=True)
        converted = convert_json_input(content)
    return render_template('data_gate/data_stream.html', converted=converted, date_time=date_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
