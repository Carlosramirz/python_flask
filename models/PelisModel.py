from database.db import get_connection
from .entities.Peliculas import Peliculas


class PelisModel():

    @classmethod
    def get_movies(self):
        try:
            connection = get_connection()
            pelis = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, titulo, duracion, estreno FROM pelis ORDER BY titulo ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    peli = Peliculas(row[0], row[1], row[2], row[3])
                    pelis.append(peli.to_JSON())

            connection.close()
            return pelis
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_movie(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, titulo, duracion, estreno FROM pelis WHERE id = %s", (id,))
                row = cursor.fetchone()

                peli = None
                if row != None:
                    peli = Peliculas(row[0], row[1], row[2], row[3])
                    peli = peli.to_JSON()

            connection.close()
            return peli
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_movie(self, peli):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO pelis (id, titulo, duracion, estreno)
                                VALUES (%s, %s, %s, %s)""", (peli.id, peli.titulo, peli.duracion, peli.estreno))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_movie(self, peli):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE pelis SET titulo=%s, duracion=%s, estreno=%s
                                WHERE id =%s""", (peli.titulo, peli.duracion, peli.estreno, peli.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_movie(self, peli):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM pelis WHERE id = %s ", (peli.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
