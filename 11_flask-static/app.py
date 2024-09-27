"""
Linda Zheng
Boa's
SoftDev
K11 - Flask-Static
2024-09-25
time spent: .5
"""
# Question one- the one in foo. I predicted that it would show up as basic HTML text but it actually downloaded the file.
# Question two- the one in foo.html. I predicted that it would print everything but most of the code was hidden by the <!-- and -->. This can be seen through the inspect screen.
# You can override the routes by setting it in the main function aka here. In here the second statment overrides the function and prints a random letter instead of the Is this plaintext, through?.
# DEMO
# basics of /static folder
import random
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"


@app.route("/static/foo.html")
def h():
    print("the __name__ of this module is... ")
    print(__name__)
    return str(random.random())

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
