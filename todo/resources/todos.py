from flask import Blueprint, request
from flask_restful import (Resource, Api, url_for, reqparse, fields, inputs,
                           marshal, marshal_with)

import models


MODULE_PATH = 'resources.todos'
NAMESPACE = __name__


VERBOSE = True


# FOR PARSING OUTPUT (USED BY MARSHAL)
todo_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'completed': fields.Boolean,
}


# Helper Functions
# ----------------
def set_reqparser():
    """The nature of this API is such that both List and Item resources
    will need to handle `name`, and `completed` fields[note1]. Therefore,
    we can centralise the parser definition and just call it in each
    resource's initialiser.

    [note1]:  we don't need to do anything with `edited` because every request 
    either persists to the database (thus clearing the edited flag) or reads 
    from the database (i.e., loads a saved state)). 
    """

    parser = reqparse.RequestParser()

    # Define the input arguments that can be parsed by by reqparse
    # and any validation
    #
    # We can supply a default value `default=<value>`
    #
    # Every argument we add to reqparse will be validated by
    # reqparse and returned when calling `parse_args`.
    # we don't need to add a validator for every argument in the input
    # JSON, just those that we want to be able to access with `parse_args`
    parser.add_argument(
        'name',
        required=True,
        help='No todo name provided',
        location=['form', 'json']
    )
    parser.add_argument(
        'completed',
        required=False,
        help='Invalid value for complete',
        type=inputs.boolean,
        location=['form', 'json'],
        default=False
    )
    return parser


# Resource Classes
# ----------------
class ToDoList(Resource):

    def __init__(self):
        self.reqparse = set_reqparser()

    def get(self):
        todos = models.Todo.select()

        response_body = [marshal(todo, todo_fields) for todo in todos]

        return response_body

    def post(self):

        # parse_args() will give us the args that were validated.
        # Thus if there are input arguments in the JSON that we receive
        # but don't care about, we can just not parse them
        pkwargs = self.reqparse.parse_args()
        if VERBOSE:
            print("==== DEBUG POST (reqparse) ====")
            for key, value in pkwargs.items():
                print(f'key: {key}')
                print(type(key))

                print(f'value: {value}')
                print(type(value))
            print("==== END DEBUG POST (reqparse) ====")

        # create the corresponding DB entry and return it
        todo = models.Todo.create(**pkwargs)

        # use marshal to convert the peewee model instance into a 
        # data structure that is JSONable.
        #
        # when used directly marshal takes:
        # - the data object
        # - the mapping dictionary
        # - (optionally) an envelope
        #
        # The mapping dictionary describes the types that will be in the
        # final output, not necessarily the actual types in the data
        # object.
        # Examples:
        # data     | mapped type | output value
        # ---------|-------------|--------------
        # b'hello' | str         | "b'hello'"
        # r'hello' | str         | "hello"
        # 0        | bool        | False
        # 17       | bool        | True
        # 3.14159  | int         | 3
        #
        # Any values in the data object with no corresponding mapping will be
        # omitted from the output.
        # Any missing values in the data object that have mappings will be
        # returned as None.
        # If passed an iterable, marshal will operate on each element in the
        # iterable and returning a list of OrderedDicts
        #
        # when used as a decorator (`marshal_with`), marshal works the same
        # way except that if the decorated function returns a tuple, only
        # the first element in the tuple will be marshalled, the rest of the
        # tuple will be passed through unchanged.
        response_body = marshal(todo, todo_fields)
        status_code = 201
        additional_headers = {
            'Location': url_for('resources.todos.todo', id=todo.id)
        }

        return (response_body, status_code, additional_headers)


class ToDo(Resource):
    def __init__(self):
        self.reqparse = set_reqparser()

    @marshal_with(todo_fields)
    def put(self, id):
        pkwargs = self.reqparse.parse_args()

        # .update() returns a query not a model object
        query = models.Todo.update(**pkwargs).where(models.Todo.id==id)
        query.execute()

        # now we have to actually get the model
        response_body = models.Todo.get(models.Todo.id==id)
        status_code = 200
        additional_headers = {
            'Location': url_for('resources.todos.todos')
        }
        
        return (response_body, status_code, additional_headers)

    def delete(self, id):

        # .delete() returns a query not a model object
        query = models.Todo.delete().where(models.Todo.id==id)
        query.execute()

        response_body = ''
        status_code = 204  # (no content)
        additional_headers = {
            'Location': url_for('resources.todos.todos')
        }

        response = (
            response_body,
            status_code,
            additional_headers
        )

        return response


todos_api = Blueprint(MODULE_PATH, NAMESPACE)
api = Api(todos_api)


api.add_resource(
    ToDoList,
    '/todos',
    endpoint='todos'
)
api.add_resource(
    ToDo,
    '/todos/<int:id>',
    endpoint='todo'
)