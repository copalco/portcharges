from portcharges.domain import PortCharge

from .port_charge_serializing import PortChargeSerializer


class PortChargeSaver:

    def __init__(self, collection):
        self._port_charge_serializer = PortChargeSerializer()
        self._port_charges_collection = collection

    def save(self, port_charge: PortCharge) -> int:
        serialized_charge = self._port_charge_serializer.serialize(port_charge)
        return self._port_charges_collection.insert(serialized_charge)
