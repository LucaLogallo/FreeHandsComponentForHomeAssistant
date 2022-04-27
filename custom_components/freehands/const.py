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

################################################################################
# """Constants for the freehandsmiddleware integration."""

# DOMAIN = "freehands"

# BROKER = "192.168.3.122"
# PORT = "1883"
# TOPIC = "zigbee2mqtt/+"
# USERNAME = "mqtt_user"
# PASSWORD = "%%7!P6C6zji@VADv"
# URI = "mqtt://" + USERNAME + ":" + PASSWORD + "@" + BROKER + "." + PORT


# """Constants for freeHands."""
# # Base component constants
# NAME = "freeHands"
# DOMAIN = "freehands"
# DOMAIN_DATA = f"{DOMAIN}_data"
# VERSION = "0.0.1"

# ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
# ISSUE_URL = "https://github.com/riveccia/freehands/issues"

# # Icons
# ICON = "mdi:format-quote-close"

# # Device classes
# BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# # Platforms
# BINARY_SENSOR = "binary_sensor"
# SENSOR = "sensor"
# SWITCH = "switch"
# PLATFORMS = [BINARY_SENSOR, SENSOR, SWITCH]


# # Configuration and options
# CONF_ENABLED = "enabled"
# CONF_USERNAME = "username"
# CONF_PASSWORD = "password"

# # Defaults
# DEFAULT_NAME = DOMAIN


# STARTUP_MESSAGE = f"""
# -------------------------------------------------------------------
# {NAME}
# Version: {VERSION}
# This is a custom integration!
# If you have any issues with this you need to open an issue here:
# {ISSUE_URL}
# -------------------------------------------------------------------
# """


# Freehands = {
#     "Mqtt_ip": "192.168.3.63",
#     "Mqtt_port": 51885,
#     "Username": "pippo",
#     "Password": "pluto",
# }

# tenantIdentificationCode = "appforgood"
# companyIdentificationCode = "appforgood_matera"
# gatewayTag = "gateway_6"

# # {
# #     "Topic_in" : ",",
# #     "Topic_out" : tenantIdentificationCode+"/"+companyIdentificationCode+"/"+gatewayTag+"//get",
# #     "key":  [","]
# # }

# Topics = [
#     # AirQualitySensor_1
#     {
#         "Topic_in": "AirQualitySensor_1",
#         "Topic_out": tenantIdentificationCode
#         + "/"
#         + companyIdentificationCode
#         + "/"
#         + gatewayTag
#         + "/AirQualitySensor_1/get",
#         "key": [
#             "voc",
#             "temperature",
#             "humidity",
#             "battery",
#             "battery_low",
#             "air_quality",
#             "link_quality",
#         ],
#         "Topic_custom": [
#             {
#                 "key": "temperature",
#                 "Topic_out": tenantIdentificationCode
#                 + "/"
#                 + companyIdentificationCode
#                 + "/"
#                 + gatewayTag
#                 + "/AirQualitySensor_1/temperature/get",
#             },
#             {
#                 "key": "humidity",
#                 "Topic_out": tenantIdentificationCode
#                 + "/"
#                 + companyIdentificationCode
#                 + "/"
#                 + gatewayTag
#                 + "/AirQualitySensor_1/humidity/get",
#             },
#         ],
#     },
#     # Button_1
#     {
#         "Topic_in": "Button_1",
#         "Topic_out": tenantIdentificationCode
#         + "/"
#         + companyIdentificationCode
#         + "/"
#         + gatewayTag
#         + "/Button_1/get",
#         "key": ["battery", "link_quality"],
#     },
#     # EnergyMeter_1
#     {
#         "Topic_in": "EnergyMeter_1",
#         "Topic_out": tenantIdentificationCode
#         + "/"
#         + companyIdentificationCode
#         + "/"
#         + gatewayTag
#         + "/EnergyMeter_1/get",
#         "key": ["current_consumption", "total_consumption"],
#     },
#     # HeatAlarm_1
#     {
#         "Topic_in": "HeatAlarm_1",
#         "Topic_out": tenantIdentificationCode
#         + "/"
#         + companyIdentificationCode
#         + "/"
#         + gatewayTag
#         + "/HeatAlarm_1/get",
#         "key": [
#             "temperature",
#             "battery",
#             "smoke",
#             "battery_low",
#             "alarm",
#             "link_quality",
#         ],
#         "Topic_custom": [
#             {
#                 "key": "temperature",
#                 "Topic_out": tenantIdentificationCode
#                 + "/"
#                 + companyIdentificationCode
#                 + "/"
#                 + gatewayTag
#                 + "/HeatAlarm_1/temperature/get",
#             },
#         ],
#     },
#     # MotionSensor_1
#     {
#         "Topic_in": "MotionSensor_1",
#         "Topic_out": tenantIdentificationCode
#         + "/"
#         + companyIdentificationCode
#         + "/"
#         + gatewayTag
#         + "/MotionSensor_1/get",
#         "key": [
#             "occupancy",
#             "battery_low",
#             "tamper",
#             "temperature",
#             "illuminance_lux",
#             "link_quality",
#         ],
#         "Topic_custom": [
#             {
#                 "key": "temperature",
#                 "Topic_out": tenantIdentificationCode
#                 + "/"
#                 + companyIdentificationCode
#                 + "/"
#                 + gatewayTag
#                 + "/MotionSensor_1/temperature/get",
#             },
#             {
#                 "key": "occupancy",
#                 "Topic_out": tenantIdentificationCode
#                 + "/"
#                 + companyIdentificationCode
#                 + "/"
#                 + gatewayTag
#                 + "/MotionSensor_1/occupancy/get",
#             },
#         ],
#     },
#     # SmartLight_1
#     {
#         "Topic_in": "SmartLight_1",
#         "Topic_out": tenantIdentificationCode
#         + "/"
#         + companyIdentificationCode
#         + "/"
#         + gatewayTag
#         + "/SmartPlug_1/get",
#         "key": ["state"],
#     },
#     # SmartPlug_1
#     {
#         "Topic_in": "SmartPlug_1",
#         "Topic_out": tenantIdentificationCode
#         + "/"
#         + companyIdentificationCode
#         + "/"
#         + gatewayTag
#         + "/SmartPlug_1/get",
#         "key": ["current", "energy", "state", "power", "link_quality", "voltage"],
#     },
#     # Thermovalve_1
#     {
#         "Topic_in": "Thermovalve_1",
#         "Topic_out": tenantIdentificationCode
#         + "/"
#         + companyIdentificationCode
#         + "/"
#         + gatewayTag
#         + "/Thermovalve_1/get",
#         "key": [
#             "battery_low",
#             "child_lock",
#             "open_window",
#             "local_temperature",
#             "frost_protection",
#             "link_quality",
#             "heating_stop",
#             "online",
#         ],
#     },
#     # WaterLeakDetector_1
#     {
#         "Topic_in": "WaterLeakDetector_1",
#         "Topic_out": tenantIdentificationCode
#         + "/"
#         + companyIdentificationCode
#         + "/"
#         + gatewayTag
#         + "/WaterLeakDetector_1/get",
#         "key": ["tamper", "battery_low", "water_leak", "temperature", "link_quality"],
#         "Topic_custom": [
#             {
#                 "key": "temperature",
#                 "Topic_out": tenantIdentificationCode
#                 + "/"
#                 + companyIdentificationCode
#                 + "/"
#                 + gatewayTag
#                 + "/WaterLeakDetector_1/temperature/get",
#             },
#         ],
#     },
#     # WindowSensor_1
#     {
#         "Topic_in": "WindowsSensor_1",
#         "Topic_out": tenantIdentificationCode
#         + "/"
#         + companyIdentificationCode
#         + "/"
#         + gatewayTag
#         + "/WindowSensor_1/get",
#         "key": ["contact", "battery_low", "tamper", "temperature", "link_quality"],
#         "Topic_custom": [
#             {
#                 "key": "temperature",
#                 "Topic_out": tenantIdentificationCode
#                 + "/"
#                 + companyIdentificationCode
#                 + "/"
#                 + gatewayTag
#                 + "/WindowSensor_1/temperature/get",
#             },
#         ],
#     },
# ]

# ########### Gateway Settings ###########

# Login = {
#     "type": "auth",
#     "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI5NGQ4ZDMwYWMzNzQ0MDhkODM4YzZjNTY3MzFmNDhlYSIsImlhdCI6MTY1MDUzMTU5MiwiZXhwIjoxOTY1ODkxNTkyfQ.wGqiJhLJ_2YHgbuyC96iAM4K5v20L-1KYJJhVmRUCKA",
# }

# EventsSub = {"id": 18, "type": "subscribe_events", "event_type": "state_changed"}
