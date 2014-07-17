from flask.ext import restful
from m8ball.util import parse_env
from m8ball.util.makejsonapp import makejsonapp
from m8ball.routes.base import Base
from m8ball.routes.uuid import Uuid


# Convert internally-generated responses (errors) into JSON.
app = makejsonapp(__name__)

# Nab the config from the environment.
config = parse_env()
app.config.update(config)

# Continue at a restful pace.
api = restful.Api(app)

# Add the routes.
api.add_resource(Base, '/')
api.add_resource(Uuid, '/uuid/<string:uuid_list>')
