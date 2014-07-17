"""A highly useless endpoint."""


from flask.ext import restful


class Base(restful.Resource):
    """This is the base URL which shoul return *something*."""

    def get(self):
        """Perhaps this could display version info, help text, etc."""

        response = {'response': 'This is an API. :)'}
        return response
