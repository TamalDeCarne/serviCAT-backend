from api.models import *
from api import ma
import simplejson as json

#Create Request VIEW
class RequestViewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RequestView
    id = ma.auto_field()
    title = ma.auto_field()
    body = ma.auto_field()
    user_fname = ma.auto_field()
    user_lname = ma.auto_field()
    city = ma.auto_field()
    state = ma.auto_field()
    category = ma.auto_field()
    specialty = ma.auto_field()

#States Table Schema
class StateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = State
        include_relationships = True
    id = ma.auto_field()
    key = ma.auto_field()
    name = ma.auto_field()
    abrev = ma.auto_field()
    active = ma.auto_field()

#City Table Schema
class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City
        include_fk = True
        include_relationships = True
    id = ma.auto_field()
    #edit ma.Nested(StateSchema(exclude=('name', 'key', 'abrev', 'active')))
    state_id = ma.auto_field()
    key = ma.auto_field()
    name = ma.auto_field()
    active = ma.auto_field()

#Users Table Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
    id = ma.auto_field()
    f_name = ma.auto_field()
    l_name = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()

#Category Table Schema
class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        include_fk = True
        included_relationships = True
    id = ma.auto_field()
    name = ma.auto_field()

#Specialty Table Schema
class SpecialtySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Specialty
        include_fk = True
        included_relationships = True
    id = ma.auto_field()
    name = ma.auto_field()
    #edit ma.Nested(StateSchema(exclude=('name', 'key', 'abrev', 'active')))
    category_id = ma.auto_field()

#Request Table Schema
class RequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Request
    id = ma.auto_field()
    title = ma.auto_field()
    body = ma.auto_field()
    #edit ma.Nested(StateSchema(exclude=('name', 'key', 'abrev', 'active')))
    user_id = ma.auto_field()
    city_id = ma.auto_field()
    state_id = ma.auto_field()
    category_id = ma.auto_field()
    specialty_id = ma.auto_field()
    date_requested = ma.auto_field()