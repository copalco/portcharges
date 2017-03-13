class CountryStats:

    def __init__(
            self,
            country: str,
            currency: str,
            average: float,
            min_value: float,
            max_value: float,
            valid_count: int,
            outline_count: int):
        self.country = country
        self.currency = currency
        self.average = average
        self.min_value = min_value
        self.max_value = max_value
        self.valid_count = valid_count
        self.outline_count = outline_count

    def __repr__(self):
        return (
            '{self.__class__.__name__}'
            '(country={self.country!r},'
            ' currency={self.currency!r},'
            ' average={self.average!r},'
            ' min_value={self.min_value!r},'
            ' max_value={self.max_value!r},'
            ' valid_count={self.valid_count!r},'
            ' outline_count={self.outline_count!r})'
        ).format(self=self)

    def __eq__(self, other):
        if not self.__class__ == other.__class__:
            return NotImplemented
        return all((
            self.country == other.country,
            self.currency == other.currency,
            self.average == other.average,
            self.min_value == other.min_value,
            self.max_value == other.max_value,
            self.valid_count == other.valid_count,
            self.outline_count == other.outline_count,
        ))
