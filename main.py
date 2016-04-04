from gui import GUI

def mainloop():
    print("Loop")
    app.after(33, mainloop)

app = GUI()
app.master.title('TiRT - Projekt')
app.after(33, mainloop)
app.mainloop()