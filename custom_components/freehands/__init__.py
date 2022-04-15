"""
Custom integration to integrate freeHands with Home Assistant.

For more details about this integration, please refer to
https://github.com/riveccia/freehands
"""
import asyncio
import logging
from datetime import timedelta
from unittest import result

from github3 import user

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Config
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.helpers.update_coordinator import UpdateFailed

import random

# from paho.mqtt import client as mqtt_client

from .api import FreehandsApiClient

import paho.mqtt.client as mqtt
import logging, time
import jsonpickle

import json

from .const import (
    CONF_PASSWORD,
    CONF_USERNAME,
    CONF_USERNAME,
    DOMAIN,
    PLATFORMS,
    STARTUP_MESSAGE,
)

from .const import Freehands, Topics

# FreehandsConfiguration = json.dumps(Freehands)
# TopicsConfiguration = json.loads(Topics)
# TopicsConfiguration = jsonpickle.decode(Topics)

SCAN_INTERVAL = timedelta(seconds=30)

_LOGGER: logging.Logger = logging.getLogger(__package__)
_LOGGER.info("Hello World freeHands!")

voltage = {"voltageIst": 0, "power": 0, "reactivePowerIst": 0, "voltageOverall": 0}


async def async_setup(hass: HomeAssistant, config: Config):
    """Set up this integration using YAML is not supported."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up this integration using UI."""
    if hass.data.get(DOMAIN) is None:
        hass.data.setdefault(DOMAIN, {})
        _LOGGER.info(STARTUP_MESSAGE)

    username = entry.data.get(CONF_USERNAME)
    password = entry.data.get(CONF_PASSWORD)

    session = async_get_clientsession(hass)
    client = FreehandsApiClient(username, password, session)

    coordinator = FreehandsDataUpdateCoordinator(hass, client=client)
    await coordinator.async_refresh()

    if not coordinator.last_update_success:
        raise ConfigEntryNotReady

    hass.data[DOMAIN][entry.entry_id] = coordinator

    for platform in PLATFORMS:
        if entry.options.get(platform, True):
            coordinator.platforms.append(platform)
            hass.async_add_job(
                hass.config_entries.async_forward_entry_setup(entry, platform)
            )

    entry.add_update_listener(async_reload_entry)
    return True


class FreehandsDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    def __init__(
        self,
        hass: HomeAssistant,
        client: FreehandsApiClient,
    ) -> None:
        """Initialize."""
        self.api = client
        self.platforms = []

        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=SCAN_INTERVAL)

    async def _async_update_data(self):
        """Update data via library."""
        try:
            return await self.api.async_get_data()
        except Exception as exception:
            raise UpdateFailed() from exception


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle removal of an entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    unloaded = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
                if platform in coordinator.platforms
            ]
        )
    )
    if unloaded:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unloaded


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)


client_id = f"python-mqtt-{random.randint(0, 1000)}"
clientToFreeHands_id = f"freehands-mqtt-{random.randint(0, 1000)}"
clients = []
username = "mqtt_user"
# usernameTo


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        _LOGGER.info("freeHands connected to MQTT Broker!")
        client.subscribe("#")
    else:
        _LOGGER.info("freeHands failed to connect, return code %d\n", rc)


def on_connectToFreehands(client, userdata, flags, rc):
    if rc == 0:
        _LOGGER.info("djahsdkjhaskjdhkajshdkjashdkajshdkajshd!")
        client.subscribe("#")
    else:
        _LOGGER.info("freeHands failed to connect, return code %d\n", rc)


def on_message(client, userdata, msg):

    # print("messagio messaggio messaggio messaggio messaggio messaggio")
    _LOGGER.info(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    for t in Topics:
        if t["Topic_in"] == msg.topic:
            topic = t["Topic_out"]
            message_routing(client, topic, msg.payload)


def message_routing(client, topic, msg):

    if client._client_id.decode("utf-8") == client_id:
        print("PAYLOAD :" + msg.decode("utf-8"))
        print("TOPIC: " + topic)
        client1.publish(topic=topic, payload=msg)
        # ret = client1.publish(topic, msg)
    elif client._client_id.decode("utf-8") == clientToFreeHands_id:
        # ret = client.publish(topic, msg)
        print("ciao")


def on_publish(client, userdata, result):  # create function for callback
    print("data published  \n" + str(result) + "RESULT \n")
    # print("MESSAGGIO: " + userdata)
    # print("CLIENT :" + client + "\n\n")
    pass


client = mqtt.Client(
    client_id=client_id,
    clean_session=True,
    userdata=None,
    protocol=mqtt.MQTTv31,
    transport="tcp",
)
client.username_pw_set("mqtt_user", "%%7!P6C6zji@VADv")
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.broker = "192.168.3.122"
client.port = 1883
client.topic = "#"
client.keepalive = 60
clients.append(client)
# client.connect("192.168.3.122", port)


client1 = mqtt.Client(
    client_id=clientToFreeHands_id,
    clean_session=True,
    userdata=None,
    protocol=mqtt.MQTTv31,
    transport="tcp",
)
client1.username_pw_set("pippo", "pluto")
# client1.username_pw_set(
#     FreehandsConfiguration["Username"], FreehandsConfiguration["Password"]
# )
client1.on_connect = on_connectToFreehands
client1.on_message = on_message
client1.on_publish = on_publish
client1.broker = "192.168.3.63"  # FreehandsConfiguration["Mqtt_ip"]
client1.port = 51885  # FreehandsConfiguration["Mqtt_port"]
client1.topic = "#"
client1.keepalive = 60
# clients.append(client1)


client.connect(client.broker, client.port, client.keepalive)
client.loop_start()


client1.connect(client1.broker, client1.port, client1.keepalive)
client1.loop_start()


# for x in clients:
#     logging.info("connecting to broker :" + str(x.broker))
#     try:
#         res = x.connect(x.broker, x.port, x.keepalive)  # connect to broker
#         x.loop_start()  # start loop
#     except:
#         _LOGGER.info("ERROR")
# except Exception as error:
#     logging.debug("connection failed")
#     print("connection failed", x.broker)
#     x.bad_count += 1
#     x.bad_connection_flag = True  # old clients use this

