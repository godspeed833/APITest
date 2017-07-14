from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}
        
class n(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('addr',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('count',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )    

    @jwt_required()
    def get(self, name):
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}
        
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = n.parser.parse_args()

        item = {'name': name, 'addr': data['addr'], 'count': data['count']}
        items.append(item)
        return item
        
class s(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('addr',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('count',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )    

    @jwt_required()
    def get(self, name):
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}
        
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = s.parser.parse_args()

        item = {'name': name, 'addr': data['addr'], 'count': data['count']}
        items.append(item)
        return item        
        
        

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(n, '/n/<string:name>')
api.add_resource(s, '/s/<string:name>')



if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
