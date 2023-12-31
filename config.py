import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """ Class that defines the database and secret env variables """    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
        # or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False