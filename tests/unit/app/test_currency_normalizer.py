import pytest

from portcharges.app import CurrencyNormalizer

CURRENCY = 'CNY'
VALUE = 790.00


class TestCurrencyNormalizer:

    def test_normalizes_currency_to_usd(self, normalizer):
        assert normalizer.normalize(CURRENCY, VALUE) == 114.27


@pytest.fixture
def normalizer(exchange_rates_provider):
    return CurrencyNormalizer(
        exchange_rates_provider=exchange_rates_provider,
    )


@pytest.fixture
def exchange_rates_provider():
    class FakeExchangeRatesProvider:

        def get_rates(self, currency):
            return 6.9133
    return FakeExchangeRatesProvider()
