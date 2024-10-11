"""
Linda Zheng
ducky123
SoftDev
K<16> -- cookies n crumble (the code crumbles)
2024-10-10
time spent: 
"""

from flask import Flask, render_template, request, session

app = Flask(__name__)    #create Flask object

app.secret_key = 

@app.route("/")
def main():
    if 'name' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login')
def disp_loginpage():
    print(app)
    print(request)
    print(request.args)
    return render_template( 'login.html' )
    
@app.route("/auth", methods=['POST'])
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return render_template('response.html', name=request.cookies.get('username'))
    
if __name__ == "__main__":
    app.debug = True 
    app.run()