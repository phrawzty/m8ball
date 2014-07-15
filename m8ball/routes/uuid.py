"""The views (routes)."""


from flask import abort, request
from flask.ext import restful
from flask.ext.restful import reqparse
from m8ball.util import str2bool, check_uuid
from m8ball.util.s3backend import S3Backend
from m8ball.util.authball import AuthBall


# TODO: Import the bucket names from ENV.
# Instantiate the back-end.
UUID_BACKEND = S3Backend('m8ballbucket')
# Instantiate the authball.
AUTHBALL = AuthBall({'type': 's3', 'bucket': 'm8ballapikeys'})


class Uuid(restful.Resource):

    def get(self, uuid_list):
        """Get one or more UUIDs."""

        # Parse whatever arguments may have been passed.
        args = self.__args()
        # At some we'll want to return some JSON.
        content = {}
        # Obtain a list of UUIDs (n>0).
        uuids = uuid_list.split(',')

        for uuid in uuids:
            lookup_uuid = UUID_BACKEND.get(uuid)
            if check_uuid(uuid) and lookup_uuid:
                content[uuid] = lookup_uuid
            elif str2bool(args['empty']):
                content[uuid] = ''

        return content

    def put(self, uuid_list):
        """Put one UUID."""

        # Parse whatever arguments may have been passed.
        args = self.__args()
        # At some we'll want to return some JSON.
        content = {}

        # Each PUT request needs to be authorised somehow.
        authenticated = False

        # Using an API key is one possibility, I guess.
        if args['api_key']:
            if AUTHBALL.apikey(args['api_key']):
                authenticated = True
        # There are other possibilities. This is totally up in the air.
        # Note that this is done per-request; there is currently no notion
        #   of a session. Clearly this is a WIP.

        if not authenticated:
            abort(401)

        # Only one UUID is allowed for a PUT.
        if not check_uuid(uuid_list):
            abort(400)

        # If there's no data then nothing can be inserted.
        # We may wish to validate further in real life.
        try:
            len(request.values.get('data'))
        except TypeError:
            abort(400)

        data = request.values.get('data')

        # Ok, try to set the UUID and data pair.
        if UUID_BACKEND.set(uuid_list, data, str2bool(args['clobber'])):
            content[uuid_list] = data

        return content

    def __args(self):
        """Arguments specific to this endpoint."""

        parser = reqparse.RequestParser()

        parser.add_argument(
            name='empty',
            default='false',
            help="'empty': Return empty values?",
            choices=['true', 'false'],
            case_sensitive=False
        )

        parser.add_argument(
            name='clobber',
            default='false',
            help="'clobber': Overwrite existing UUID during PUT?",
            choices=['true', 'false'],
            case_sensitive=False
        )

        parser.add_argument(
            name='api_key',
            help="'api_key': API key (for PUTting)."
        )

        args = parser.parse_args()

        return args
