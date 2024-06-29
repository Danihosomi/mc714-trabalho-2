from paho.mqtt import client as mqtt_client
import util, time, message, random, os, sys


def connect_mqtt(device_id) -> mqtt_client:

    def on_connect(client, userdata, flags, rc):
        return None

    client = mqtt_client.Client(device_id)
    client.on_connect = on_connect
    client.connect(util.BROKER_ADDRESS,util.PORT)
    return client

class Device: ### represents a device in the network
    def __init__(self, id):
        self.id = id
        self.timestamp = 0
        self.leader_id = id ### everyone starts as its own leader
        self.has_token = False
        self.client = connect_mqtt(str(self.id))
        self.subscribe()

    def __str__(self):
        return f"Device(id={self.id}, has_token={self.has_token}, leader_id={self.leader_id}, timestamp={self.timestamp})"

    def publish(self, main_data, receiver = "all"):
        time.sleep(1)
        self.timestamp +=1

        msg = message.Message(self.id, str(receiver), main_data, self.timestamp)
        result = self.client.publish(util.TOPIC, msg.__str__())
        status = result[0]

        if status == 0:
            if msg.receiver == "all":
                print(f"Device {msg.sender} broadcasted message to all devices with timestamp {msg.timestamp}", file = sys.stderr)
            else:
                print(f"Device {msg.sender} sent message to device {msg.receiver} with timestamp {msg.timestamp}", file = sys.stderr)
        else:
            print(f"Failed to send message to device {msg.receiver}", file = sys.stderr)
            
    def subscribe(self):
        def on_message(client, userdata, msg):
            MSG = message.__uncode__(msg.payload.decode())

            if MSG.receiver == str(self.id):
                MSG.receiver = int(MSG.receiver)
                self.timestamp = max(self.timestamp, MSG.timestamp+1)
                print(f"Device {MSG.receiver} received a message from {MSG.sender}", file = sys.stderr)
                print(f"Device {self.id} timestamp is {self.timestamp}", file = sys.stderr)
                time.sleep(1 + random.randint(0,3))
                if MSG.data== "token":
                    self.set_token()

                elif MSG.data == "election_answer":
                    print(f"Device {MSG.sender} is the new leader of the {self.id} device", file = sys.stderr)
                    self.leader_id = max(MSG.sender, self.leader_id)

            elif MSG.receiver == "all" and MSG.sender != self.id:
                self.timestamp = max(self.timestamp, MSG.timestamp+1)
                print(f"Device {self.id} received a message from {MSG.sender}", file = sys.stderr)
                print(f"Device {self.id} timestamp is {self.timestamp}", file = sys.stderr)
                time.sleep(1 + random.randint(0,3))
                if MSG.data == "election":
                    self.election(MSG.sender)

        self.client.subscribe(util.TOPIC)
        self.client.on_message = on_message

    def election(self, sender_id):
        if sender_id < self.id:
            print(f"Device {self.id} is its own leader!", file = sys.stderr)
            self.publish("election_answer", receiver = sender_id)
            time.sleep(1 + random.randint(0,3))
            self.publish("election", receiver = "all")
        else:
            print(f"Device {sender_id} is the new leader of the {self.id} device", file = sys.stderr)
            self.leader_id = sender_id

    def apply_resource(self):
        time.sleep(1 + random.randint(0,3))
        print(f"Device {self.id} has the token and is using the resource", file = sys.stderr)
    
    def use_resource(self):
        if self.has_token == True:
            self.apply_resource()

    def pass_token(self):
        self.has_token = False
        print(f"Device {self.id} has no longer the token", file = sys.stderr)
        self.publish("token", receiver = (self.id + 1) % 5)

    def set_token(self):
        self.has_token = True
        self.use_resource()
        self.pass_token()


def run(device):
    if device.id == 0:
        device.publish("election", receiver = "all")

        time.sleep(40)

        device.set_token()
        
    
    device.publish("hello", receiver = "all")
    device.publish("hello you", receiver = (device.id + 1) % 5)

    device.client.loop_forever()

if __name__ == "__main__":
    id = int(os.environ["ID"])

    device = Device(id)
    run(device)    