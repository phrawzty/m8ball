"""
Abstraction class for authentication.

Really not sure how to best implement this; actually, not even sure that
it's a good idea, but we'll roll with it for now.
"""


from m8ball.util.pretendbackend import PretendBackend


class AuthBall(object):
    """This is experimental and may be eliminated entirely."""

    def apikey(self, api_key):
        """Simple key passed as string in plaintext."""

        backend = PretendBackend('m8ball/util/apikey_store.json')

        if api_key in backend.get('api_keys'):
            return True
        else:
            return False
