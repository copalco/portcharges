import copy

import pytest

from portcharges.domain import CountryStats

COUNTRY = 'NO'
CURRENCY = 'EUR'
AVERAGE = 3000.00
MIN_VALUE = 1500.00
MAX_VALUE = 4500.00
VALID_COUNT = 100
OUTLINE_COUNT = 13


class TestCountryStatsInit:

    def test_sets_attributes_from_data(self, country_stats):
        assert country_stats.country == COUNTRY
        assert country_stats.currency == CURRENCY
        assert country_stats.average == AVERAGE
        assert country_stats.min_value == MIN_VALUE
        assert country_stats.max_value == MAX_VALUE
        assert country_stats.valid_count == VALID_COUNT
        assert country_stats.outline_count == OUTLINE_COUNT


class TestCountryStatsRepr:

    def test_returns_class_name_with_attributes(self, country_stats):
        assert repr(country_stats) == (
            "CountryStats"
            "(country='{}',"
            " currency='{}',"
            " average={},"
            " min_value={},"
            " max_value={},"
            " valid_count={},"
            " outline_count={})"
        ).format(
            COUNTRY,
            CURRENCY,
            AVERAGE,
            MIN_VALUE,
            MAX_VALUE,
            VALID_COUNT,
            OUTLINE_COUNT,
        )


class TestCountryStatsEquality:

    def test_portrate_equal_if_data_equal(self, country_stats):
        assert country_stats == CountryStats(
            country=COUNTRY,
            currency=CURRENCY,
            average=AVERAGE,
            min_value=MIN_VALUE,
            max_value=MAX_VALUE,
            valid_count=VALID_COUNT,
            outline_count=OUTLINE_COUNT,
        )

    @pytest.mark.parametrize(
        'attribute, average',
        (
            ('country', 'PL'),
            ('currency', 'PLN'),
            ('average', 2000.00),
            ('min_value', 100.00),
            ('max_value', 10000.00),
            ('valid_count', 0),
            ('outline_count', 0),
        ),
    )
    def test_not_equal_if_data_differs(
            self, country_stats, attribute, average):
        other_portrate = copy.copy(country_stats)
        setattr(other_portrate, attribute, average)
        assert country_stats != other_portrate

    def test_does_not_try_to_compare_if_of_different_type(
            self, country_stats):
        assert country_stats != []


@pytest.fixture
def country_stats():
    return CountryStats(
        country=COUNTRY,
        currency=CURRENCY,
        average=AVERAGE,
        min_value=MIN_VALUE,
        max_value=MAX_VALUE,
        valid_count=VALID_COUNT,
        outline_count=OUTLINE_COUNT,
    )
