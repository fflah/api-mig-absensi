from app.models.ModelUser import ModelUsers
from app.response import response
from app import db
from app import fernet
from flask_restful import Resource
from flask import request
from flask_jwt_extended import *
import datetime
import re


class Register(Resource):
    def post(self):
        try:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            account = ModelUsers.query.filter_by(email=email).first()
            if account:
                return response.bad_request('Account already exists', '')

            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                return response.bad_request('error email address', '')

            elif not name or not password or not email:
                return response.bad_request('Please fill out the form ', '')

            else:
                users = ModelUsers(name=name, email=email)
                users.setPassword(password)
                db.session.add(users)
                db.session.commit()
                return response.ok('success', '')

        except Exception as e:
            return response.bad_request("error", "{}".format(e))
        
class Login(Resource):
    def post(self):
        try:
            email = request.form['email']
            password = request.form['password']

            user = ModelUsers.query.filter_by(email=email).first()
            if not user:
                return response.bad_request('user not found', '')

            if not user.checkPassword(password):
                return response.bad_request('Your credentials is error', '')

            user_id_encrypt = fernet.encrypt(str(user.id).encode()).decode("utf-8")
            data = {
                'id': user_id_encrypt,
                'name': user.name,
                'email': user.email,
            }
            expires = datetime.timedelta(days=1)
            expires_refresh = datetime.timedelta(days=3)
            access_token = create_access_token(data, fresh=True, expires_delta=expires)
            refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

            return response.ok("success", {
                'data': data,
                'token_access': access_token,
                'token_refresh': refresh_token
            })
        except Exception as e:
            return response.bad_request("{}".format(e), '')

class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        try:
            user = get_jwt_identity()
            new_token = create_access_token(identity=user, fresh=False)

            return response.ok("success", {
                "token_access": new_token
            })

        except Exception as e:
            return response.bad_request("error", "{}".format(e))