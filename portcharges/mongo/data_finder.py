class DataFinder:

    def __init__(self, collection):
        self._collection = collection

    def find(self):
        return self._collection.aggregate([
            {
                '$group': {
                    '_id': '$country',
                    'port_charges': {'$push': "$$ROOT"}
                },
            },
        ])
