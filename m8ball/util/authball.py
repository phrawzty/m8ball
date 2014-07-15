"""
Abstraction class for authentication.

Really not sure how to best implement this; actually, not even sure that
it's a good idea, but we'll roll with it for now.
"""


from m8ball.util.pretendbackend import PretendBackend
from m8ball.util.s3backend import S3Backend


class AuthBall(object):
    """This is experimental and may be eliminated entirely."""

    def __init__(self, back):
        """Init the AuthBall!"""

        self.backend = False

        # Sanity checking.
        backs = ['pretend', 's3']

        try:
            assert back['type']
            assert back['type'] in backs
        except KeyError:
            raise KeyError('Must specify "type" of back-end.')
        except AssertionError:
            raise ValueError('Back-end type must be one of %s ' % types)

        if back['type'] == 'pretend':
            try:
                assert back['file']
            except KeyError:
                raise KeyError('Pretend back-end requires "file" source.')

            self.backend = PretendBackend(back['file'])

        if back['type'] == 's3':
            try:
                assert back['bucket']
            except KeyError:
                raise KeyError('S3 requires a "bucket" source.')

            self.backend = S3Backend(back['bucket'])

    def apikey(self, api_key):
        """Simple key passed as string in plaintext."""

        if self.backend.get(api_key):
            return True
        else:
            return False
