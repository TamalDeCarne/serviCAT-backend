from datetime import datetime, timedelta
from sqlalchemy.dialects.mysql import DATETIME
from api import db

#Create Request VIEW Model
class RequestView(db.Model):
    __tablename__ = "requests_v"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(64))
    user_fname = db.Column(db.String(64))
    user_lname = db.Column(db.String(64))
    city = db.Column(db.String(100))
    state = db.Column(db.String(64))
    category = db.Column(db.String(64))
    specialty = db.Column(db.String(64))

class Request(db.Model):
    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer)
    city_id = db.Column(db.Integer)
    state_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    specialty_id = db.Column(db.Integer)
    date_requested = db.Column(
        db.DateTime, nullable=False, default=datetime.now() + timedelta(hours=-6)
    )
    #missing user relationship

#Edit relationships
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    specialty = db.relationship(
        "Specialty",
        back_populates="categories",
        lazy="subquery"
    )

class Specialty(db.Model):
    __tablename__ = "specialties"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.id", onupdate="CASCADE", ondelete="SET NULL"), nullable=True
    )
    categories = db.relationship(
        "Category",
        back_populates="specialty",
        lazy="subquery"
    )

class City(db.Model):
    __tablename__ = "cities"
    id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(
        db.Integer, db.ForeignKey("states.id"), nullable=True
    )
    key = db.Column(db.String(3))
    name = db.Column(db.String(100))
    active = db.Column(db.Integer)
    states = db.relationship(
        "State",
        back_populates="city",
        lazy="subquery"
    ) # one-to-one

class State(db.Model):
    __tablename__ = "states"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64))
    name = db.Column(db.String(64))
    abrev = db.Column(db.String(64))
    active = db.Column(db.Integer)
    city = db.relationship(
        "City", 
        back_populates="states",
        lazy="subquery"
    )