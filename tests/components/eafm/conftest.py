"""eafm fixtures."""

from asynctest import patch
import pytest


@pytest.fixture()
def mock_get_stations():
    """Mock aioeafm.get_stations."""
    with patch("homeassistant.components.eafm.config_flow.get_stations") as patched:
        yield patched


@pytest.fixture()
def mock_get_station():
    """Mock aioeafm.get_station."""
    with patch("homeassistant.components.eafm.sensor.get_station") as patched:
        yield patched