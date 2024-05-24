#!/usr/bin/python3
'''A simple web application using flask'''
from flkask import Flask, render_template

from models import storage
from models.state import State


app = Flask(__name__)
'''The Flask application instance'''
app.url_map.strict_slashes = False

@app.route('/states_list')
def states_list():
    '''the states list page'''
    all_states = list(storage.all(States.values()))
    all_states.sort(key=lambda x: x.name)
    txt = {
            'states' : all_states
            }
    return render_template('7-states_list.html', **txt)

@app.teardown_appcontext
def flask_teardown(exec):
    '''The Flask event listener'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
