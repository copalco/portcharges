class StatsFinder:

    def __init__(self, collection):
        self._collection = collection

    def find(self):
        return self._collection.aggregate([
            {
                '$group': {
                    '_id': '$country',
                    'valid': {'$sum': {'$cond': ['$outlier', 0, 1]}},
                    'invalid': {'$sum': {'$cond': ['$outlier', 1, 0]}},
                    'average': {'$avg': '$value'},
                    'min_value': {'$min': '$value'},
                    'max_value': {'$max': '$value'},
                },
            },
        ])
