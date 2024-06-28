import message
import random
from paho.mqtt import client as mqtt_client


BROKER_ADDRESS = 'broker.emqx.io'
PORT = 1883
TOPIC = 'mc714-trab-2'
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(BROKER_ADDRESS, PORT)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        MSG = message.__uncode__(msg.payload.decode())
        print(f"{MSG.receiver} received a message with id {MSG.id()} from {MSG.sender}")

    client.subscribe(TOPIC)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
