import socket
from qrCreator import ipadress
import time
print("wifi baglanti bekleniyor Top")
serversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind((ipadress, 8089))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ipadress, 8090))
s.listen(1)

connTCP, addrTCP = s.accept()
print 'Connection address:', addrTCP

while True:
    try:
        data, addr = serversocket.recvfrom(64)
        if data != "":
            # print(addr[0])
            time.sleep(0.0145)
            datas = []
            datas = data.split("/")

            # if mouse
            if (datas[0] == "mouse"):
                from pynput.mouse import Button, Controller
                mouse = Controller()
                if (datas[1] == "left"):
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                elif (datas[1] == "right"):
                    mouse.press(Button.right)
                    mouse.release(Button.right)
                elif (datas[1] == "scroll"):
                    mouse.scroll(0, int(datas[2]))
                else:
                    mouseX, mouseY = (mouse.position)
                    mouse.position = (mouseX + (int(datas[1]) / 10), (mouseY + int(datas[2]) / 10))
            else:
                if (datas[0] == "keyboard"):
                    from pynput.keyboard import Key, Controller
                    keyboard = Controller()
                    if (datas[1]) == "Backspace":
                        keyboard.press(Key.backspace)
                    elif(datas[1]) == "Enter":
                        keyboard.press(Key.enter)
                    elif(datas[1] == "fButtons"):
                        if datas[2] == "f1":
                            keyboard.press(Key.f1)
                        elif datas[2] == "f2":
                            keyboard.press(Key.f2)
                        elif datas[2] == "f3":
                            keyboard.press(Key.f3)
                        elif datas[2] == "f4":
                            keyboard.press(Key.f4)
                        elif datas[2] == "f5":
                            keyboard.press(Key.f5)
                        elif datas[2] == "f6":
                            keyboard.press(Key.f6)
                        elif datas[2] == "f7":
                            keyboard.press(Key.f7)
                        elif datas[2] == "f8":
                            keyboard.press(Key.f8)
                        elif datas[2] == "f9":
                            keyboard.press(Key.f9)
                        elif datas[2] == "f10":
                            keyboard.press(Key.f10)
                        elif datas[2] == "f11":
                            keyboard.press(Key.f11)
                        elif datas[2] == "f12":
                            keyboard.press(Key.f12)
                    elif(datas[1] == "controlButtonsPress"):
                        if (datas[2] == "ctrl"):
                            keyboard.press(Key.ctrl)
                        elif (datas[2] == "alt"):
                            keyboard.press(Key.alt)
                        elif (datas[2] == "arrowRight"):
                            keyboard.press(Key.right)
                        elif (datas[2] == "arrowLeft"):
                            keyboard.press(Key.left)
                        elif (datas[2] == "arrowTop"):
                            keyboard.press(Key.up)
                        elif (datas[2] == "arrowBottom"):
                            keyboard.press(Key.down)
                        elif (datas[2] == "tab"):
                            keyboard.press(Key.tab)
                        elif (datas[2] == "esc"):
                            keyboard.press(Key.esc)
                        elif (datas[2] == "delete"):
                            keyboard.press(Key.delete)

                    elif (datas[1] == "controlButtonsRelease"):
                        if (datas[2] == "ctrl"):
                            keyboard.release(Key.ctrl)
                            print("s")
                        elif (datas[2] == "alt"):
                            keyboard.release(Key.alt)

                    elif (datas[1] == "shortcut"):
                        if (datas[2] == "ctrl+c"):
                            keyboard.press(Key.ctrl)
                            keyboard.press("c")
                            keyboard.release(Key.ctrl)

                        elif (datas[2] == "ctrl+x"):
                            keyboard.press(Key.ctrl)
                            keyboard.press("x")
                            keyboard.release(Key.ctrl)

                        elif (datas[2] == "ctrl+v"):
                            keyboard.press(Key.ctrl)
                            keyboard.press("v")
                            keyboard.release(Key.ctrl)

                        elif (datas[2] == "ctrl+s"):
                            keyboard.press(Key.ctrl)
                            keyboard.press("s")
                            keyboard.release(Key.ctrl)

                        elif (datas[2] == "ctrl+z"):
                            keyboard.press(Key.ctrl)
                            keyboard.press("z")
                            keyboard.release(Key.ctrl)

                        elif (datas[2] == "ctrl+y"):
                            keyboard.press(Key.ctrl)
                            keyboard.press("y")
                            keyboard.release(Key.ctrl)

                        elif (datas[2] == "ctrl+a"):
                            keyboard.press(Key.ctrl)
                            keyboard.press("a")
                            keyboard.release(Key.ctrl)

                        elif (datas[2] == "ctrl+p"):
                            keyboard.press(Key.ctrl)
                            keyboard.press("p")
                            keyboard.release(Key.ctrl)

                        elif (datas[2] == "ctrl+w"):
                            keyboard.press(Key.ctrl)
                            keyboard.press("w")
                            keyboard.release(Key.ctrl)

                        elif (datas[2] == "alt+f4"):
                            keyboard.press(Key.alt)
                            keyboard.press(Key.f4)
                            keyboard.release(Key.alt)

                        elif (datas[2] == "enter"):
                            keyboard.press(Key.enter)

                    else:
                        if(datas[1] == ""):
                            keyboard.press("/")
                        keyboard.press(datas[1])
                        keyboard.release(datas[1])

        else:
            s.close()
            print("wifi baglanti bekleniyor")
            client_sock, address = serversocket.accept()
            print("baglanti saglandi")

    except Exception as e:
        print("error:")
        print(e)
        pass
