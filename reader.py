# -*- coding: utf-8 -*-
from enum import Enum
import cv2

class StreamReaderState(Enum):
    Waiting = 0;
    Connected = 1;
class StreamReader:
    def __init__(self):
        self.state = StreamReaderState.Waiting
    def connect(self, address):
        self.cap = cv2.VideoCapture('rtsp://' + address)
        if not self.cap:
            print("!!! Failed VideoCapture: invalid parameter!")
        else:
            self.state = StreamReaderState.Connected
    def get_image(self):
        return self.cap.read()
    def on_closing(self):
        if(hasattr(self, 'cap')):
            self.cap.release()