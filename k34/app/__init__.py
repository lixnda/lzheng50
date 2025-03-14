from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    if 'username' in session:
        conn = get_db_connection()
        blogs = conn.execute('SELECT * FROM blog').fetchall()
        conn.close()
        return render_template('index.html', blogs=blogs)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        
        conn = get_db_connection()
        conn.execute('INSERT INTO user (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()

        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM user WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['username'] = user['username']
            return redirect(url_for('index'))
        flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/create_blog', methods=['GET', 'POST'])
def create_blog():
    if 'username' in session:
        if request.method == 'POST':
            title = request.form['title']
            
            conn = get_db_connection()
            user = conn.execute('SELECT * FROM user WHERE username = ?', (session['username'],)).fetchone()
            conn.execute('INSERT INTO blog (title, user_id) VALUES (?, ?)', (title, user['id']))
            conn.commit()
            conn.close()

            return redirect(url_for('index'))
        return render_template('create_blog.html')
    return redirect(url_for('login'))

@app.route('/blog/<int:blog_id>')
def view_blog(blog_id):
    conn = get_db_connection()
    blog = conn.execute('SELECT * FROM blog WHERE id = ?', (blog_id,)).fetchone()
    entries = conn.execute('SELECT * FROM entry WHERE blog_id = ?', (blog_id,)).fetchall()
    conn.close()
    return render_template('view_blog.html', blog=blog, entries=entries)

@app.route('/add_entry/<int:blog_id>', methods=['GET', 'POST'])
def add_entry(blog_id):
    if 'username' in session:
        if request.method == 'POST':
            content = request.form['content']
            
            conn = get_db_connection()
            conn.execute('INSERT INTO entry (content, blog_id) VALUES (?, ?)', (content, blog_id))
            conn.commit()
            conn.close()

            return redirect(url_for('view_blog', blog_id=blog_id))
        return render_template('add_entry.html', blog_id=blog_id)
    return redirect(url_for('login'))

@app.route('/edit_entry/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    if 'username' in session:
        conn = get_db_connection()
        entry = conn.execute('SELECT * FROM entry WHERE id = ?', (entry_id,)).fetchone()
        blog = conn.execute('SELECT * FROM blog WHERE id = ?', (entry['blog_id'],)).fetchone()
        user = conn.execute('SELECT * FROM user WHERE username = ?', (session['username'],)).fetchone()

        # Check if the logged-in user is the owner of the entry
        if blog['user_id'] == user['id']:
            if request.method == 'POST':
                content = request.form['content']
                conn.execute('UPDATE entry SET content = ? WHERE id = ?', (content, entry_id))
                conn.commit()
                conn.close()
                return redirect(url_for('view_blog', blog_id=entry['blog_id']))
            conn.close()
            return render_template('edit_entry.html', entry=entry)
        else:
            conn.close()
            flash('You do not have permission to edit this entry.')
            return redirect(url_for('index'))
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS blog (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES user (id)
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS entry (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                blog_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                FOREIGN KEY (blog_id) REFERENCES blog (id)
            )
        ''')
        conn.commit()
        conn.close()
    app.run(debug=True)
