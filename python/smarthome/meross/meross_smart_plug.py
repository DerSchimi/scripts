import os
import time
import argparse
from random import randint

from meross_iot.cloud.devices.door_openers import GenericGarageDoorOpener
from meross_iot.cloud.devices.hubs import GenericHub
from meross_iot.cloud.devices.humidifier import GenericHumidifier, SprayMode
from meross_iot.cloud.devices.light_bulbs import GenericBulb
from meross_iot.cloud.devices.power_plugs import GenericPlug
from meross_iot.cloud.devices.subdevices.thermostats import ValveSubDevice, ThermostatV3Mode
from meross_iot.cloud.devices.subdevices.sensors import SensorSubDevice
from meross_iot.manager import MerossManager
from meross_iot.meross_event import MerossEventType
from pytradfri.util import load_json

CONFIG_FILE = "credentials.conf"
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-P', '--plug', dest='plug', required=True)
    parser.add_argument('-on','--on',  dest='on', required=False, action='store_true')
    parser.add_argument('-off','--off', dest="off",required=False, action='store_true')

    args = parser.parse_args()

    conf = load_json(CONFIG_FILE)
    EMAIL = conf["meross"].get("email")
    PASSWORD = conf["meross"].get("password")

    manager = MerossManager.from_email_and_password(meross_email=EMAIL, meross_password=PASSWORD)
    manager.start()
    p = manager.get_device_by_name(args.plug)
    print("found device: " + str(p))
    channels = len(p.get_channels())
    print("The plug %s supports %d channels." % (p.name, channels))

    for i in range(0, channels):
     if args.on:
      p.turn_on_channel(i)
      print("Turning on channel %d of %s" % (i, p.name))
     elif args.off:
      print("Turning off channel %d of %s" % (i, p.name))
      p.turn_off_channel(i)

    manager.stop()


