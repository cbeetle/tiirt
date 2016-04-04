from reader import StreamReader, StreamReaderState
from gui import GUI
import tkinter as tk
import vlc


def mainloop():
    #if (reader.player.get_state() = ")
    if hasattr(reader, 'player'):
        state = reader.player.get_state()
        #print(state)
        if(state.value is vlc.State.Playing.value):
            reader.getImage()
            gui.update_previews()
    gui.after(33, mainloop)

def on_closing():
    if hasattr(reader, 'player'):
        reader.player.stop()
    root.destroy();

reader = StreamReader()
root = tk.Tk();
gui = GUI(reader, master=root)
gui.master.title('TiRT - Projekt')
root.protocol("WM_DELETE_WINDOW", on_closing)
gui.after(33, mainloop)
gui.mainloop()