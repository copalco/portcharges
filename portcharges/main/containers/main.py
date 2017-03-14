from . import mongo
from . import usecases


def setup(container):
    mongo.setup(container)
    usecases.setup(container)
