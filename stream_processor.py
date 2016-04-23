from reader import StreamReader
from reader import StreamReaderState
from gui import GUI
import tkinter as tk
import vlc

class StreamProcessor():
    def __init__(self):
        self.reader = StreamReader()
        self.root = tk.Tk();
        self.gui = GUI(self.reader, master=self.root)
        self.gui.master.title('TiRT - Projekt')
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.gui.after(33, self.mainloop)
        self.gui.mainloop()
    def mainloop(self):
        if(self.reader.state == StreamReaderState.Connected):
            img = self.reader.get_image()
            self.gui.update_previews(img)
        self.gui.after(33, self.mainloop)
    def on_closing(self):
        #if hasattr(reader, 'player'):
        #    reader.player.stop()
        self.reader.on_closing()
        self.root.destroy()