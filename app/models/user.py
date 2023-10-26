import uuid
from enum import Enum
from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import validates
from app.models.base_model import Base
from sqlalchemy.dialects.postgresql import UUID

# class UserRoleEnum(Enum):
#     USER = 'USER'
#     ADMIN = 'ADMIN'
#     PROVIDER = 'PROVIDER'


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
