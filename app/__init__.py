from flask import Flask
from .extensions import db, migrate, jwt, bcrypt 
from .routes.auth_routes import auth_bp
from .routes.note_routes import note_bp

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = "SECRET_KEY"


    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)


    app.register_blueprint(auth_bp)
    app.register_blueprint(note_bp)


    return app


