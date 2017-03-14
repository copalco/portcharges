import datetime

import pytest

from portcharges.gateways import ExchangeRateProvider


class TestExchangeRatesProvider:

    def test_gets_exchange_rate_to_usd_for_specified_currency(self, provider):
        assert provider.get_rates('CNY') == 6.9133

    def test_called_once_a_day(self, provider, session):
        provider.get_rates('CNY')
        provider.get_rates('CNY')
        session.assert_called_once()

    def test_called_again_if_day_passes(
            self, provider, date_provider, session):
        provider.get_rates('CNY')
        date_provider.increment_date()
        provider.get_rates('CNY')
        session.assert_called_twice()


@pytest.fixture
def provider(date_provider, session):
    return ExchangeRateProvider(date_provider=date_provider, session=session)


@pytest.fixture
def date_provider():
    class FakeDateProvider:

        def __init__(self):
            self._date = datetime.date(2017, 3, 13)

        def __call__(self):
            return self._date

        def increment_date(self):
            self._date = self._date + datetime.timedelta(days=1)
    return FakeDateProvider()


@pytest.fixture
def session():
    class Response:

        def json(self):
            return {
                'base': 'USD',
                'date': '2017-03-13',
                'rates': {
                    'AUD': 1.3203,
                    'BGN': 1.8342,
                    'BRL': 3.1519,
                    'CNY': 6.9133,
                }
            }

    class SpyHTTPSession:

        def __init__(self):
            self._calls = 0

        def get(self, url):
            self._calls += 1
            return Response()

        def assert_called_once(self):
            assert self._calls == 1

        def assert_called_twice(self):
            assert self._calls == 2

    return SpyHTTPSession()
