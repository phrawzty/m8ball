"""A highly useless endpoint."""


from flask.ext import restful


class Base(restful.Resource):
    def get(self):
        response = {'response': 'This is an API. :)'}
        return response
