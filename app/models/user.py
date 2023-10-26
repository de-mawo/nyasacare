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
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    lastname = Column(String)
    profile_img = Column(String)
    password = Column(String, nullable=False)
    role = Column(String, default='USER')

    
    
    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.phone}', '{self.role}')"
