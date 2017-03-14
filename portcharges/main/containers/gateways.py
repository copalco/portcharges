import datetime

import requests

from portcharges.gateways import ExchangeRateProvider


def setup(container):
    container.add_service(
        provider,
        'gateways.exchange_rate_provider',
    )


def date_provider():
    return datetime.date.today()


def provider(container):
    return ExchangeRateProvider(
        date_provider=date_provider,
        session=requests.session(),
    )
