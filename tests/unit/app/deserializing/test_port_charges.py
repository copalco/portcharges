import pytest

from portcharges.app.deserializing import PortChargeDeserializer
from portcharges.domain import PortCharge


class TestPortChargeDeserializer:

    def test_deserializes_from_dict_to_port_charge_object(
            self, deserializer, port_charge_json, port_charge):
        assert deserializer.deserialize(port_charge_json) == port_charge


@pytest.fixture
def deserializer():
    return PortChargeDeserializer()


@pytest.fixture
def port_charge_json():
    return {
        'currency': 'CNY',
        'supplier_id': 35,
        'port': 'CNAQG',
        'value': 820.0
    }


@pytest.fixture
def port_charge():
    return PortCharge(
        id=None,
        country='CN',
        city='AQG',
        supplier_id=35,
        currency='CNY',
        value=820.0,
    )
