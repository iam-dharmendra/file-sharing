from channels.generic.websocket import WebsocketConsumer

from random import randint
from time import sleep
import json

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        # for i in range(50):
        for i in range(0,20):
            self.send(json.dumps(i))
            sleep(1)