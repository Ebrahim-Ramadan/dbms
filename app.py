from flask import Flask, session, request, redirect, render_template
from db_connection import get_db_connection
from dotenv import load_dotenv
import os

# Load env vars from .env file
load_dotenv()

app = Flask(__name__)


# Use the SECRET_KEY from the .env file
app.secret_key = os.getenv('APP_SECRET_KEY')  # Required for session management
# Predefined admin credentials
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/students', methods=['GET'])
def get_students():
    # Check if the admin is logged in
    if not session.get('logged_in'):
        return redirect('/login')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, enrollment_year, name, major , age, gpa FROM students')
    students = [{'id': row[0], 'enrollment_year': row[1], 'name': row[2], 'major': row[3], 'age': row[4], 'gpa': row[5]} for row in cursor.fetchall()]
    conn.close()
    return render_template('students.html', students=students, admingusername = ADMIN_USERNAME)

@app.route('/students', methods=['POST'])
def add_student():
    # Check if the admin is logged in
    if not session.get('logged_in'):
        return redirect('/login')
    
    data = request.form  
    age = int(data['age']) if data['age'] else None
    enrollment_year = int(data['enrollment_year']) if data['enrollment_year'] else None
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
            'INSERT INTO students (name, major, age, enrollment_year) VALUES (?, ?, ?, ?)',
            (data['name'], data['major'], age, enrollment_year)
        )
    conn.commit()
    conn.close()
    return redirect('/students')  


@app.route('/students/delete/<int:id>', methods=['GET'])
def delete_student(id):
    # Check if the admin is logged in
    if not session.get('logged_in'):
        return redirect('/login')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/students')  



@app.route('/students/edit/<int:id>', methods=['GET'])
def edit_student_form(id):
    # Check if the admin is logged in
    if not session.get('logged_in'):
        return redirect('/login')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, enrollment_year, name, major, age, gpa FROM students WHERE id = ?', (id,))
    student = cursor.fetchone()
    conn.close()
    if student:
        student_dict = {
            'id': student[0],
            'enrollment_year': student[1],
            'name': student[2],
            'major': student[3],
            'age': student[4],
            'gpa': student[5]
        }
        return render_template('edit_student.html', student=student_dict)
    return 'Student not found', 404

@app.route('/students/edit/<int:id>', methods=['POST'])
def update_student(id):
    # Check if the admin is logged in
    if not session.get('logged_in'):
        return redirect('/login')
    
    data = request.form
    age = int(data['age']) if data['age'] else None
    enrollment_year = int(data['enrollment_year']) if data['enrollment_year'] else None
    gpa = float(data['gpa']) if data['gpa'].strip() else None  

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
            '''UPDATE students 
               SET name = ?, major = ?, age = ?, enrollment_year = ?, gpa = ?
               WHERE id = ?''',
            (data['name'], data['major'], age, enrollment_year, gpa, id)
        )
    conn.commit()
    conn.close()
    return redirect('/students')




# Admin Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('form', request.form)
        username = request.form['username']
        password = request.form['password']
        print('os env', ADMIN_USERNAME, ADMIN_PASSWORD)
        print('cre', username, password)
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print('admin login')
            session['logged_in'] = True
            return redirect('/students')
        else:
            return 'Invalid credentials', 401
    return '''
    <link rel="stylesheet" href="static/style.css">
    <h1>Admin Login</h1>
        <form method="post" class="admin-login-form">
            <label for="username">Username:</label>
            <input type="text" name="username" id="username">
            <br>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password">
            <br>
            <input type="submit" value="Login">
        </form>
    '''

# Admin Logout Route
@app.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
