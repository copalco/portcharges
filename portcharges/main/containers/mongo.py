import pymongo

from portcharges.mongo import PortChargeSaver
from portcharges.mongo.data_finder import DataFinder
from portcharges.mongo.data_updater import PortChargeOutliersUpdater
from portcharges.mongo.stats_finder import StatsFinder


def setup(container):
    container.add_service(
        client,
        'mongo.client',
    )
    container.add_service(
        db,
        'mongo.db',
    )
    container.add_service(
        port_charges_collection,
        'mongo.port_charges.collection',
    )
    container.add_service(
        port_data_finder,
        'mongo.port_charges.finder',
    )
    container.add_service(
        port_data_updater,
        'mongo.port_charges.updater',
    )
    container.add_service(
        stats_finder,
        'mongo.port_charges.stats',
    )
    container.add_service(
        port_charge_saver,
        'gateway.port_charge.saver',
    )


def client(container):
    return pymongo.MongoClient(
        container['settings']['mongodb.uri'],
        connect=False,
    )


def db(container):
    return container('mongo.client').get_default_database()


def port_charges_collection(container):
    collection = container('mongo.db').port_charges
    collection.create_index('country')
    return collection


def port_charge_saver(container):
    return PortChargeSaver(
        collection=container('mongo.port_charges.collection'),
    )


def port_data_finder(container):
    return DataFinder(collection=container('mongo.port_charges.collection'))


def port_data_updater(container):
    return PortChargeOutliersUpdater(
        collection=container('mongo.port_charges.collection'),
    )


def stats_finder(container):
    return StatsFinder(
        collection=container('mongo.port_charges.collection'),
    )
