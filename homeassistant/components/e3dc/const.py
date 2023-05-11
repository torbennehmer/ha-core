"""Constants for the E3DC Remote Storage Control Protocol integration."""

from datetime import timedelta

from homeassistant.const import Platform

# Basic consts for various names
DOMAIN = "e3dc"
ERROR_AUTH_INVALID = "invalid_auth"
ERROR_CANNOT_CONNECT = "cannot_connect"
SERVICE_CLEAR_POWER_LIMITS = "clear_power_limits"
SERVICE_SET_POWER_LIMITS = "set_power_limits"

# Configuration Keys
CONF_RSCPKEY = "rscpkey"
CONF_VERSION = 1

# Parameters for integration setup
DEFAULT_SCAN_INTERVAL = timedelta(seconds=10)
PLATFORMS: list[Platform] = [
    Platform.BINARY_SENSOR,
    Platform.SENSOR,
    Platform.SWITCH,
]
