from flask import Flask, jsonify, request, redirect, render_template
from db_connection import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, enrollment_year, name, major , age, gpa FROM students')
    students = [{'id': row[0], 'enrollment_year': row[1], 'name': row[2], 'major': row[3], 'age': row[4], 'gpa': row[5]} for row in cursor.fetchall()]
    conn.close()
    return render_template('students.html', students=students)

@app.route('/students', methods=['POST'])
def add_student():
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
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/students')  



@app.route('/students/edit/<int:id>', methods=['GET'])
def edit_student_form(id):
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




if __name__ == '__main__':
    app.run(debug=True)
