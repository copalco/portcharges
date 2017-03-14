import knot

from . import config
from . import containers


class CreateApp:

    def create(self, config_path):
        settings = config.read_ini(config_path)
        container = knot.Container(settings)
        containers.setup(container)
        return container('app')
