import os
from m8ball import app
from m8ball.util import str2bool


# Boto requires credentials.
if not (os.environ.get('AWS_ACCESS_KEY_ID')
    and os.environ.get('AWS_SECRET_ACCESS_KEY')):
    print 'Need AWS credentials.'
    exit(1)

# Set the M8_DEBUG environment variable to true for debug mode.
app.run(debug=str2bool(os.environ.get('M8_DEBUG', 'false')))
