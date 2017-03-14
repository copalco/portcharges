class ExchangeRateProvider:

    def __init__(self, date_provider, session):
        self._date_provider = date_provider
        self._session = session
        self._rates = None
        self._rates_date = None

    def get_rates(self, currency: str) -> float:
        self._get_current_rates()
        return self._rates[currency]

    def _get_current_rates(self):
        today = self._date_provider()
        if self._rates_date == today:
            return
        response = self._session.get(
            'https://openexchangerates.org/api/latest.json'
            '?app_id=1a03277cf1ad4169bb6f081946c9405f&base=USD',
        )
        self._rates = response.json()['rates']
        self._rates_date = today
