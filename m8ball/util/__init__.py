"""Some handy internal utils."""


import re
from os import environ


def str2bool(string):
    """Given a boolean-style string, return True/False; defaults to False."""

    try:
        return string.lower() in ['yes', 'true', 'ok', '1']
    except AttributeError:
        return False


def check_uuid(string):
    """Determine if a given string is a UUID."""

    # Set up the UUID regex.
    re_uuid = re.compile(
        r'^(?:bp-)?[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}$', re.I
    )

    return re_uuid.match(string)


def parse_env():
    """Extract potential config options from env."""

    m8_env = {}

    # All runtime args must be prefixed my 'M8_'.
    for key in environ:
        if key.startswith('M8_'):
            # Drop the prefix for internal assignment.
            m8_env[key.split('M8_')[1]] = environ[key]

    return m8_env
