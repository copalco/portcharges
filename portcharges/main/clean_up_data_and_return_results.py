import sys
import knot

from portcharges.main import config
from portcharges.main import containers


def create_save_usecase(config_path):
    settings = config.read_ini(config_path)
    container = knot.Container(settings=settings)
    containers.setup(container)
    return container('usecases.clean_up_and_results')


if __name__ == '__main__':
    config_path = sys.argv[1]
    usecase = create_save_usecase(config_path)
    results = usecase.clean()
    print(results)
