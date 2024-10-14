"""
Linda Zheng, Ryan, Michelle
boas
SoftDev
K<16> -- cookies n crumble (the code crumbles)
2024-10-10
time spent: 1
"""
from flask import Flask, render_template, request, session
import secrets
from flask import redirect
from flask import url_for

app = Flask(__name__)    #create Flask object

app.secret_key = secrets.token_hex()


@app.route("/")
def main():
    return 'head to /login'

@app.route('/login', methods=['GET', 'POST'])
def disp_loginpage():
    print(session)
    #print(request)
    #print(request.args)
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('authenticate'))
    if 'username' in session:
        return f'hello {session["username"]}'
    return render_template( 'login.html' )
    
@app.route("/auth", methods=['GET','POST'])
def authenticate():
    print(session)
    #print(app)
    #print(request)
    #print(request.args)
    if 'username' in session:
        return render_template('response.html', name=session['username'])
    return 'You are not logged in, head to /login'

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return render_template('logout.html')
    
if __name__ == "__main__":
    app.debug = True 
    app.run()
"""
from flask import Flask
from flask import session
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'qwrqwsxolwcbuytr_5#y2L"ujedcF4Qsdfastiugyhkb8z\nasdf\xecgb;lkiy]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
"""