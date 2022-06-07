from urllib import request

from flask import Flask, render_template, request

import os
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{basedir}/sqlite.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    semester = db.Column(db.String(120), unique=True, nullable=False)
    GPA = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'Student("{self.id}", "{self.name}", "{self.semester}", "{self.GPA}")'


@app.route('/')
def index():
    return render_template('Student.html', students=Student.query.all())


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student = Student(request.form['id'], request.form['name'],
                           request.form['semester'], request.form['GPA'])
        db.session.add(Student)
        db.session.commit()
    else: print('error')
    return render_template('add_student.html')



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)
