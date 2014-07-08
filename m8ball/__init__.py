from flask.ext import restful
from m8ball.util.makejsonapp import makejsonapp
from m8ball.routes.base import Base
from m8ball.routes.uuid import Uuid


app = makejsonapp(__name__)
api = restful.Api(app)


api.add_resource(Base, '/')
api.add_resource(Uuid, '/uuid/<string:uuid_list>')
