from flask import Flask

##from config import config
from routes.auth import routes_auth
from dotenv import load_dotenv


#routes
from routes import Pelis

app = Flask(__name__)
app.config['SECRET_KEY']='Th1s1ss3cr3t'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


def page_not_found(error):
    return "<h1>No se encontro la pagina</h1>", 404

if __name__ == '__main__':
    load_dotenv()
    ##app.config.from_object(config['development'])

    #blueprints
    app.register_blueprint(Pelis.main, url_prefix='/api/pelis')
    app.register_blueprint(routes_auth, url_prefix="/api/user")

    #Error en la pagina
    app.register_error_handler(404, page_not_found)
    app.run(host='0.0.0.0', debug=True, port=3050)