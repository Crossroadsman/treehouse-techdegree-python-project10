from flask import Blueprint, request
from flask_restful import (Resource, Api, url_for, reqparse, fields, inputs,
                           marshal)

import models


MODULE_PATH = 'resources.todos'
NAMESPACE = __name__


# FOR PARSING OUTPUT (USED BY MARSHAL)
todo_fields = {
    'id': fields.Integer,
    'name': fields.String,
    #'complete': fields.Boolean,
    #'edited': fields.Boolean,
}

class ToDoList(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        # Define the input arguments that can be parsed by by reqparse
        # and any validation
        #
        # We can supply a default value `default=<value>`
        self.reqparse.add_argument(
            'name',
            required=True,
            help='No todo name provided',
            location=['form', 'json']
        )
        # every argument we add to reqparse will be validated by
        # reqparse and returned when calling `parse_args`.
        # we don't need to add a validator for every argument in the input
        # JSON, just those that we want to be able to access with `parse_args`
        #
        # We might want these later, so they are left for now.
        '''
        self.reqparse.add_argument(
            'complete',
            required=False,
            help='Invalid value for complete',
            type=inputs.boolean,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'edited',
            required=False,
            help='Invalid value for edited',
            type=inputs.boolean,
            location=['form', 'json']
        )
        '''

    def get(self):
        todos = models.Todo.select()

        response_body = [marshal(todo, todo_fields) for todo in todos]

        print(response_body)
        return response_body

    def post(self):

        # parse_args() will give us the args that were validated.
        # Thus if there are input arguments in the JSON that we receive
        # but don't care about, we can just not parse them
        pkwargs = self.reqparse.parse_args()
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

    def delete(self):

        # we can get access to the request through Flask's request context
        # by importing `flask.request`
        #
        # Once we have it, we can drill into it
        if request:
            print("==== DEBUG DELETE (request)====")
            print(request)
            print(type(request))
            print(dir(request))
            for att in [
                request.base_url,
                request.content_encoding,
                request.content_type,
                request.data,
                request.endpoint,
                request.files,
                request.form,
                request.full_path,
                request.get_data(),
                request.get_json(force=True),
                request.json,
                request.headers,
                request.host,
                request.host_url,
                request.method,
                request.path,
                request.query_string,
                request.remote_addr,
                request.url,
                request.url_root
            ]:
                print(att)
                print(type(att))
            print("==== END DEBUG DELETE (request)====")

        id = ''
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

class ToDo(Resource):

    def delete(self, id):

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
    '/todos/<id>',
    endpoint='todo'
)