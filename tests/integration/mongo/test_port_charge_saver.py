import bson
import pytest

from portcharges.domain import PortCharge


class TestPortChartSaver:

    def test_saves_port_chart_to_db(self, saver, port_charges_collection):
        new_port_charge = PortCharge(
            id=None,
            country='NO',
            city='OSL',
            supplier_id=1,
            value=3567.34,
        )
        port_charge_id = saver.save(new_port_charge)
        expected_value = [
            dict(
                _id=bson.ObjectId(port_charge_id),
                country='NO',
                city='OSL',
                supplier_id=1,
                value=3567.34,
                outlier=False,
            ),
        ]
        assert list(port_charges_collection.find()) == expected_value


@pytest.fixture
def saver(container):
    return container('gateway.port_charge.saver')


@pytest.fixture
def port_charges_collection(container):
    yield container('mongo.port_charges.collection')
    container('mongo.port_charges.collection').drop()
