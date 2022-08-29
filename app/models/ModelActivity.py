from app import db
from datetime import datetime
from app.models.ModelUser import ModelUsers

class ModelActivity(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    activity_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey(ModelUsers.id))

    def __repr__(self):
        return '<ModelActivity {}>'.format(self.activity_name)