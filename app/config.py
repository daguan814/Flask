import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess!'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Lhf@2001.@localhost:3306/course_select_system?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False