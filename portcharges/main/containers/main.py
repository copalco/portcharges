from . import gateways
from . import mongo
from . import usecases


def setup(container):
    gateways.setup(container)
    mongo.setup(container)
    usecases.setup(container)
