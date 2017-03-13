from portcharges.domain import PortCharge


class PortChargeDeserializer:

    def deserialize(self, port_charge_dict: dict) -> PortCharge:
        country = self._extract_country(port_charge_dict)
        city = self._extract_city(port_charge_dict)
        return PortCharge(
            id=None,
            country=country,
            city=city,
            supplier_id=port_charge_dict['supplier_id'],
            currency=port_charge_dict['currency'],
            value=port_charge_dict['value'],
        )

    def _extract_country(self, port_charge_dict):
        return port_charge_dict['port'][:2]

    def _extract_city(self, port_charge_dict):
        return port_charge_dict['port'][2:]
