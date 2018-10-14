from flask_restplus import Resource, Namespace

ns = Namespace('test', path='/test')


@ns.route('/')
class Test(Resource):
    def get(self):
        return {'hello': 'world'}