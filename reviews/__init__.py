from flask import Flask
from review.controllers.main import main
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

app.register_blueprint(main, url_prefix='/reviews')
from review.db import views, models
