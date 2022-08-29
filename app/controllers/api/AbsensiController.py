from flask_restful import Resource
from flask import request
from datetime import datetime
from app.models.ModelAbsensi import ModelAbsensi
from app.response import response
from flask_jwt_extended import *
from app import fernet, db

class Checkin(Resource):
    @jwt_required()
    def post(self):
        try:
            users = get_jwt_identity()
            id_user = fernet.decrypt(bytes(users['id'], 'utf-8')).decode()
            absensi = ModelAbsensi(user_id=id_user, type="checkin")
            db.session.add(absensi)
            db.session.commit()
            return response.ok("success", "")
            
        except Exception as e:
            return response.bad_request("{}".format(e), '')

class Checkout(Resource):
    @jwt_required()
    def post(self):
        try:
            users = get_jwt_identity()
            id_user = fernet.decrypt(bytes(users['id'], 'utf-8')).decode()
            absensi = ModelAbsensi(user_id=id_user, type="checkout")
            db.session.add(absensi)
            db.session.commit()
            return response.ok("success", "")
            
        except Exception as e:
            return response.bad_request("{}".format(e), '')

class RiwayatAbsensi(Resource):
    @jwt_required()
    def get(self):
        try:
            users = get_jwt_identity()
            id_user = fernet.decrypt(bytes(users['id'], 'utf-8')).decode()
            data_absensi = ModelAbsensi.query.filter_by(user_id=id_user).all()
            result = []
            for item in data_absensi:
                result.append(
                    {
                        'type_absensi': item.type,
                        'date': item.created_at
                    }
                )
            return response.ok("success", {
                'data': result
            })
            
        except Exception as e:
            return response.bad_request("{}".format(e), '')

