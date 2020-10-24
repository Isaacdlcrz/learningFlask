"""Initialize Flask app."""
from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    """Create Flask application."""
    application = Flask(__name__)
    application.config.from_object('config.Config')
    CORS(application)
    

    with application.app_context():
        
        #from .models import db, ma
        from .model.model import db, ma
        db.init_app(application)
        ma.init_app(application)
        
        # Import parts of our application
        #from .companies import companies
        
        # Register Blueprints
        #application.register_blueprint(companies.companies_bp, url_prefix="/companies/<id_company>")

        return application