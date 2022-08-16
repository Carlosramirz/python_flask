
#from distutils.command.config import config
#from urllib import response
from flask import request, jsonify, current_app
import jwt
from datetime import datetime, timedelta, timezone
#from re import split
from flask import Blueprint, request, jsonify
from models.UsuariosModel import UsuariosModel
from models.entities.Usuarios import Usuario
from functools import wraps

from utils.function_jwt import validate_token
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


routes_auth = Blueprint("routes_auth", __name__)


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        #print('holi')
        try:
            token = None
            #print('request' + request.headers['Authorization'].split(" ")[1])
            if request.headers['Authorization']:
                token = request.headers['Authorization'].split(" ")[1]
                #print('config', current_app.config['SECRET_KEY'])
                data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
                current_user = UsuariosModel.get_id_user(id=data['public_id']) #user by id
                
                if not current_user:
                    return jsonify({'message':'El usuario no existe'}),401
            else:
                return jsonify({'message': 'Falta autorizacion por token'}),401

        except Exception as ex:
            print('error', str(ex))
            return jsonify({'message': 'Ocurrio un error al validar el token'}),500 #mensajes al español

        return f(*args, **kwargs)
        
    return decorator

@routes_auth.route('/users')
@token_required
def get_user():
    try:
        usuario = UsuariosModel.get_user()
        # print(usuario)
        return jsonify({'usuario':usuario})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@routes_auth.route("/register", methods=["GET", "POST"])
def add_user():
    try:
        data = request.get_json()
        id = uuid.uuid4()
        hashed_password = generate_password_hash(
            data['password'], method='sha256')
        usuario = Usuario(
            str(id), data["username"], hashed_password, data["fullname"])
        affected_rows = UsuariosModel.add_user(usuario)

        if affected_rows == 1:
            return jsonify({"id_usuario": usuario.id, "message": "Usuario agregado correctamente",'agregado':True} )

        else:
            return jsonify({'message': 'Error al ingresar'}), 401
    except Exception as ex:
        return jsonify({'message': str(ex)}), 401


@routes_auth.route("/login", methods=['POST'])
def get_all_user():
    try:
        auth = request.get_json()
                
        if not auth or not auth["username"] or not auth["password"]:            
            return jsonify({'message':'Datos invalidos'}), 401
            #return make_response('could not verify', 401, {'message': 'Basic realm: "login required"'})
            
        usuario = UsuariosModel.get_all_user(auth["username"])
        
        if check_password_hash(usuario["password"], auth["password"]):
            exp = datetime.now(tz=timezone.utc) + timedelta(minutes=30)
            #exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            #print(exp)
            token = jwt.encode({'public_id': usuario["id"], 'exp': exp}, 'Th1s1ss3cr3t')
            #token = jwt.encode({'public_id': usuario["id"], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'Th1s1ss3cr3t')
            
            return jsonify({
                "exp": datetime.timestamp(exp), 
                "status":True, 
                "token": token, 
                #"token": token.encode('UTF-8'), 
                "usuario":{
                    "id_usuario": usuario["id"],
                    "username": auth["username"]
                    }})

        return jsonify({'message':'Usuario o contraseña incorrectos'}), 401
        #return make_response('could not verify',  401, {'message': 'Basic realm: "login required"'})

    except Exception as ex:
        print("error", ex)
        return jsonify({'message': "Ocurrio un error al procesar la solicitud"}), 500
        #return jsonify({'message': str(ex)}), 500




# @routes_auth.route("/login", methods=['POST'])
# def login():
#    data = request.get_json()
#    if data == Usuario(str(id), data["username"], data["password"], data["fullname"]):
#        return write_token(data=request.get_json())
#    else:
#        response = jsonify({"message":"Usuario no encontrado"})
#        response.status_code = 404
#        return response



@routes_auth.route("/token")
def verify():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=True)
