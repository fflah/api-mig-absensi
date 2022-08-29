from flask_restful import Resource
from flask import request
from datetime import datetime
from app.models.ModelActivity import ModelActivity
from app.models.ModelAbsensi import ModelAbsensi
from app.response import response
from flask_jwt_extended import *
from app import db, fernet
from sqlalchemy import cast, Date


class Activity(Resource):
    @jwt_required()
    def get(self):
        try:
            users = get_jwt_identity()
            id_user = fernet.decrypt(bytes(users['id'], 'utf-8')).decode()
            data_activity = ModelActivity.query.filter_by(user_id=id_user).all()
            result = []
            for item in data_activity:
                result.append(
                    {
                        'id': item.id,
                        'activity_name': item.activity_name,
                        'description': item.description
                    }
                )
            return response.ok("success", {
                'data': result
            })
        except Exception as e:
            return response.bad_request("{}".format(e), '')

    @jwt_required()
    def post(self):
        try:
            date = datetime.today().strftime('%Y-%m-%d')
            users = get_jwt_identity()
            id_user = fernet.decrypt(bytes(users['id'], 'utf-8')).decode()
            absensi = ModelAbsensi.query.filter(cast(ModelAbsensi.created_at, Date) == date).filter_by(type='checkin').filter_by(user_id=id_user).first()
            if absensi:
                activity_name = request.form.get('activity_name')
                description = request.form.get('description')
                activity = ModelActivity(activity_name=activity_name, description=description, user_id=id_user)
                db.session.add(activity)
                db.session.commit()
                return response.ok('success', "")
            else:
                return response.bad_request("invalid", 'silakan melakukan checkin terlebih dahulu')


        except Exception as e:
            return response.bad_request('invalid', "{}".format(e))

    @jwt_required()
    def put(self, id):
        try:
            date = datetime.today().strftime('%Y-%m-%d')
            users = get_jwt_identity()
            id_user = fernet.decrypt(bytes(users['id'], 'utf-8')).decode()
            absensi = ModelAbsensi.query.filter(cast(ModelAbsensi.created_at, Date) == date).filter_by(type='checkin').filter_by(user_id=id_user).first()
            if absensi:
                activity_name = request.form.get('activity_name')
                description = request.form.get('description')
                query = ModelActivity.query.get(id)
                query.activity_name = activity_name
                query.description = description
                query.updated_at = datetime.utcnow()
                db.session.commit()
                
                return response.ok('success', "")
            else:
                return response.bad_request("invalid", 'silakan melakukan checkin terlebih dahulu')
        except Exception as e:
            return response.bad_request("{}".format(e), '')

    @jwt_required()
    def delete(self, id):
        try:
            date = datetime.today().strftime('%Y-%m-%d')
            users = get_jwt_identity()
            id_user = fernet.decrypt(bytes(users['id'], 'utf-8')).decode()
            absensi = ModelAbsensi.query.filter(cast(ModelAbsensi.created_at, Date) == date).filter_by(type='checkin').filter_by(user_id=id_user).first()
            if absensi:
                query = ModelActivity.query.get(id)
                db.session.delete(query)
                db.session.commit()
                
                return response.ok('success', "")
            else:
                return response.bad_request("invalid", 'silakan melakukan checkin terlebih dahulu')
        except Exception as e:
            return response.bad_request("{}".format(e), '')


class ActivityFilterDate(Resource):
    @jwt_required()
    def get(self):
        try:
            users = get_jwt_identity()
            date = request.form.get('date')
           
            id_user = fernet.decrypt(bytes(users['id'], 'utf-8')).decode()
            data_activity = ModelActivity.query.filter(cast(ModelActivity.created_at, Date) == date).filter_by(user_id=id_user).all()
            result = []
            for item in data_activity:
                result.append(
                    {
                        'activity_name': item.activity_name,
                        'description': item.description,
                        'date': item.created_at
                    }
                )
            return response.ok("success", {
                'data': result
            })
        except Exception as e:
            return response.bad_request("{}".format(e), '')
