MSG_COUNTER = 0 ### common counter for all messages

class Message:

    def __init__(self, id, sender, receiver, data, timestamp):
        self.id = id
        self.sender = sender
        self.receiver = receiver
        self.data = data ### data can be only a message or can be a leader election message or can be a resource pass message
        self.timestamp = timestamp

    def __str__(self):
        return f"Message(id={self.id}, sender={self.sender}, receiver={self.receiver}, data={self.data}, timestamp={self.timestamp})"