from portcharges.app import CurrencyNormalizer


def setup(container):
    container.add_service(
        normalizer,
        'app.currency_normalizer',
    )


def normalizer(container):
    return CurrencyNormalizer(
        exchange_rates_provider=container('gateways.exchange_rate_provider'),
    )
