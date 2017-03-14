from . import app
from . import gateways
from . import mongo
from . import usecases


def setup(container):
    app.setup(container)
    gateways.setup(container)
    mongo.setup(container)
    usecases.setup(container)
