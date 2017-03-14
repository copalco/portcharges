from portcharges.usecases import SavePortChargesFromJSONUseCase


def setup(container):
    container.add_service(
        save_charges_usecase,
        'usecases.save_charges_from_json',
    )


def save_charges_usecase(container):
    return SavePortChargesFromJSONUseCase(
        charges_saver=container('gateway.port_charge.saver'),
    )
