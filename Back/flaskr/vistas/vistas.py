from flask_restful import Resource
from flask import request,  request, render_template, url_for
from flask_jwt_extended import create_access_token
from ..modelos import *
from datetime import datetime
from joblib import load
import pandas as pd
import json

usaurioSchema = UsuariosSchema()

class SignIn(Resource):
    def post(self):
            nuevo_usuario = Usuarios( 
                                  user_id=request.json["user_id"],
                                  password=request.json["password"])
            db.session.add(nuevo_usuario)
            db.session.commit()
            return {'menaje':'Usuario creado'}
            
            
class LogIn(Resource):
    def post(self):
        u_user = request.json["user_id"]
        u_contrasena = request.json["password"]
        usuario = Usuarios.query.filter_by(user_id=u_user, password=u_contrasena).first()
        token_de_Acceso = create_access_token(identity=request.json["user_id"])
        if usuario:
            return {'token:': token_de_Acceso}
        else:
            return {'mensaje':'Usuario no encontrado'}, 400

class Usuario(Resource):
    def post(self):
        user_id = request.json["user_id"]
        return usaurioSchema.dump(Usuarios.query.get_or_404(user_id))


class Predict(Resource):
    def post(self):
        return "test"
