import bluetooth
import time
# -*- coding: utf-8 -*-

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
server_sock.bind(("",bluetooth.PORT_ANY))
server_sock.listen(1)

print("anan")
print server_sock
bluetooth.advertise_service(server_sock, "helloService",
                     service_classes=[bluetooth.SERIAL_PORT_CLASS],
                     profiles=[bluetooth.SERIAL_PORT_PROFILE])

print("bluetooth baglanti bekleniyor...")
print(server_sock.getsockname()[0])
client_sock, address = server_sock.accept()
print "Accepted connection from ",address

while True:
    try:
        data = client_sock.recv(64)
        if data != "":
            time.sleep(0.0075)
            datas = []
            datas = data.split("/")

            # if mouse
            if(datas[0] == "mouse"):
                from pynput.mouse import Button, Controller
                print(data)

                mouse = Controller()
                if(datas[1] == "left"):
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                elif(datas[1] == "right"):
                    mouse.press(Button.right)
                    mouse.release(Button.right)
                elif(datas[1] == "scroll"):
                    mouse.scroll(0, int(datas[2]))
                else:
                    mouseX, mouseY = (mouse.position)
                    mouse.position = (mouseX + (int(datas[1])/10), (mouseY +int(datas[2])/10))
            # if keyboard
            else:
                from pynput.keyboard import Key, Controller
                keyboard = Controller()
                if (datas[0]) == "Backspace":
                    keyboard.press(Key.backspace)
                elif(datas[0]) == "Enter":
                    keyboard.press(Key.enter)
                else:
                    keyboard.press(datas[0])
                    keyboard.release(datas[0])

        else:
            print("bluetooth baglanti bekleniyor...")
            client_sock, address = server_sock.accept()
            print "Accepted connection from ", address
    except Exception as e:
        print(e)
        pass


