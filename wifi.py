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
            # if keyboard
            else:
                from pynput.keyboard import Key, Controller

                keyboard = Controller()
                if (datas[0]) == "Backspace":
                    keyboard.press(Key.backspace)
                elif (datas[0]) == "Enter":
                    keyboard.press(Key.enter)
                else:
                    keyboard.press(datas[0])
                    keyboard.release(datas[0])

        else:
            s.close()
            print("wifi baglanti bekleniyor")
            client_sock, address = serversocket.accept()
            print("baglanti saglandi")

    except Exception as e:
        print(e)
        pass
