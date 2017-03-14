import knot
import pytest

from portcharges.main import config
from portcharges.main import containers


@pytest.fixture
def container():
    settings = config.read_ini('tests/integration/config/test.ini')
    container = knot.Container(settings=settings)
    containers.setup(container)
    return container
