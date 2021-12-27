import time
import paho.mqtt.client as mqtt


def on_message(client, user_data, msg):

    print("message : {0}".format(str(msg.payload.decode())))


# information
broker_id = "mqtt.eclipseprojects.io"
topic = 'RezaBhm10/Example/Status'
client_id = 'rezabhm50_subscriber'

# create client
reza_client = mqtt.Client(client_id)

# connect
reza_client.connect(broker_id, 1883)
reza_client.loop_start()

while True:

    # subscribe message
    reza_client.subscribe(topic)
    reza_client.on_message = on_message

    # sleep
    time.sleep(3.0)


reza_client.loop_stop()

