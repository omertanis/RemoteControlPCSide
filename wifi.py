import socket
from qrCreator import ipadress
import time
print("waiting")
serversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind((ipadress, 8089))
# serversocket.listen(5) # become a server socket, maximum 5 connections
# connection, address = serversocket.accept()
# print 'Connection address:', address

while True:
    try:
        data, addr = serversocket.recvfrom(64)
        if data != "":
            time.sleep(0.012)
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
                else:

                    mouseX, mouseY = (mouse.position)
                    mouse.position = (mouseX + (int(datas[1]) / 5), (mouseY + int(datas[2]) / 5))
            # if keyboard
            else:
                from pynput.keyboard import Key, Controller

                keyboard = Controller()
                if (datas[0]) == "Backspace":
                    keyboard.press(Key.backspace)
                else:
                    keyboard.press(datas[0])
                    keyboard.release(datas[0])

        else:
            print "connection lost"
            client_sock, address = serversocket.accept()
            print "Accepted connection from ", address
    except Exception as e:
        print(e)
        pass
