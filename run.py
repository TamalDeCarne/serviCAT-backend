from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from api.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/servicat_db'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    return app

app = create_app()
db = SQLAlchemy(app)
ma = Marshmallow(app)
bycrypt = Bcrypt(app)

from api.blueprints.exports import *

app.register_blueprint(request)
app.register_blueprint(city)
app.register_blueprint(state)
app.register_blueprint(category)
app.register_blueprint(specialty)
app.register_blueprint(user)

if __name__ == '__main__':
    app.run(debug=True)