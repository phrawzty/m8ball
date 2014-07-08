"""Insert docstring here."""


from flask import json


class PretendBackend(object):
    """Pretend this is a k/v back-end."""

    def __init__(self, filename):
        """Init. You know."""

        with open(filename, 'r') as json_file:
            self.data = json.load(json_file)

    def get(self, key):
        """Get a key."""

        if key in self.data:
            return self.data[key]
        else:
            return False

    def set(self, key, val, clobber=False):
        """Set a key."""

        if key not in self.data:
            self.data[key] = val
            return True
        elif key in self.data and clobber:
            self.data[key] = val
            return True

        return False
