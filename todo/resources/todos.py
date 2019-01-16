from flask import Blueprint
from flask_restful import Resource, Api


MODULE_PATH = 'resources.todos'
NAMESPACE = __name__


class ToDoList(Resource):

    def get(self):
        return [
            {'name': 'to_do_item_1'},
            {'name': 'to_do_item_2'},
            {'name': 'to_do_item_3'},
            {'name': 'to_do_item_4'}
        ]


todos_api = Blueprint(MODULE_PATH, NAMESPACE)
api = Api(todos_api)


api.add_resource(
    ToDoList,
    '/todos',
    endpoint='todos'
)