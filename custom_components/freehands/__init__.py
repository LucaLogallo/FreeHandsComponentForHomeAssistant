"""The freehandsmiddleware integration."""
from __future__ import annotations

import asyncio
from datetime import timedelta  # importa il delta

# from asyncore import loop
import logging
import random

from paho.mqtt import client as mqtt_client

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN

# TODO List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
PLATFORMS: list[Platform] = [Platform.LIGHT]

_LOGGER: logging.Logger = logging.getLogger(__package__)
_LOGGER.info("Hello World freeHands!")


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up freehandsmiddleware from a config entry."""
    # TODO Store an API object for your platforms to access
    # hass.data[DOMAIN][entry.entry_id] = MyApi(...)

    hass.config_entries.async_setup_platforms(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


from .const import BROKER, PASSWORD, PORT, TOPIC, USERNAME

# generate client ID with pub prefix randomly
client_id = f"python-mqtt-{random.randint(0, 1000)}"

URI = "mqtt://" + USERNAME + ":" + PASSWORD + "@" + BROKER + "." + PORT

broker = "192.168.0.101"
port = 1883
topic = "zigbee2mqtt/0x0015bc002f0117ee"
# generate client ID with pub prefix randomly
client_id = "python-mqtt-2"  # f'python-mqtt-{random.randint(0, 1000)}'
username = "mqtt_user"
password = "%%7!P6C6zji@VADv"
turn = False
sensorData = ""

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        _LOGGER.info("freeHands connected to MQTT Broker!")
        # print("connected")
    else:
        _LOGGER.info("freeHands failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg, sensorData):
    _LOGGER.info(
        "Received " + str(msg.payload.decode("utf-8")) + " from `{msg.topic}` topic"
    )
    sensorData = str(msg.payload.decode("utf-8"))

    # def publish(turn):
    #     if turn is not True:
    #         turn = True
    #         client.publish("zigbee2mqtt/0x00158d0006e0f046/action", "single")

    # publish(turn)
    # print("Received " + str(msg.payload.decode("utf-8")) + " from `{msg.topic}` topic")

def on_publish(client, userdata, result):  # create function for callback
    print("data published \n" + str(userdata))
    print("result" + str(result))
    ref = on_publishToBrokerFreehands
    pass

def on_disconnect(client, userdata, rc=0):
    logging.debug("DisConnected result code " + str(rc))
    client.loop_stop()

###########################################################################################
# def on_connectToBrokerFreehands(client, userdata, rc):
#     if rc == 0:
#         _LOGGER.info("freeHands connected to MQTT Broker!")
#         # print("connected")
#     else:
#         _LOGGER.info("freeHands failed to connect, return code %d\n", rc)


# def on_messageToBrokerFreehands(client, userdata, msg):
#     _LOGGER.info(
#         "Received " + str(msg.payload.decode("utf-8")) + " from `{msg.topic}` topic"
#     )


# def on_publishToBrokerFreehands(
#     client, userdata, result
# ):  # create function for callback
#     print("data published \n" + str(userdata))
#     print("result" + str(result))
#     pass


# def on_disconnectToBrokerFreehands(client, userdata, rc=0):
#     logging.debug("DisConnected result code " + str(rc))
#     client1.loop_stop()

###########################################################################################

client = mqtt_client.Client(client_id)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.connect("192.168.3.122", 1883)
client.subscribe(topic)
ret = client.publish("zigbee2mqtt/0x00158d0006e0f046/action", "single")

# usernameBrokerFreehands = "pippo"
# passwordBrokerFreehands = "pluto"

# client1 = mqtt_client.Client(client_id)
# client1.username_pw_set(usernameBrokerFreehands, passwordBrokerFreehands)
# client1.on_connect = on_connectToBrokerFreehands
# client1.on_message = on_messageToBrokerFreehands
# client1.on_disconnect = on_disconnectToBrokerFreehands
# client1.on_publish = on_publishToBrokerFreehands
# client1.connect("192.168.3.68")
# client1.subscribe("tenant/company/gateway/sensore/misura/get/")

client1.loop_forever() #client sottoscrito al broker mqtt nel bc di freehands
client.loop_forever() #client sottoscritto al broker mqtt interno a homeassistant
