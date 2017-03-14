import json

import pytest

from portcharges.domain import PortCharge
from portcharges.usecases import SavePortChargesFromJSONUseCase


class TestSavePortChargesFromJSONUseCase:

    def test_saves_port_charges_from_json(
            self, usecase, json_data, saver, port_charges):
        usecase.save(json_data)
        saver.assert_charges_saved(port_charges)


@pytest.fixture
def usecase(currency_normalizer, saver):
    return SavePortChargesFromJSONUseCase(
        currency_normalizer=currency_normalizer,
        charges_saver=saver,
    )


@pytest.fixture
def json_data():
    return json.dumps([
        {
            "currency": "CNY",
            "supplier_id": 35,
            "port": "CNAQG",
            "value": 820.0,
        },
        {
            "currency": "CNY",
            "supplier_id": 19,
            "port": "CNAQG",
            "value": 835.0,
        },
        {
            "currency": "CNY",
            "supplier_id": 49,
            "port": "CNAQG",
            "value": 600.0,
        },
        {
            "currency": "CNY",
            "supplier_id": 54,
            "port": "CNAQG",
            "value": 775.0,
        },
    ])


@pytest.fixture
def currency_normalizer():
    class FakeCurrencyNormalizer:

        def normalize(self, currency, value):
            return round(value / 6.9133, 2)
    return FakeCurrencyNormalizer()


@pytest.fixture
def saver():
    class SpySaver:

        def __init__(self):
            self.charges = []

        def save(self, charge):
            self.charges.append(charge)

        def assert_charges_saved(self, charges):
            assert self.charges == charges
    return SpySaver()


@pytest.fixture
def port_charges():
    return [
        PortCharge(
            id=None,
            country="CN",
            city="AQG",
            supplier_id=35,
            value=118.61,
        ),
        PortCharge(
            id=None,
            country="CN",
            city="AQG",
            supplier_id=19,
            value=120.78,
        ),
        PortCharge(
            id=None,
            country="CN",
            city="AQG",
            supplier_id=49,
            value=86.79,
        ),
        PortCharge(
            id=None,
            country="CN",
            city="AQG",
            supplier_id=54,
            value=112.10,
        ),
    ]
