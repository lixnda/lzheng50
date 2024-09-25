# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # app defines a new instance of Flask with the parameter of __name__, which just inputs the location of this relative to project

@app.route("/")                # This defines the following function at a certain point in the directory, with the / being at the root, or at (url)/
def hello_world():
    print(__name__)            # This statement just prints the origin of the file, being __name__, into the terminal, whenver the method is run.
    return "No hablo queso!"   # This statement returns what is to be displayed the website, where flask takes the response and puts it into html.

app.run()                      # This initiates the app and runs it depending on which method is accessed, and actually creates the output.
