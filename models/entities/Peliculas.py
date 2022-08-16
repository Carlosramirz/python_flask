from utils.DateFormat import DateFormat


class Peliculas ():

    def __init__(self, id, titulo=None, duracion=None, estreno=None) -> None:
        self.id = id
        self.titulo = titulo
        self.duracion = duracion
        self.estreno = estreno

    def to_JSON(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'duracion': self.duracion,
            'estreno': DateFormat.convert_date(self.estreno)
        }


