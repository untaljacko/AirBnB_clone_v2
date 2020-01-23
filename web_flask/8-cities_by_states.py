#!/usr/bin/python3
""" a script that starts a Flask web application """
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ render cities by states HTML template """
    state_list = list(storage.all("State").values())
    return render_template('8-cities_by_states.html', states=state_list)


@app.teardown_appcontext
def teardown(exception):
    """ decorator for close storage """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
