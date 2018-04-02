import socket
import pyqrcode
import bluetooth


def createWifi():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
    url = pyqrcode.create(s.getsockname()[0])
    url.png('wifi.png', scale=10)
    s.close()

def createBluetooth():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", bluetooth.PORT_ANY))

    macAddress=server_sock.getsockname()[0]
    print(macAddress)
    print("--------------")
    url = pyqrcode.create(macAddress)
    url.png('bluetooth.png', scale=10)

createBluetooth()
createWifi()