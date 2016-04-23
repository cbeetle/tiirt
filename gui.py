# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tkinter as tk
from PIL import Image, ImageTk
import os.path
import cv2

class GUI(tk.Frame):
    def __init__(self, reader, master=None):
        self.reader = reader
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.frame0=tk.Frame(self)
        self.frame0.grid(column=0, row=0, sticky=tk.W)

        self.menubuttonResetCharts = tk.Menubutton(self.frame0, text="Resetuj wykresy")
        self.menubuttonResetCharts.grid(column=0, row=0)
        self.menuResetChartsMenu = tk.Menu(self.menubuttonResetCharts, tearoff=0)
        self.menubuttonResetCharts['menu']=self.menuResetChartsMenu

        self.menuResetChartsMenu.add_command(label="Komenda1", command=self.quit)
        self.menuResetChartsMenu.add_command(label="Komenda2", command=self.quit)

        self.menubuttonGenerateCharts = tk.Menubutton(self.frame0, text="Generuj wykresy")
        self.menubuttonGenerateCharts.grid(column=1, row=0)
        self.menuGenerateChartsMenu = tk.Menu(self.menubuttonGenerateCharts, tearoff=0)
        self.menubuttonGenerateCharts['menu']=self.menuGenerateChartsMenu

        self.menuGenerateChartsMenu.add_command(label="Komenda3", command=self.quit)
        self.menuGenerateChartsMenu.add_command(label="Komenda4", command=self.quit)

        self.frame1=tk.Frame(self, padx=10, pady=5)
        self.frame1.grid(column=0, row=1)

        self.labelInputStreamAdress=tk.Label(self.frame1, text=("Adres streamu wejściowego:"))
        self.labelInputStreamAdress.grid(column=0, row=0, pady=10, sticky=tk.W)

        self.entryInputStreamAdress=tk.Entry(self.frame1)
        self.entryInputStreamAdress.grid(column=1,row=0)

        self.labelOutputStreamAdress=tk.Label(self.frame1, text=("Adres streamu wyjściowego:"))
        self.labelOutputStreamAdress.grid(column=0, row=1, pady=10, sticky=tk.W)

        self.entryOutputStreamAdress=tk.Entry(self.frame1)
        self.entryOutputStreamAdress.grid(column=1,row=1)

        self.variablePlayPause=tk.IntVar()
        self.imagePlaySelected=tk.PhotoImage(file="images\\playselected.gif")
        self.imagePlay=tk.PhotoImage(file="images\\play.gif")
        self.radiobuttonPlay=tk.Button(self.frame1, image=self.imagePlay, borderwidth=1, command=lambda: self.reader.connect(self.entryInputStreamAdress.get()))
        self.radiobuttonPlay.grid(column=1,row=2,)

        #self.imagePauseSelected=tk.PhotoImage(file="images\\pauseselected.gif")
        #self.imagePause=tk.PhotoImage(file="images\\pause.gif")
        #self.radiobuttonPause=tk.Radiobutton(self.frame1, image=self.imagePause, selectimage=self.imagePauseSelected,borderwidth=1,indicatoron=0, variable=self.variablePlayPause, value=1)
        #self.radiobuttonPause.grid(column=1,row=2, sticky=tk.E)

        self.labelFiltersParameters=tk.Label(self.frame1, text="Parametry filtrów:")
        self.labelFiltersParameters.grid(column=0, row=2, sticky="WS")

        self.frameFiltersParameters=tk.Frame(self.frame1, width=300, height=240, bg='#00ffff')
        self.frameFiltersParameters.grid_propagate(0)
        self.frameFiltersParameters.grid(column=0, row=3, columnspan=2, pady=10, sticky=tk.W)

        self.frame2=tk.Frame(self, padx=10, pady=5)
        self.frame2.grid(column=1, row=1)

        self.labelFilters=tk.Label(self.frame2, text=("Filtry:"))
        self.labelFilters.grid(column=0, row=0)

        self.listboxFilters=tk.Listbox(self.frame2, height=15, width=25)
        self.listboxFilters.grid(column=0, row=1, pady=10)

        self.frame2_1=tk.Frame(self.frame2)
        self.frame2_1.grid(column=0, row=2)

        self.buttonAdd=tk.Button(self.frame2_1, text='+', width=3)
        self.buttonAdd.grid(column=0, row=0, padx=5)

        self.buttonRemove=tk.Button(self.frame2_1, text='-', width=3)
        self.buttonRemove.grid(column=1, row=0, padx=5)

        self.buttonUp=tk.Button(self.frame2_1, text='\u21E7', width=3)
        self.buttonUp.grid(column=2, row=0, padx=5)

        self.buttonDown=tk.Button(self.frame2_1, text='\u21E9', width=3)
        self.buttonDown.grid(column=3, row=0, padx=5)

        self.frame3=tk.Frame(self, padx=15, pady=10)
        self.frame3.grid(column=2,row=1, rowspan=3)

        self.labelInputVideo=tk.Label(self.frame3, text="Obraz wejściowy")
        self.labelInputVideo.grid(column=0,row=0)
        self.imgtk=ImageTk.PhotoImage(file="play.png")
        self.frameInputVideo=tk.Label(self.frame3, image=self.imgtk, width=320, height=240)
        self.frameInputVideo.grid_propagate(0)
        self.frameInputVideo.grid(column=0, row=1, pady=5)

        self.labelOutputVideo=tk.Label(self.frame3, text="Obraz wyjściowy")
        self.labelOutputVideo.grid(column=0,row=2, pady=5)
        self.imgtk2=ImageTk.PhotoImage(file="play.png")
        self.frameOutputVideo=tk.Label(self.frame3, image=self.imgtk2, width=320, height=240)
        self.frameOutputVideo.grid_propagate(0)
        self.frameOutputVideo.grid(column=0,row=3)


        
    def update_previews(self, img):
        if os.path.isfile('snapshot.png'):
            #input frame
            #self.in_img = ImageTk.PhotoImage(Image.open('snapshot.png'))
            #self.frameInputVideo.configure(image = self.in_img)
            #image processing
            self.imgtk=ImageTk.PhotoImage(image=img)
            self.proc_out_img = cv2.blur(self.proc_in_img, (15, 15))
            self.im2=Image.fromarray(self.proc_out_img)
            self.imgtk2=ImageTk.PhotoImage(image=self.im2)
            self.frameInputVideo.configure(image = self.imgtk)
            self.frameOutputVideo.configure(image = self.imgtk2)
            #self.frameInputVideo=tk.Label(self.frame3, image=self.imgtk, width=320, height=240)
            #self.frameInputVideo.grid(column=0, row=1, pady=5)            
            #self.frameOutputVideo=tk.Label(self.frame3, image=self.imgtk2, width=320, height=240)
            #self.frameOutputVideo.grid(column=0,row=3)
            


