from database.db import get_connection
from .entities.Usuarios import Usuario



class UsuariosModel():

    @classmethod
    def get_user(self):
        try:
            connection = get_connection()
            usuarios = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, username, password, fullname FROM usuarios ORDER BY fullname ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    usuario = Usuario(row[0], row[1], row[2], row[3])
                    usuarios.append(usuario.to_JSON())

            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_all_user(self, username):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, username, password, fullname FROM usuarios WHERE username = %s", (username,))
                row = cursor.fetchone()
                #buscador
                usuario = None
                if row != None:
                    usuario = Usuario(row[0], row[1], row[2], row[3])
                    usuario = usuario.to_JSON()
            #print('usuario: {}'.format(usuario))
            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_id_user(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, username, password, fullname FROM usuarios WHERE id = %s", (id,))
                row = cursor.fetchone()
                #buscador
                usuario = None
                if row != None:
                    usuario = Usuario(row[0], row[1], row[2], row[3])
                    usuario = usuario.to_JSON()
            
            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuarios (id, username, password, fullname)
                                VALUES (%s, %s, %s, %s)""", (usuario.id, usuario.username, usuario.password, usuario.fullname))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)


    
