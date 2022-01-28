import paho.mqtt.client as mqtt
import time
import random

# information
broker_id = "broker.hivemq.com"
topic = 'RezaBhm10/Example/Status'
client_id = 'rezabhm50'

# create client
reza_client = mqtt.Client(client_id)

# connect to broker
reza_client.connect(broker_id, 1883)

dt = ['w', 'r', 't', 'y']

counter = 0
while True:

    counter += 1

    msg = str(dt[(len(dt) % counter) - 1]) + ' ==> ' + str(random.randint(1, 1000)) + ' reza'

    # publish to broker
    result = reza_client.publish(topic, msg)

    # successfully publish to broker
    print('successfully publish [ {0} ] to broker .'.format(msg))

    time.sleep(3.0)

    if counter % 30 == 0.0:
        break

print('finished publish')
