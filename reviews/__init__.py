from flask import Flask
from reviews.main.controllers import main
from flask_cors import CORS, cross_origin


app = Flask(__name__)
#app.config.from_object('websiteconfig')
CORS(app)

app.register_blueprint(main)


