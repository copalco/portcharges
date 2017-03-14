from portcharges.usecases import SavePortChargesFromJSONUseCase
from portcharges.usecases import DataCleanUpUseCase


def setup(container):
    container.add_service(
        save_charges_usecase,
        'usecases.save_charges_from_json',
    )
    container.add_service(
        clean_up_data_usecase,
        'usecases.clean_up_and_results',
    )


def save_charges_usecase(container):
    return SavePortChargesFromJSONUseCase(
        currency_normalizer=container('app.currency_normalizer'),
        charges_saver=container('gateway.port_charge.saver'),
    )


def clean_up_data_usecase(container):
    return DataCleanUpUseCase(
        data_finder=container('mongo.port_charges.finder'),
        data_updater=container('mongo.port_charges.updater'),
        stats_finder=container('mongo.port_charges.stats'),
    )
