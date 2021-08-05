from flask import Flask, request, render_template
from webapp.control_func import forward, backward, speedup, speeddown

app = Flask(__name__)


@app.route('/')
def return_controller():
    return render_template('index.html')


@app.route('/control')
def control():
    if request.args.get('func') == 'forward':
        forward()
    elif request.args.get('func') == 'backward':
        backward()
    elif request.args.get('func') == 'speedup':
        speedup()
    elif request.args.get('func') == 'speeddown':
        speeddown()
    else:
        pass
    return ''


app.run('0.0.0.0')
