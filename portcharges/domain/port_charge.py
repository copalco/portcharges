import typing


class PortCharge:

    def __init__(
            self,
            id: typing.Optional[str],
            country: str,
            city: str,
            supplier_id: int,
            value: float):
        self.id = id
        self.country = country
        self.city = city
        self.supplier_id = supplier_id
        self.value = value

    def __repr__(self):
        return (
            '{self.__class__.__name__}'
            '(id={self.id!r},'
            ' country={self.country!r},'
            ' city={self.city!r},'
            ' supplier_id={self.supplier_id!r},'
            ' value={self.value!r})'
        ).format(self=self)

    def __eq__(self, other):
        if not self.__class__ == other.__class__:
            return NotImplemented
        return all((
            self.id == other.id,
            self.country == other.country,
            self.city == other.city,
            self.supplier_id == other.supplier_id,
            self.value == other.value,
        ))
