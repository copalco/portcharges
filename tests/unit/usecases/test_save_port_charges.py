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
def usecase(saver):
    return SavePortChargesFromJSONUseCase(charges_saver=saver)


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
            currency="CNY",
            supplier_id=35,
            value=820.0,
        ),
        PortCharge(
            id=None,
            country="CN",
            city="AQG",
            currency="CNY",
            supplier_id=19,
            value=835.0,
        ),
        PortCharge(
            id=None,
            country="CN",
            city="AQG",
            currency="CNY",
            supplier_id=49,
            value=600.0,
        ),
        PortCharge(
            id=None,
            country="CN",
            city="AQG",
            currency="CNY",
            supplier_id=54,
            value=775.0,
        ),
    ]
