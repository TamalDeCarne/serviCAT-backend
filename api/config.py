import os

class Config:
    FLASK_ENV = os.environ.get('FLASK_ENV', 'dev')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:3306/servicat_db'
    #SQLALCHEMY_DATABASE_URI="mysql://admin:NeverCr0ssMeAgain!@localhost:3306/servicat_db?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_SIZE=100
    SQLALCHEMY_POOL_TIMEOUT=300