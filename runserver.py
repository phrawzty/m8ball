import os
from m8ball import app
from m8ball.util import str2bool


# Set the M8_DEBUG environment variable to true for debug mode.
app.run(debug=str2bool(os.environ.get('M8_DEBUG', 'false')))
