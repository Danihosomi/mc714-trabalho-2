from paho.mqtt import client as mqtt_client
import util
import time
import message

def connect_mqtt(device_id) -> mqtt_client:

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(device_id)
    client.on_connect = on_connect
    client.connect(util.BROKER_ADDRESS,util.PORT)
    return client

class Device:
    def __init__(self, id, name, status, timestamp):
        self.id = id
        self.name = name
        self.status = status
        self.timestamp = timestamp
        self.has_token = False
        self.client = connect_mqtt(self.id)

    def __str__(self):
        return f"Device(id={self.id}, name={self.name}, status={self.status}, has_token={self.has_token})"

    def publish(self):

        while True:
            time.sleep(1)
            message.MSG_COUNTER += 1
            msg = message.Message(message.MSG_COUNTER+1, self.id, "receba", "MENSAGEM", self.timestamp)
            result = self.client.publish(util.TOPIC, msg)
            status = result[0]

            if status == 0:
                print(f"Send `{msg}` to topic `{util.TOPIC}`")
            else:
                print(f"Failed to send message to topic {util.TOPIC}")
            
    def subscribe(self):
        def on_message(client, userdata, msg):
            if msg.receiver == self.id:
                print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            
        self.client.subscribe(util.TOPIC)
        self.client.on_message = on_message

    def apply_resource(self):
        print(f"Device {self.id} is using the resource")
    
    def use_resource(self):
        if self.has_token == True:
            self.apply_resource()

    def pass_token(self):
        pass

    def set_token(self):
        self.has_token = True
        self.use_resource()
        self.pass_token()

def run():
    device = Device()

if __name__ == '__main__':
    run()