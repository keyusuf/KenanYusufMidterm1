from flask import Flask, jsonify, request

app = Flask(__name__)

students = []

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    student = request.json
    students.append(student)
    return jsonify(student), 201

@app.route('/students/<id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s["ID"] == id), None)
    if student:
        updated_data = request.json
        student.update(updated_data)
        return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

@app.route('/students/<id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s["ID"] != id]
    return jsonify({"message": "Student deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
