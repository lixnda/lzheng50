'''
Michelle, Tanzeem, Linda
Purple Tortoise
SoftDev
K15 -- flask_forms
2024-10-9
time spent: 0.5
'''

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET'])
def disp_loginpage():
    return render_template( 'login.html' )

@app.route("/auth", methods=['GET'])
def authenticate():
    username = request.args['username']
    return render_template( 'response.html', name = username)


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()