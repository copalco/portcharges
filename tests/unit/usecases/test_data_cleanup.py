import pytest

from portcharges.domain import PortCharge
from portcharges.usecases import DataCleanUpUseCase


class TestDataCleanUpUseCase:

    def test_splits_data_by_ranges_and_marks_least_populated_as_erroneus(
            self, usecase, data_updater):
        usecase.clean()
        data_updater.assert_updated(['4'])


@pytest.fixture
def usecase(data_finder, data_updater, stats_finder):
    return DataCleanUpUseCase(
        data_finder=data_finder,
        data_updater=data_updater,
        stats_finder=stats_finder,
    )


@pytest.fixture
def data_finder(port_charges):
    class FakeDataFinder:

        def find(self):
            return [{
                '_id': 'PL',
                'port_charges': port_charges,
            }]
    return FakeDataFinder()


@pytest.fixture
def data_updater():
    class SpyDataUpdater:

        def __init__(self):
            self._updated = []

        def update(self, chart_ids):
            self._updated.extend(chart_ids)

        def assert_updated(self, ids):
            assert self._updated == ids
    return SpyDataUpdater()


@pytest.fixture
def stats_finder():
    class FakeStatsFinder:
        def find(self):
            return (a for a in range(1, 3))
    return FakeStatsFinder()


@pytest.fixture
def port_charges():
    return [
        dict(
            _id='1',
            country='PL',
            city='GDA',
            supplier_id=1,
            value=10,
        ),
        dict(
            _id='2',
            country='PL',
            city='GDY',
            supplier_id=2,
            value=50,
        ),
        dict(
            _id='3',
            country='PL',
            city='GDY',
            supplier_id=1,
            value=65,
        ),
        dict(
            _id='4',
            country='PL',
            city='GDY',
            supplier_id=3,
            value=1000,
        ),
        dict(
            _id='5',
            country='PL',
            city='GDY',
            supplier_id=3,
            value=140,
        ),
        dict(
            _id='6',
            country='PL',
            city='GDY',
            supplier_id=3,
            value=250,
        ),
        dict(
            _id='7',
            country='PL',
            city='GDY',
            supplier_id=3,
            value=300,
        ),
    ]
