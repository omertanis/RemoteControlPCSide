import multiprocessing
from Tkinter import *
import PIL
# from multiprocessing import Process
import ttk
import time
import qrCreator
# -*- coding: utf-8 -*-
class Application():

    def __init__(self, master=None):
        self.mainPage()


    def backOnClick(self):
        frameBluetooth.pack_forget()
        frameWifi.pack_forget()
        frameMain.pack()
        self.thread.terminate()


    def useBluetooth2(self):
        self.thread = multiprocessing.Process(target=self.useBluetooth, name="threadBluetoth")
        self.thread.start()

    def useBluetooth(self):
        print("bluetooth")
        import Bluetooth

    def useWifi(self):
        self.thread = None
        self.thread = multiprocessing.Process(target=self.useWifi2, name="threadWifi")
        self.thread.start()
    def useWifi2(self):
        print("wifi")
        import wifi


    def mainPage(self):
        labelVar = StringVar()

        frameMain.configure(background='#299FD2')
        frameMain.pack()
        # ----------
        # logo
        import PIL.ImageTk
        space1 = Label(frameMain, text="\n\n", background='#299FD2')
        space1.pack()

        im = PIL.Image.open("logo.png")
        im = im.resize((150, 150))
        photo = PIL.ImageTk.PhotoImage(im)
        label = Label(frameMain, image=photo, background='#299FD2')
        label.image = photo
        label.pack()

        # -----------
        labelMain = Label(frameMain, textvariable=labelVar, background='#299FD2')
        labelMain.config(font=("Helvetica", 40))
        labelVar.set("Remote Control")
        labelMain.pack()

        R1 = Radiobutton(frameMain, text="Bluetooth", variable=var, value=0, background='#299FD2')
        R1.config(font=("Helvetica", 20))

        R1.pack()

        R2 = Radiobutton(frameMain, text="Wifi", variable=var, value=1, background='#299FD2')
        R2.config(font=("Helvetica", 20))
        R2.pack()

        space2 = Label(frameMain, text="\n", background='#299FD2')
        space2.pack()

        B = Button(frameMain, text="Cihaz Ara", command=self.helloCallBack, background='#b3c6e5')
        B.config(font=("Helvetica", 20))
        B.pack()
        self.createWifiQr()
        self.createBluetoothQr()
        root.mainloop()

    def createBluetoothQr(self):

        frameBluetooth.configure(background='#299FD2')

        space3 = Label(frameBluetooth, text="\n\n", background='#299FD2')
        space3.pack()
        im = PIL.Image.open("bluetooth.png")
        im = im.resize((300, 300))
        photo = PIL.ImageTk.PhotoImage(im)

        label = Label(frameBluetooth, image=photo, background='#299FD2')
        label.image = photo
        label.pack()
        space4 = Label(frameBluetooth, text="\n\n", background='#299FD2')
        space4.pack()
        B = Button(frameBluetooth, text="Geri", command=self.backOnClick, background='#b3c6e5')
        B.config(font=("Helvetica", 20))
        B.pack()

        B = Button(frameBluetooth, text="Run", command=self.useBluetooth2, background='#b3c6e5')
        B.config(font=("Helvetica", 20))
        B.pack()

    def createWifiQr(self):
        frameWifi.configure(background='#299FD2')

        space5 = Label(frameWifi, text="\n\n", background='#299FD2')
        space5.pack()

        im = PIL.Image.open("wifi.png")
        im = im.resize((300, 300))
        photo = PIL.ImageTk.PhotoImage(im)
        label = Label(frameWifi, image=photo, background='#299FD2')
        label.image = photo
        label.pack()

        space6 = Label(frameWifi, text="\n\n", background='#299FD2')
        space6.pack()

        B = Button(frameWifi, text="Geri", command=self.backOnClick, background='#b3c6e5')
        B.config(font=("Helvetica", 20))
        B.pack()

        B = Button(frameWifi, text="Run", command=self.useWifi, background='#b3c6e5')
        B.config(font=("Helvetica", 20))
        B.pack()




    def helloCallBack(self):
        # frameMain.pack_forget()
        if(var.get() == 0):
            frameMain.pack_forget()
            frameBluetooth.pack()

        else:
            frameMain.pack_forget()
            frameWifi.pack()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    root = Tk()
    root.minsize(width=500, height=500)
    root.resizable(width=False, height=False)
    root.configure(background='#299FD2')
    root.title(' TK Wizards ')
    var = IntVar()
    frameMain = Frame(root)
    frameBluetooth = Frame(root)
    frameWifi = Frame(root)
    app = Application(master=root)
