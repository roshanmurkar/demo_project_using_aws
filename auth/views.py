from flask_sqlalchemy import SQLAlchemy
# from .models import db, InfoModel,InfoModelSchema
from models import db, InfoModel,InfoModelSchema
from flask import jsonify,request,Blueprint
from app import app
import json


userregister= Blueprint("userregister",__name__)

# general Flask Code
@userregister.route('/registration',methods=['POST'])
def register():
    user_data = request.get_json()
    info_model = InfoModel.query.all()
    info_model_schema = InfoModelSchema(many=True)
    output = info_model_schema.dump(info_model)
    for user in output:
        if user['username'] == user_data['username'] and int(user['password']) == int(user_data['password']):
            return jsonify({"message": "User is already Register", "Data": user_data})

    username = user_data['username']
    password = user_data['password']
    new_user = InfoModel(username,password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"New User registration successful","data":user_data})


details= Blueprint("details",__name__)
@details.route('/details',methods=['GET'])
def details():
    info_model = InfoModel.query.all()
    info_model_schema = InfoModelSchema(many=True)
    output = info_model_schema.dump(info_model)
    return jsonify({"message":"All User Registrations","details": output})


login= Blueprint("login",__name__)
@login.route('/login',methods=['POST'])
def login():
    user_data = request.get_json()
    info_model = InfoModel.query.all()
    info_model_schema = InfoModelSchema(many=True)
    output = info_model_schema.dump(info_model)
    for user in output:
        if user['username'] == user_data['username'] and int(user['password']) == int(user_data['password']):
            return jsonify({"message":"User Login Successful","Data":user_data})
    return jsonify({"message":"User Login Unsuccessful","Data":user_data})


if __name__ == '__main__':
    app.run(debug=True)