class PortChargeOutliersUpdater:

    def __init__(self, collection):
        self._port_charges_collection = collection

    def update(self, ids):
        return self._port_charges_collection.update_many(
            {'_id': {'$in': ids}}, {'$set': {'outlier': True}}
        )
