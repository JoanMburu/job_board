from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config


# Initialize the extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    # Initialize the extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app)

    # Import and register the blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.member_routes import member_bp
    from app.routes.employer_routes import employer_bp  
    from app.routes.job_routes import job_bp 
    from app.routes.log_routes import log_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(member_bp, url_prefix='/members')
    app.register_blueprint(employer_bp, url_prefix='/api/employers')
    app.register_blueprint(job_bp, url_prefix='/api/jobs')  
    app.register_blueprint(log_bp, url_prefix='/system')

    return app
