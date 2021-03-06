import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
