from flask_restplus import Resource, Namespace, fields, marshal_with
import app.core.item_service as service

ns = Namespace('Item', path='/item')

model = ns.model('item', {
    'id': fields.Integer,
    'name': fields.String,
    'price': fields.Float
})

@ns.route('/all')
class Item(Resource):
    @marshal_with(model, skip_none=False)
    def get(self):
        return service.query_all()