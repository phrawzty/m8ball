"""Insert docstring here."""


from boto.s3.connection import S3Connection, OrdinaryCallingFormat
from boto.s3.key import Key
from boto.exception import S3ResponseError


class S3Backend(object):
    """This is a simple abstration layer to S3 (boto)."""

    def __init__(self, **kwargs):
        """Set up the S3 connection."""

        # Basic sanity checking.
        needs = ['access', 'secret', 'source']
        for need in needs:
            try:
                assert kwargs[need]
            except KeyError:
                raise KeyError('Must specify %s for S3Backend' % need)

        # We might be using a mock S3.
        if kwargs['port'] and kwargs['host']:
            conn = S3Connection(kwargs['access'], kwargs['secret'],
                is_secure=False, calling_format=OrdinaryCallingFormat(),
                port=int(kwargs['port']), host=kwargs['host'])
        else:
            conn = S3Connection(kwargs['access'], kwargs['secret'])

        self.bucket = conn.get_bucket(kwargs['source'])
        self.k = Key(self.bucket)

    def get(self, key):
        """Get a key."""

        self.k.key = key

        try:
            value = self.k.get_contents_as_string()
        except S3ResponseError:
            return False

        return value

    def set(self, key, value, clobber=False):
        """Set a key."""

        self.k.key = key

        exists = self.get(key)

        if (exists and clobber) or (not exists):
            return self.k.set_contents_from_string(value)
        else:
            return False
