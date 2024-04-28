from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from pydantic import BaseModel

class DataModel(BaseModel):
    iid: str
    uid: str

db = SQLAlchemy()

class Usuarios(db.Model):
    user_id = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)


class UsuariosSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuarios
        include_relationships = True
        include_pk = True
        load_instance = True
