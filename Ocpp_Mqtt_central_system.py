import asyncio
import logging
from datetime import datetime
import paho.mqtt.client as mqtt_client

from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call_result

import random

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp):
    @on('BootNotification')
    async def on_boot_notification(self, charging_station, reason, **kwargs):
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status='Accepted'
        )


def on_connect(mqtt_connection, path):
    """ For every new charge point that connects, create a ChargePoint
    instance and start listening for messages.
    """

    get_topic = 'reza/ocpp/central/'
    send_topic = 'reza/ocpp/charge_point/'

    charge_point_id = path.strip('/')
    cp = ChargePoint(charge_point_id, mqtt_connection, send_topic, get_topic, 'data/server/server')

    cp.manage_message()


def main():

    client = mqtt_client.Client('reza'+str(random.randint(0, 50)))

    broker_id = "mqtt.eclipseprojects.io"

    client.connect(broker_id, 1883)

    logging.info("WebSocket Server Started")
    on_connect(client, '/reza/bhm/12901290/')

if __name__ == '__main__':
    asyncio.run(main())
