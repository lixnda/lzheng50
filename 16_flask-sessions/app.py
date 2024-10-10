"""
Linda Zheng
ducky123
SoftDev
K<16> -- cookies n crumble (the code crumbles)
2024-10-10
time spent: 
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def login_page():
    render_template('login.html')
    
@app.route("/auth", methods=['POST'])
def auth_page():
    render_template('response.html', name=request.form['username'])
    
app.run()
app.debug()==True