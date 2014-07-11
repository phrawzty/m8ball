"""Insert docstring here."""


from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.exception import S3ResponseError


class S3Backend(object):
    """This is a simple abstration layer to S3 (boto)."""

    def __init__(self):
        conn = S3Connection()
        # TODO: Make the bucket name a runtime config.
        self.bucket = conn.get_bucket('m8ballbucket')
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
