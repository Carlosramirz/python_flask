from .auth import token_required


from flask import Blueprint, jsonify, request

import uuid

# entities
from models.entities.Peliculas import Peliculas


# models
from models.PelisModel import PelisModel
#from ..utils.token import token_required


main = Blueprint('pelis_blueprint', __name__)



@main.route('/')
@token_required
def get_movies():
    try:
        pelis = PelisModel.get_movies()
        return jsonify(pelis)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
@token_required
def get_movie(id):
    try:
        pelis = PelisModel.get_movie(id)
        if pelis != None:
            return jsonify(pelis)
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
@token_required
def add_movie():
    try:
        titulo = request.json['titulo']
        duracion = int(request.json['duracion'])
        estreno = request.json['estreno']
        id = uuid.uuid4()
        pelicula = Peliculas(str(id), titulo, duracion, estreno)

        affected_rows = PelisModel.add_movie(pelicula)

        if affected_rows == 1:
            return jsonify({'id':pelicula.id, 'titulos': pelicula.titulo,'message':'Pelicula agregada'})
        else:
            return jsonify({'message': 'Error al insertar'}), 500

        # return jsonify({})

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
@token_required
def update_movie(id):
    try:
        titulo = request.json['titulo']
        duracion = int(request.json['duracion'])
        estreno = request.json['estreno']
        pelicula = Peliculas(id, titulo, duracion, estreno)

        affected_rows = PelisModel.update_movie(pelicula)

        if affected_rows == 1:
            return jsonify({'id':pelicula.id, 'titulos': pelicula.titulo, 'message':'Actualizacion realizada con exito'})
        else:
            return jsonify({'message': 'Error al actualizar'}), 500

        # return jsonify({})

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
@token_required
def delete_movie(id):
    try:
        pelicula = Peliculas(id)

        affected_rows = PelisModel.delete_movie(pelicula)

        if affected_rows == 1:
            return jsonify({'id':pelicula.id, 'titulos': pelicula.titulo,'message':'Pelicula eliminada'})
        else:
            return jsonify({'message': 'Error al eliminar'}), 404

        # return jsonify({})

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

    