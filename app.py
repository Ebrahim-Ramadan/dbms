from flask import Flask, session, request, redirect, render_template, jsonify, url_for
from db_connection import get_db_connection
from dotenv import load_dotenv
import os
from datetime import datetime

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

@app.route('/register_student')
def register_student():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Fetch faculties
    cursor.execute('SELECT faculty_id, name FROM faculty')
    faculties = [{'id': row[0], 'name': row[1]} for row in cursor.fetchall()]
    conn.close()
    return render_template('register_student.html', faculties=faculties)

@app.route('/students', methods=['GET'])
def get_students():
    # Check if the admin is logged in
    if not session.get('logged_in'):
        return redirect('/login')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT student_id, enrollment_year, name, major , age, gpa, email, faculty_id FROM students')
    students = [{'id': row[0], 'enrollment_year': row[1], 'name': row[2], 'major': row[3], 'age': row[4], 'gpa': row[5], 'email': row[6], 'faculty_id': row[7]} for row in cursor.fetchall()]
    

    
    conn.close()
    return render_template('students.html', students=students, admingusername = ADMIN_USERNAME)

@app.route('/students', methods=['POST'])
def add_student():
    # Check if the admin is logged in
    if not session.get('logged_in'):
        return redirect('/login')
    
    data = request.form  
    age = int(data['age'].strip()) if data['age'].strip() else None
    enrollment_year = int(data['enrollment_year'].strip()) if data['enrollment_year'].strip() else None
    faculty_id = int(data['faculty_id'].strip()) if data['faculty_id'].strip() else None

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
            'INSERT INTO students (name, major, age, enrollment_year, email, faculty_id) VALUES (?, ?, ?, ?, ?, ?)',
            (data['name'], data['major'], age, enrollment_year, data['email'].strip(), faculty_id)
        )
    conn.commit()
    conn.close()
    return redirect('/students')  

@app.route('/students/faculty/<int:faculty_id>', methods=['GET'])
def get_students_by_faculty(faculty_id):
    # Check if the admin is logged in
    if not session.get('logged_in'):
        return redirect('/login')
    
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query to fetch students with the specified faculty_id and faculty name
    cursor.execute('''
        SELECT students.student_id, students.enrollment_year, students.name, students.major,
               students.age, students.gpa, students.email, faculty.name
        FROM students
        JOIN faculty ON students.faculty_id = faculty.faculty_id
        WHERE students.faculty_id = ?
    ''', (faculty_id,))
    
    students = [{
        'id': row[0], 'enrollment_year': row[1], 'name': row[2], 'major': row[3], 'age': row[4], 
        'gpa': row[5], 'email': row[6], 'faculty_name': row[7]
    } for row in cursor.fetchall()]
    

        # Query to fetch professors for the given faculty_id
    cursor.execute('''
        SELECT professor.professor_id, professor.name, professor.email, professor.nationalID
        FROM professor
        JOIN professor_faculty ON professor.professor_id = professor_faculty.professor_id
        WHERE professor_faculty.faculty_id = ?
    ''', (faculty_id,))

    professors = [{
        'id': row[0], 'name': row[1], 'email': row[2], 'nationalID': row[3]
    } for row in cursor.fetchall()]

    conn.close()

    # Render the template with the students and faculty name
    return render_template('students_by_faculty.html', students=students, professors=professors, faculty_name=students[0]['faculty_name'] if students else 'Unknown Faculty', faculty_id=faculty_id, admingusername=ADMIN_USERNAME)




@app.route('/students/delete/<int:id>', methods=['GET'])
def delete_student(id):
    # Check if the admin is logged in
    if not session.get('logged_in'):
        return redirect('/login')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE student_id = ?', (id,))
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
    cursor.execute('SELECT student_id, enrollment_year, name, major, age, gpa, email FROM students WHERE student_id = ?', (id,))
    student = cursor.fetchone()
    conn.close()
    if student:
        student_dict = {
            'id': student[0],
            'enrollment_year': student[1],
            'name': student[2],
            'major': student[3],
            'age': student[4],
            'gpa': student[5], 
            'email': student[6]
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
               SET name = ?, major = ?, age = ?, enrollment_year = ?, gpa = ?, email = ?
               WHERE student_id = ?''',
            (data['name'], data['major'], age, enrollment_year, gpa, data['email'].strip(), id)
        )
    conn.commit()
    conn.close()
    return redirect('/students')




# Admin Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        redirect_url = request.args.get('redirect', default=url_for('get_students'))

        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(redirect_url)
        else:
            return """
            <p>Invalid credentials</p>
            <button onclick="window.location.href='/login';">Retry</button>
            """
    return '''
    <link rel="stylesheet" href="static/style.css">
    
    <h1 style="color:blue;">

     <a href="/" style="text-decoration: none;">&#8592;</a>
       Admin Login</h1>
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



@app.route('/assign-internship', methods=['POST'])
def assign_internship():
    # Check if the admin is logged in
    if not session.get('logged_in'):
        return redirect('/login?redirect=assign-internship')
    
    # Handle form-encoded data
    student_id = request.form['student_id']
    company_name = request.form['company_name']
    position = request.form['position']
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    # Validate input
    if not (student_id and company_name and position and start_date and end_date):
        return jsonify({'error': 'All fields are required'}), 400
     # Validate dates
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

    if end_date_obj <= start_date_obj:
        return """
        <p style="color: red; font-weight: bold; font-size: 20px;">End date must be greater than start date</p>
        <button onclick="window.location.href='/assign-internship';">Retry</button>
        """
    

    conn = get_db_connection()
    cursor = conn.cursor()
    # Insert internship record
    cursor.execute("""
        INSERT INTO internships (company_name, position, start_date, end_date, student_id)
        VALUES (?, ?, ?, ?, ?)
    """, (company_name, position, start_date, end_date, student_id))
    conn.commit()
    conn.close()
    return "Internship assigned successfully!", 200

@app.route('/assign-internship', methods=['GET'])
def assign_internship_form():
    # Check if the admin is logged in
    if not session.get('logged_in'):
        return redirect('/login?redirect=assign-internship')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, name FROM students")
    students = [{'id': row[0], 'name': row[1]} for row in cursor.fetchall()]
    conn.close()
    return render_template('assign_internship.html', students=students)



if __name__ == '__main__':
    app.run(debug=True)
