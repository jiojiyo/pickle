import os
import sqlite3

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'imdb.db'))
# SQLALCHEMY의 이벤트를 처리하는 옵션 
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY="dev"

