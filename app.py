from flask import Flask, jsonify, request
from db_connection import get_db_connection

app = Flask(__name__)

@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, major FROM students')
    students = [{'id': row[0], 'name': row[1], 'major': row[2]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO students (id, name, major) VALUES (?, ?, ?)',
        (data['id'], data['name'], data['major'])
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Student added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
