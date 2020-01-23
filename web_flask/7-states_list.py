#!/usr/bin/python3
""" a script that starts a Flask web application """
import models
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ render states HTML template """
    state_list = list(storage.all("State").values())
    return render_template('7-states_list.html', states=state_list)


@app.teardown_appcontext
def teardown(exception):
    """ decorator for close storage """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
