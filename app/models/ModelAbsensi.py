from app import db
from datetime import datetime
from app.models.ModelUser import ModelUsers

class ModelAbsensi(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey(ModelUsers.id))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    type = db.Column(db.String(120), nullable=False)
    users = db.relationship("ModelUsers", backref="user_id")

    def __repr__(self):
        return '<ModelAbsensi {}>'.format(self.type)