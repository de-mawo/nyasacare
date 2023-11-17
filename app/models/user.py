from sqlalchemy import inspect
from datetime import datetime
from app.extensions import login_manager
from flask_login import UserMixin
from app.extensions import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    """ User Class for registerring users"""
    __tablename__ = 'users'
    id = db.Column(db.String(50), primary_key=True,
                   unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           default=datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(
    ), onupdate=datetime.now(), nullable=False)

    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100))
    profile_img = db.Column(db.String(100))
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), default='USER')

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    # def __repr__(self):
    #     return f"User('{self.name}', '{self.email}', '{self.phone}', '{self.role}')"
