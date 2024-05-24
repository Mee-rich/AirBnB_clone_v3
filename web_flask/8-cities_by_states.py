#!/usr/bin/python3
'''A simple web application using flask'''
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)
'''The Flask application instances'''
app.url_map.strict_slashes = False

@app.route('/cities_by_states')
def cities_by_states():
    '''The cities_by_states page'''
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)

    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    txt = {
            'states': all_states
            }
    return render_template('8-cities_by_states.html', **txt)


@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask event listener'''
    storage.close()
