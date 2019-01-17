from flask import Blueprint, request
from flask_restful import Resource, Api, url_for, reqparse, fields, inputs


MODULE_PATH = 'resources.todos'
NAMESPACE = __name__


# FOR PARSING OUTPUT (USED BY MARSHAL)
todo_fields = {
    'name': fields.String,
    'complete': fields.Boolean,
    'edited': fields.Boolean,
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

        return [
            {'name': 'to_do_item_1'},
            {'name': 'to_do_item_2'},
            {'name': 'to_do_item_3'},
            {'name': 'to_do_item_4'}
        ]

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


        response_body = {
            'name': 'some fucking bullshit',
            'complete': True,
            'edited': False
        }
        status_code = 201
        additional_headers = {
            'Location': url_for('resources.todos.todo', id=1)
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