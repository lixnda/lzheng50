"""
Linda Zheng
TEAMNAME
SoftDev
K<08> -- webapp and flask
2024-09-24
time spent: 0.3 

"""

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #where will this go?
    return "No hablo queso!"
    

app.debug = True                      #Before, the debugger was set to false by default, however, there is now a debugger
                                      #pin in the terminal.
app.run()
