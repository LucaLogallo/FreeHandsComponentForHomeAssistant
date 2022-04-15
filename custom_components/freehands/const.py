"""Constants for the freehandsmiddleware integration."""

DOMAIN = "freehands"

BROKER = "192.168.3.122"
PORT = "1883"
TOPIC = "zigbee2mqtt/+"
USERNAME = "mqtt_user"
PASSWORD = "%%7!P6C6zji@VADv"
URI = "mqtt://" + USERNAME + ":" + PASSWORD + "@" + BROKER + "." + PORT


"""Constants for freeHands."""
# Base component constants
NAME = "freeHands"
DOMAIN = "freehands"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"

ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/riveccia/freehands/issues"

# Icons
ICON = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [BINARY_SENSOR, SENSOR, SWITCH]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""


Freehands = {

    "Mqtt_ip": "192.168.3.63",

    "Mqtt_port": 51885,

    "Username":"pippo",

    "Password":"pluto"

}

tenantIdentificationCode = "appforgood"
companyIdentificationCode ="appforgood_matera"
gatewayTag = "gateway_6"

Topics = [
    {
        "Topic_in" : "shellies/mqtt2shellyem_1/emeter/1/power",
        "Topic_out" : tenantIdentificationCode+"/"+companyIdentificationCode+"/"+gatewayTag+"/emeter/power/get"
    },
    {
        "Topic_in" : "shellies/mqtt2shellyem_1/emeter/0/voltage",
        "Topic_out" :  tenantIdentificationCode+"/"+companyIdentificationCode+"/"+gatewayTag+"/emeter/voltage/get"
    },
    {
        "Topic_in" : "shellies/mqtt2shellyem_1/emeter/1/total",
        "Topic_out" : tenantIdentificationCode+"/"+companyIdentificationCode+"/"+gatewayTag+"/emeter/total/get"
    },
    {
        "Topic_in" : "shellies/mqtt2shellyem_1/relay/0",
        "Topic_out" : tenantIdentificationCode+"/"+companyIdentificationCode+"/"+gatewayTag+"/emeter/status/get"
    }
]

# variabili const
# per ogni gateway servirà modificare questo documento in base al gateway sul quale si andrà a mettere
