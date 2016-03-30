#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

class Okno(Frame):  # definiujemy klase

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Projekt z TiRT - panel sterowania")
        ttk.Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.rowconfigure(0, pad=3)

        # lbl-etykieta, cls-przycisk, lst-listbox, w pack definiujesz wyrównanie, padding, rozszerzalność
        placeholder = Button(self, text="Resetuj statystyki", command=self.quit)
        placeholder.grid(row=1, column=0, sticky=W + E)

        placeholder = Button(self, text="Generuj wykresy", command=self.quit)
        placeholder.grid(row=1, column=1, sticky=W + E)

        lbl_adres_streamu_wej = Label(self, text="Adres wejściowego streamu:")
        lbl_adres_streamu_wej.grid(row=3, column=0)

        adres_streamu_wej = Entry(self)
        adres_streamu_wej.grid(padx=15, row=3, column=1, columnspan=2, rowspan=1)

        lbl_filtry = Label(self, text="Filtry:")
        lbl_filtry.grid(row=3, column=3)

        lbl_obraz_wej = Label(self, text="Obraz wejściowy:")
        lbl_obraz_wej.grid(row=3, column=5)

        placeholder = Listbox(self)
        placeholder.grid(padx=15, row=4, column=3, columnspan=2, rowspan=4)

        placeholder = Listbox(self)
        placeholder.grid(pady=15, row=4, column=5, columnspan=2, rowspan=4)

        lbl_adres_streamu_wyj = Label(self, text="Adres wyjściowego streamu:")
        lbl_adres_streamu_wyj.grid(row=5, column=0)
        # zadecydowac jaki format itd

        cls_start = Button(self, text="|>", command=self.quit)
        cls_start.grid(row=6, column=1, sticky=W + E)

        cls_stop = Button(self, text="[]", command=self.quit)
        cls_stop.grid(row=6, column=2, sticky=W + E)

        lbl_filtry = Label(self, text="Parametry filtrów:")
        lbl_filtry.grid(row=7, column=0)

        lst_filtry = Listbox(self)
        lst_filtry.grid(pady=15, row=8, column=0, columnspan=1, rowspan=1)

        lbl_obraz_wyj = Label(self, text="Obraz wyjściowy:")
        lbl_obraz_wyj.grid(row=9, column=5)

        placeholder = Label(self, text="TU MA BYĆ TO")
        placeholder.grid(padx=15, row=10, column=5, columnspan=1, rowspan=1)

        cls_plus = Button(self, text="+", command=self.quit)
        cls_plus.grid(row=11, column=1, sticky=W + E)

        cls = Button(self, text="[]", command=self.quit)
        cls.grid(row=11, column=2, sticky=N + S)

        self.pack()


width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


def main():
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    root.bind('<Escape>', lambda e: root.quit())
    ws = root.winfo_screenwidth()  # sprawdza szerokosc ekranu
    hs = root.winfo_screenheight()  # sprawdza wysokość ekranu
    w = 800  # Zadana początkowa szerokość oknna
    h = 600  # zadana początkowa wysokość okna
    centerx = (ws / 2) - (w / 2)  # Obliczenia w celu wycentrowania okna
    centery = (hs / 2) - (h / 2)  # Obliczenia w celu wycentrowania okna
    root.geometry('%dx%d+%d+%d' % (w, h, centerx, centery))  # Definiuje rozmiar i położenie okna
    app = Okno(root)  # tworzymy instancje klasy
    root.mainloop()



root = Tk()
lmain = Label(root)
lmain.pack()

def show_frame():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(33, show_frame)
show_frame()

if __name__ == '__main__':
    main()
