# -*- coding: utf-8 -*-
from enum import Enum
import vlc
class StreamReaderState(Enum):
    Waiting = 0;
    Connected = 1;
class StreamReader:
    def __init__(self):
        self.state = StreamReaderState.Waiting
    def connect(self, address):
        self.player=vlc.MediaPlayer('rtsp://' + address)
        self.player.play()
    def getImage(self):
        self.player.video_take_snapshot(0, 'snapshot.png', 0, 0)