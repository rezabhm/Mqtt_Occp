import asyncio
import logging
import paho.mqtt.client as mqtt_client

from ocpp.v201 import call
from ocpp.v201 import ChargePoint as cp
import random

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp):

   async def send_boot_notification(self):
       request = call.BootNotificationPayload(
               charging_station={
                   'model': 'Wallbox XYZ',
                   'vendor_name': 'anewone'
               },
               reason="PowerUp"
       )
       response = await self.call(request)

       if response.status == 'Accepted':
           print("Connected to central system.")


def main():

    client = mqtt_client.Client('reza' + str(random.randint(0, 50)))

    broker_id = "broker.emqx.io"

    client.connect(broker_id, 1883)

    topic_list = ['reza/ocpp_old/mqtt/charge_point_0/send/', 'reza/ocpp_old/mqtt/charge_point_0/recv/']
    cp = ChargePoint('charge_point_0', client, topic_list, ['data/charge_point/charge_point.json',
                                                            'data/charge_point/charge_point2.json'], False)

    print('charge point start ...\n')

    # asyncio.gather(cp.manage_message(), cp.send_boot_notification())
    # await cp.send_boot_notification()
    cp.manage_message()


if __name__ == '__main__':
   main()
