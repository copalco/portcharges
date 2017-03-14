import pymongo

from portcharges.mongo import PortChargeSaver


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
