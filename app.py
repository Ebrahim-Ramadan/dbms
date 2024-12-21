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
    data = request.form  # Changed from json to form for the POST request
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO students (name, major, age, enrollment_year, gpa) VALUES (?, ?, ?, ?, ?)',
        (data['name'], data['major'], data['age'], data['enrollment_year'], data['gpa'])
    )
    conn.commit()
    conn.close()
    return redirect('/students')  # Redirect to the GET route to see the updated list


@app.route('/students/delete/<int:id>', methods=['GET'])
def delete_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/students')  # Redirect to the students list after deletion

if __name__ == '__main__':
    app.run(debug=True)
