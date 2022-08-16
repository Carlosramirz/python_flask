
import jwt

from flask import jsonify


def validate_token(token, output=False):
    try:
        if output:
            return jwt.decode(token, key=("Th1s1ss3cr3t"), algorithms=["HS256"])
        jwt.decode(token, key=("Th1s1ss3cr3t"), algorithms=["HS256"])
    except jwt.exceptions.DecodeError:
        response = jsonify({"message": "Token invalido"})
        response.status_code = 401
        return response
    except jwt.exceptions.ExpiredSignatureError:
        response = jsonify({"message": "Token expirado"})
        response.status_code = 401
        return response