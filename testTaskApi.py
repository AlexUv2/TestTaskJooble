from main import db, app, Links
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
import datetime

api = Api(app)

link_put_args = reqparse.RequestParser()
link_put_args.add_argument('id', type=int, help='id doesn\'t allowed')
link_put_args.add_argument('full_url', type=str, help='full url required', required=True)
link_put_args.add_argument('short_url', type=str, help='short url doesn\'t exist')
link_put_args.add_argument('create_time', type=datetime, help='created time')  # Просто добавили аргументы в request parser
link_put_args.add_argument('time_life', type=int, help='lifetime', required=True)

link_update_args = reqparse.RequestParser()
link_update_args.add_argument('full_url', type=str, help='full url require8d7')
link_update_args.add_argument('short_url', type=str, help='short url doesn\'t exist')
link_update_args.add_argument('create_time', type=datetime, help='created time')  # Просто добавили аргументы в request parser
link_update_args.add_argument('time_life', type=int, help='lifetime')


videos = {}

resource_fields = {
    'id': fields.String,
    'full_url': fields.String,
    'short_url': fields.String,
    'create_time': fields.DateTime,
    'time_life': fields.Integer
}


class URL(Resource):
    """For all requests returns one object"""
    @marshal_with(resource_fields)
    def get(self, url_id):
        result = Links.query.filter_by(id=url_id).first()
        if not result:
            abort(404, message='Couldn\'t find link with that ID')

        return result

    @marshal_with(resource_fields)
    def put(self, url_id):
        result = Links.query.filter_by(id=url_id).first()
        args = link_put_args.parse_args()  # args gets all arguments from link_put_args
        if result:
            abort(409, message='link id taken')
        link = Links(id=url_id, full_url=args['full_url'], time_life=args['time_life'])

        db.session.add(link)
        db.session.commit()

        return link, 201

    @marshal_with(resource_fields)
    def patch(self, url_id):
        args = link_update_args.parse_args()
        result = Links.query.filter_by(id=url_id).first()
        if not result:
            abort(409, message='link doesn\'t exist, can\'t update')

        if args['full_url']:
            result.full_url = args['full_url']
        if args['short_url']:
            result.short_url = args['short_url']
        if args['time_life']:
            result.time_life = args['time_life']

        db.session.add(result)
        db.session.commit()

        return result

    def delete(self, url_id):
        result = Links.query.get(url_id)
        db.session.delete(result)
        db.session.commit()

        return '', 204


class URLs(Resource):

    @marshal_with(resource_fields)
    def get(self):
        result = Links.query.order_by(Links.create_time.desc()).all()
        if not result:
            abort(404, message='Couldn\'t find any links')

        return result


api.add_resource(URL, "/links/api/<int:url_id>")
api.add_resource(URLs, "/links/api")


if __name__ == '__main__':
    app.run(debug=True)
