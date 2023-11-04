from sqlalchemy import inspect
from datetime import datetime

from app.extensions import db


<<<<<<< HEAD
class User():
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    lastname = Column(String)
    profile_img = Column(String)
    password = Column(String, nullable=False)
    role = Column(String, default='USER')

    def __init__(self, name, email, phone, password, lastname=None, profile_img=None, role='USER'):
        self.name = name
        self.email = email
        self.phone = phone
        self.lastname = lastname
        self.profile_img = profile_img
        self.password = password
        self.role = role

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.phone}', '{self.role}')"
=======
class User(db.Model):
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
>>>>>>> prince
