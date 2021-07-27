from flask import Flask
from flask_cors import CORS
from models import db
from routes.user import user_bp
from routes.skill import skill_bp


def create_app():
    _app = Flask(__name__)
    _app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    _app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(_app)
    with _app.app_context():
        db.drop_all()
        db.create_all()
    _app.register_blueprint(user_bp)
    _app.register_blueprint(skill_bp)
    return _app


app = create_app()

CORS(app)

if __name__ == "__main__":
    app.run()
