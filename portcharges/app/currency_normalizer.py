class CurrencyNormalizer:

    def __init__(self, exchange_rates_provider):
        self._exchange_rates_provider = exchange_rates_provider

    def normalize(self, currency: str, value: float) -> float:
        exchange_rate = self._exchange_rates_provider.get_rates(currency)
        return round(value / exchange_rate, 2)
