from flask import Flask,jsonify,request
from student.views import student
from student.views import teacher
from student.views import subject
from student.views import student_teacher_rel
from student.views import teacher_subject_rel
#from auth.views import userregister
#from auth.views import login
#from auth.views import details
from app import app

app.register_blueprint(student)
app.register_blueprint(teacher)
app.register_blueprint(subject)
app.register_blueprint(student_teacher_rel)
app.register_blueprint(teacher_subject_rel)

#app.register_blueprint(userregister)
#app.register_blueprint(login)
#app.register_blueprint(details)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
