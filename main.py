from reader import StreamReader, StreamReaderState
from gui import GUI

def mainloop():
    print("Loop")
    gui.after(33, mainloop)

reader = StreamReader()
gui = GUI(reader)
gui.master.title('TiRT - Projekt')
#gui.after(33, mainloop)
gui.mainloop()