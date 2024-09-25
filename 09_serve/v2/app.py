# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go? Both of these print statements will go into the terminal, but they will be on different lines.
                                  #Also the first statement prints directly what is in the quotes, while the second line prints the value for __name__: __main__.
    return "No hablo queso!"

app.run()

#The only difference from the previous versions is that there is an extra print statement that adds a new line to the terminal whenever the website is loaded / method is called.

