"""
Abstraction class for authentication.

Really not sure how to best implement this; actually, not even sure that
it's a good idea, but we'll roll with it for now.
"""


from m8ball.util.pretendbackend import PretendBackend
from m8ball.util.s3backend import S3Backend


class AuthBall(object):
    """This is experimental and may be eliminated entirely."""

    def __init__(self, **kwargs):
        """Init the AuthBall!"""

        # Basic sanity checking.
        backs = ['pretend', 's3']

        try:
            assert kwargs['type']
            assert kwargs['type'] in backs
        except KeyError:
            raise KeyError('Must specify "type" of back-end.')
        except AssertionError:
            raise ValueError('Back-end type must be one of %s ' % types)

        try:
            assert kwargs['source']
        except KeyError:
            raise KeyError('Must specify "source" for back-end.')

        if kwargs['type'] == 'pretend':
            self.backend = PretendBackend(kwargs['source'])

        if kwargs['type'] == 's3':
            self.backend = S3Backend(**kwargs)

    def apikey(self, api_key):
        """Simple key passed as string in plaintext."""

        if self.backend.get(api_key):
            return True
        else:
            return False
