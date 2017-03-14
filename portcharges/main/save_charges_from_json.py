import sys
import knot

from portcharges.main import config
from portcharges.main import containers


def create_save_usecase(config_path):
    settings = config.read_ini(config_path)
    container = knot.Container(settings=settings)
    containers.setup(container)
    return container('usecases.save_charges_from_json')


if __name__ == '__main__':
    config_path = sys.argv[1]
    with open(sys.argv[2]) as data_file:
        data = data_file.read()
    usecase = create_save_usecase(config_path)
    usecase.save(data)
