import bluetooth        #BT-Library schon auf RPI vorinstalliert
import RPi.GPIO as GPIO #GPIO Library um Pins anzusteuern
import time             #Library für Verzögerungsfunktionen

GPIO.setmode(GPIO.BCM)  #GPIO Pins sollen mit der GPIO Nummerierung angesprochen werden
GPIO.setup(24,GPIO.IN)


serverMACAddress = '00:1f:e1:dd:08:3d'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    
    if GPIO.input(24) == 0:
        # Taster nicht gedrückt
         text = "notpressed"
    else:
        # Taster gedrückt
        text = "pressed"
    s.send(text)
    time.sleep(0.1)
sock.close()

