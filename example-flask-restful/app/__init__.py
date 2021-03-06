# app/__init__.py
import json
from flask_api import FlaskAPI, status
# from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask import request, jsonify, abort, make_response, Flask

# local import
from app.restfulapi import Quotes
from instance.config import app_config

# For password hashing
# from flask_bcrypt import Bcrypt


# initialize db
# db = SQLAlchemy()


def create_app(config_name):

    # uncomment below 3 lines for restful API
    # app = Flask(__name__)
    # api = Api(app)
    # api.add_resource(Quotes, '/')
    # #########################

    # from app.models import Bucketlist, User

    # comment out below line for rest API
    app = FlaskAPI(__name__, instance_relative_config=True)

    # overriding Werkzeugs built-in password hashing utilities using Bcrypt.
    # bcrypt = Bcrypt(app)

    app.config.from_object(app_config[config_name])

    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # db.init_app(app)

    @app.route('/bucketlists/', methods=['POST', 'GET'])
    def bucketlists():
        response = {
            'message': 'test POST'
        }
        return make_response(jsonify(response)), 200
        # get the access token
        # auth_header = request.headers.get('Authorization')
        # access_token = auth_header.split(" ")[1]
        #
        # if access_token:
        #     user_id = User.decode_token(access_token)
        #     if not isinstance(user_id, str):
        #         # Go ahead and handle the request, the user is authed
        #         if request.method == "POST":
        #             name = str(request.data.get('name', ''))
        #             if name:
        #                 bucketlist = Bucketlist(name=name, created_by=user_id)
        #                 bucketlist.save()
        #                 response = jsonify({
        #                     'id': bucketlist.id,
        #                     'name': bucketlist.name,
        #                     'date_created': bucketlist.date_created,
        #                     'date_modified': bucketlist.date_modified,
        #                     'created_by': user_id
        #                 })
        #
        #                 return make_response(response), 201
        #
        #         else:
        #             # GET
        #             # get all the bucketlists for this user
        #             bucketlists = Bucketlist.get_all(user_id)
        #             results = []
        #
        #             for bucketlist in bucketlists:
        #                 obj = {
        #                     'id': bucketlist.id,
        #                     'name': bucketlist.name,
        #                     'date_created': bucketlist.date_created,
        #                     'date_modified': bucketlist.date_modified,
        #                     'created_by': bucketlist.created_by
        #                 }
        #                 results.append(obj)
        #
        #             return make_response(jsonify(results)), 200
        #     else:
        #         # user is not legit, so the payload is an error message
        #         message = user_id
        #         response = {
        #             'message': message
        #         }
        #         return make_response(jsonify(response)), 401

    # @app.route('/bucketlists/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    # def bucketlist_manipulation(id, **kwargs):
    #     response = {
    #         'message': 'test GET'+id
    #     }
    #     return make_response(jsonify(response)), 200
    # auth_header = request.headers.get('Authorization')
    # access_token = auth_header.split(" ")[1]
    #
    # if access_token:
    #     user_id = User.decode_token(access_token)
    #     if not isinstance(user_id, str):
    #         bucketlist = Bucketlist.query.filter_by(id=id).first()
    #         if not bucketlist:
    #             # Raise an HTTPException with a 404 not found status code
    #             abort(404)
    #
    #         if request.method == "DELETE":
    #             bucketlist.delete()
    #             return {
    #                 "message": "bucketlist {} deleted".format(bucketlist.id)
    #             }, 200
    #         elif request.method == 'PUT':
    #             name = str(request.data.get('name', ''))
    #             bucketlist.name = name
    #             bucketlist.save()
    #             response = {
    #                 'id': bucketlist.id,
    #                 'name': bucketlist.name,
    #                 'date_created': bucketlist.date_created,
    #                 'date_modified': bucketlist.date_modified,
    #                 'created_by': bucketlist.created_by
    #             }
    #             return make_response(jsonify(response)), 200
    #         else:
    #             # GET
    #             response = jsonify({
    #                 'id': bucketlist.id,
    #                 'name': bucketlist.name,
    #                 'date_created': bucketlist.date_created,
    #                 'date_modified': bucketlist.date_modified,
    #                 'created_by': bucketlist.created_by
    #             })
    #             return make_response(response), 200
    #     else:
    #         # user is not legit, so the payload is an error message
    #         message = user_id
    #         response = {
    #             'message': message
    #         }
    #         return make_response(jsonify(response)), 401

    # import the authentication blueprint and register it on the app
    # from .auth import auth_blueprint
    # app.register_blueprint(auth_blueprint)

    return app
