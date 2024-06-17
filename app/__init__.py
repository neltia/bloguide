# flask app
from flask import Flask
from flask import Blueprint
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

# get blueprint
from app.admin.container import container_ns


def create_app():
    # app init
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    api = Api(app, version='1.0', title='BloGuide API')

    # namesapces
    api_bp_admin = Blueprint('api', __name__, url_prefix='/admin')
    api.add_namespace(container_ns)

    # blueprint register
    app.register_blueprint(api_bp_admin)

    return app
