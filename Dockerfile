FROM python:3.9-alpine
#exporte la version del proyecto y la version ligera

WORKDIR  /app
#Con esto creamos una ruta para crear una carpeta dentro del contenedor

COPY . /app
#el punto ( . ) pasamos el desarrollo a una imagen

#RUN apk add --reinstall libpq-dev
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary
#instala las dependencias

EXPOSE 3050
#puerto expuesto

#ENTRYPOINT [ "python" ]

CMD [ "python", "app.py" ]
#CMD ["gunicorn", "-w", "2", "-t", "3600", "-b", "0.0.0.0:3050", "app:app"]
#Ejecutar la app de python
