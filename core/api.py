from flask import jsonify, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy.exc import IntegrityError
from webargs import fields, validate, ValidationError
from webargs.flaskparser import use_args
import re, traceback

from app import app, db
from models import Asset
from helpers import make_error

api = Api(app)

def validate_asset(args):
    asset_type = args['type']
    asset_class = args['class']
    valid_input = asset_type == 'satellite' and (asset_class in ['dove','rapideye'])
    valid_input = valid_input or (asset_type == 'antenna' and (asset_class in ['dish','yagi']))
    if not valid_input:
        raise ValidationError("Args is incorrect. type: %s, class: %s" %  (asset_type, asset_class))

def validate_asset_name(asset_name):
    if not (4 <= len(asset_name) <= 64):
        raise ValidationError("Asset name is out of range. (Only between 4 to 64 characters allowed)")
    if not bool(re.search("^[^_^-][a-zA-Z_-]*$", asset_name)):
        raise ValidationError("Asset name only accepts alphanumeric characters, underscores, or dashes. It also cannot begin with an underscore or dash.")

asset_args = {
    'type': fields.Str(required=True),
    'class': fields.Str(required=True),
    'asset_name': fields.Str(required=True, validate=validate_asset_name)
}

class AssetResource(Resource):

    def get(self, asset_name):
        # abort_if_todo_doesnt_exist(todo_id)
        asset = Asset.query.filter(Asset.name == asset_name).first()
        if asset:
            return jsonify(message="success",data=asset.serialize())
        else:
            response = jsonify(message="asset not found.")
            response.status_code = 404
            return response

    @use_args(asset_args, locations=('form','view_args'),validate=validate_asset)
    def post(self, args, asset_name):
        asset = Asset(asset_name, args['type'], args['class'])
        db.session.add(asset)
        try:
            db.session.commit()
            return jsonify(message="success",data=asset.serialize())
        except IntegrityError as e:
            traceback.print_exc() # there are better ways to handle logging than just printing to the console
            return make_error(409, "database error occurred. asset not created.") # we would not want to publicly show the full stack trace. for now, do a simple message

class AssetsResource(Resource):
    def get(self):
        return jsonify(message="success",data = [asset.serialize() for asset in Asset.query.all()])

api.add_resource(AssetsResource, '/assets')
api.add_resource(AssetResource, '/asset/<asset_name>')
