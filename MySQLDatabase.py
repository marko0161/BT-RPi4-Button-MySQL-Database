import RPi.GPIO as GPIO
import time
import mysql.connector
#from connection import connection
#import dht11

#import pymysql

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

for i in range(5):
    GPIO.output(23, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.5)

 #Endlosschleife
while True:
    if GPIO.input(24) == 0:
        # Ausschalten
       GPIO.output(23, GPIO.LOW)
    else:
         #Einschalten
        GPIO.output(23, GPIO.HIGH)
        connection = mysql.connector.connect(host='localhost',
                                                 database='hallo',
                                                 user='username',
                                                 password= 'root')
        counter=1
        counter+=1
        counter= counter+1
   
        mycursor = connection.cursor()
        sql = "INSERT INTO neu (Name,Wert) VALUES (%s, %s)"
        val = ("Taster",counter)
        mycursor.execute(sql,val)

        connection.commit()

        print(mycursor.rowcount, "datenbank ausgeführt.")

