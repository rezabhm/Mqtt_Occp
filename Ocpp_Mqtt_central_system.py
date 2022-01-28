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


def on_connect(mqtt_connection):

    """
    For every new charge point that connects, create a ChargePoint
    instance and start listening for messages.
    """

    topic_list = [

        {'send_topic': 'reza/ocpp_old/mqtt/charge_point_0/recv/',
         'recv_topic': 'reza/ocpp_old/mqtt/charge_point_0/send/',
         'charge_point_id': 'charge_point_0',
         },

        {'send_topic': 'reza/ocpp_old/mqtt/charge_point_1/recv/',
         'recv_topic': 'reza/ocpp_old/mqtt/charge_point_1/send/',
         'charge_point_id': 'charge_point_1',
         },

    ]

    cp = ChargePoint('Central_system_Root', mqtt_connection, topic_list, ['data/server/server.json',])

    cp.manage_message()


def main():

    client = mqtt_client.Client('chargeV'+str(random.randint(0, 50)))

    broker_id = "broker.emqx.io"

    client.connect(broker_id, 1883)

    logging.info("WebSocket Server Started")
    on_connect(client)


if __name__ == '__main__':
    main()
