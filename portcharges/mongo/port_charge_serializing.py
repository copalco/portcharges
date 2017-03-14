from portcharges.domain import PortCharge


class PortChargeSerializer:

    def serialize(self, port_charge: PortCharge) -> dict:
        return {
            'country': port_charge.country,
            'city': port_charge.city,
            'supplier_id': port_charge.supplier_id,
            'currency': port_charge.currency,
            'value': port_charge.value,
        }
