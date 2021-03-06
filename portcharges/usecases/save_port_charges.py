import json

from portcharges.app.deserializing import PortChargeDeserializer


class SavePortChargesFromJSONUseCase:

    def __init__(self, currency_normalizer, charges_saver):
        self._currency_normalizer = currency_normalizer
        self._charge_deserializer = PortChargeDeserializer()
        self._charges_saver = charges_saver

    def save(self, port_charges_json: str):
        port_charges_data = json.loads(port_charges_json)
        port_charges = list(
            self._deserialize_port_charges_data(port_charges_data)
        )
        self._save_port_charges(port_charges)

    def _deserialize_port_charges_data(self, port_charges_data):
        for port_charge_data in port_charges_data:
            value = self._normalize_value(port_charge_data)
            yield self._charge_deserializer.deserialize(
                port_charge_data,
                value,
            )

    def _normalize_value(self, port_charge_data):
        currency = port_charge_data['currency']
        value = port_charge_data['value']
        if currency == 'USD':
            return value
        return self._currency_normalizer.normalize(currency, value)

    def _save_port_charges(self, port_charges):
        for port_charge in port_charges:
            self._charges_saver.save(port_charge)
