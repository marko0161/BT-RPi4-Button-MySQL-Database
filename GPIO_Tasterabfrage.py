import RPi.GPIO as GPIO #GPIO Library um Pins anzusteuern
import time             #Library für Verzögerungsfunktionen

GPIO.setmode(GPIO.BCM)  #GPIO Pins sollen mit der GPIO Nummerierung angesprochen werden
GPIO.setup(23, GPIO.OUT)#GPIO Pin 23 soll als Output definiert werden
GPIO.setup(24,GPIO.IN)

#Beispiel: Bei Tastendruck LED leuchten lassen
# Endlosschleife
while True:
    if GPIO.input(24) == 0:
        # Ausschalten
        GPIO.output(23, GPIO.LOW)
    else:
        # Einschalten
        GPIO.output(23, GPIO.HIGH)
    time.sleep(0.1)
