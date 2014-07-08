"""Insert docstring here."""


from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException


def makejsonapp(import_name, **kwargs):
    """
    Ensure all internally generated responses (i.e: errors) are output as JSON.
    http://flask.pocoo.org/snippets/83/
    """

    def make_json_error(ex):
        response = jsonify(message=str(ex))
        response.status_code = (ex.code
            if isinstance(ex, HTTPException)
            else 500)
        return response

    app = Flask(import_name, **kwargs)

    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = make_json_error

    return app
