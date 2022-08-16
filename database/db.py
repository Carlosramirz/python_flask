import psycopg2
from psycopg2 import DatabaseError


def get_connection():
    try:
        return psycopg2.connect(
            #host='localhost',
            host='postgres',
            #user='postgres',
            user='admin',
            password='1234',
            database='python_flask',
            port='5432'
        )
    except DatabaseError as ex:
        raise ex