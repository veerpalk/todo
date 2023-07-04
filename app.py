from flask import Flask, render_template, redirect, request, session
from flask_mysqldb import MySQL
import bcrypt
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'todo'
mysql = MySQL(app)

print('App started ...')


@app.route('/')
def home():
    return redirect('/dashboard')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        # Hash the password
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        # Store the user in the database
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                       (username, hashed_password))
        mysql.connection.commit()

        return redirect('/login')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        print('After encoding : ---- ',password)
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
     
        if user and bcrypt.checkpw(password, user[2].encode('utf-8')):
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect('/dashboard')
        else:
            error = 'Invalid username or password.'
            return render_template('login.html', error=error)

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id = session['user_id']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tasks WHERE user_id = %s", (user_id,))
        tasks = cursor.fetchall()
        print(tasks)
        return render_template('dashboard.html', tasks=tasks)
    else:
        return redirect('/login')


@app.route('/task/new', methods=['GET', 'POST'])
def new_task():
    current_datetime = datetime.datetime.now() 
    if 'user_id' in session:
        if request.method == 'POST':
            user_id = session['user_id']
            title = request.form['title']
            description = request.form['description']
            priority = request.form['priority']
            category = request.form['category']
            due_date = request.form['due_date']

            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO tasks (user_id, title, description, priority, category, due_date) VALUES (%s, %s, %s, %s, %s, %s)",
                           (user_id, title, description, priority, category, due_date))
            mysql.connection.commit()

            return redirect('/dashboard')

        return render_template('new_task.html', current_datetime=current_datetime )
    else:
        return redirect('/login')


@app.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    if 'user_id' in session:
        user_id = session['user_id']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = %s AND user_id = %s", (task_id, user_id))
        task = cursor.fetchone()
        current_datetime = datetime.datetime.now() 
        if not task:
            return redirect('/dashboard')

        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            priority = request.form['priority']
            # status = request.form['status']
            category = request.form['category']
            due_date = request.form['due_date']

            cursor.execute("UPDATE tasks SET title = %s, description = %s, priority = %s, category = %s, due_date = %s WHERE id = %s",
                           (title, description, priority, category, due_date, task_id))
            mysql.connection.commit()

            return redirect('/dashboard')

        return render_template('edit_task.html', task=task, current_datetime=current_datetime)
    else:
        return redirect('/login')


@app.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    if 'user_id' in session:
        user_id = session['user_id']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = %s AND user_id = %s", (task_id, user_id))
        task = cursor.fetchone()

        if not task:
            return redirect('/dashboard')

        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        mysql.connection.commit()

        return redirect('/dashboard')
    else:
        return redirect('/login')


@app.route('/task/<int:task_id>/update', methods=['POST'])
def update_task_status(task_id):
    if 'user_id' in session:
        user_id = session['user_id']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = %s AND user_id = %s", (task_id, user_id))
        task = cursor.fetchone()

        if not task:
            return redirect('/dashboard')

        new_status = request.form['status']

        cursor.execute("UPDATE tasks SET status = %s WHERE id = %s", (new_status, task_id))
        mysql.connection.commit()

        return redirect('/dashboard')
    else:
        return redirect('/login')
