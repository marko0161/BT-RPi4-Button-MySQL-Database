import bluetooth        #BT-Library schon auf RPI vorinstalliert
import RPi.GPIO as GPIO #GPIO Library um Pins anzusteuern
import time             #Library für Verzögerungsfunktionen

GPIO.setmode(GPIO.BCM)  #GPIO Pins sollen mit der GPIO Nummerierung angesprochen werden
GPIO.setup(23, GPIO.OUT)#GPIO Pin 23 soll als Output definiert werden

hostMACAddress = '00:1f:e1:dd:08:3d' 
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)

try:
    client, clientInfo = s.accept()
    while 1:                        #bei einer Verbindung werden in jedem Fall Daten gesendet
        data = client.recv(size)
        if data:
            if data == 'pressed':   #wenn defrückt, LED einschalten
                GPIO.output(23, GPIO.HIGH)
            else:
                GPIO.output(23, GPIO.LOW)
except:	# bei keiner Verbindung wird der Socket wieder geschlossen
    print("Closing socket")
    client.close()
    s.close()

