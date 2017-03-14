import copy

import pytest

from portcharges.domain import PortCharge

ID = 'test_id'
COUNTRY = 'NO'
CITY = 'OSL'
SUPPLIER_ID = 1
VALUE = 3567.34


class TestPortChargeInit:

    def test_sets_attributes_from_data(self, port_charge):
        assert port_charge.id == ID
        assert port_charge.country == COUNTRY
        assert port_charge.city == CITY
        assert port_charge.supplier_id == SUPPLIER_ID
        assert port_charge.value == VALUE


class TestPortChargeRepr:

    def test_returns_class_name_with_attributes(self, port_charge):
        assert repr(port_charge) == (
            "PortCharge"
            "(id='{}',"
            " country='{}',"
            " city='{}',"
            " supplier_id={},"
            " value={})"
        ).format(ID, COUNTRY, CITY, SUPPLIER_ID, VALUE)


class TestPortChargeEquality:

    def test_port_charge_equal_if_data_equal(self, port_charge):
        assert port_charge == PortCharge(
            id=ID,
            country=COUNTRY,
            city=CITY,
            supplier_id=SUPPLIER_ID,
            value=VALUE,
        )

    @pytest.mark.parametrize(
        'attribute, value',
        (
            ('id', None),
            ('country', 'PL'),
            ('city', 'GDA'),
            ('supplier_id', 999),
            ('value', 2000.00),
        ),
    )
    def test_not_equal_if_data_differs(self, port_charge, attribute, value):
        other_port_charge = copy.copy(port_charge)
        setattr(other_port_charge, attribute, value)
        assert port_charge != other_port_charge

    def test_does_not_try_to_compare_if_of_different_type(self, port_charge):
        assert port_charge != []


@pytest.fixture
def port_charge():
    return PortCharge(
        id=ID,
        country=COUNTRY,
        city=CITY,
        supplier_id=SUPPLIER_ID,
        value=VALUE,
    )
