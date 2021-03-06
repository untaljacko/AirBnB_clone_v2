#!/usr/bin/python3
""" A script that starts a Flask web application """


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return the message Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return the message HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ display C and the content of the text variable and replace underscore
    with space """
    return 'C %s' % text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
