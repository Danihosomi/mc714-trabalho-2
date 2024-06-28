def __uncode__(msg):
    msg_parts = msg.split(",")
    return Message(msg_parts[0], msg_parts[1], msg_parts[2], msg_parts[3])

class Message:

    def __init__(self, sender, receiver, data, timestamp):
        self.sender = sender
        self.receiver = receiver
        self.data = data ### data can be only a message or can be a leader election message or can be a resource pass message
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.sender},{self.receiver},{self.data},{self.timestamp}"