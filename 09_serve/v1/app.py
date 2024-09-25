# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024


from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

#In this case, the print statement for __name__ is gone, so now, whenever the page is loaded, __main__ doesn't print into the terminal.

