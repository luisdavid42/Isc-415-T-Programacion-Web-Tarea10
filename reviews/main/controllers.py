from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
	return "Home"

# from flask import Flask, request, jsonify
# from flask import render_template
# from flask_cors import CORS, cross_origin

# app = Flask(__name__)
# app.config.from_object('config')
# CORS(app)

# main = Blueprint('main',__name__)
# app.register(__main__,blueprint)


# @main.route("/")
# def index():
#     return 


# @main.route('/review', methods=['GET', 'POST'])
# def review():
#     if request.method == 'POST':
#         return jsonify("ok")
        
#     elif request.method == 'GET':
#         return "GET"

# if __name__ == "__main__":
#     app.run()