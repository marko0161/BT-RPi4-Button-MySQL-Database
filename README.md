# BT-RPi4-Button-MySQL-Database
This repository contains a Raspberry Pi 4 Bluetooth project to send data between two Raspberrys and to save the data in a MySQL Database.
## Inhalt
1. [Allgemeines](#general-info)
2. [Installationsschritte](#installationen)
3. [Installation](#installation)
4. [Collaboration](#collaboration)
5. [FAQs](#faqs)

## [Allgemeines](#general-info)
In diesem README wird angegeben, welche Bibliotheken auf dem Raspberry Pi 4 Model B installiert werden müssen, damit das Projekt nachgestellt werden kann. Zusätzlich findet man hier auch alle nötigen Verweise zu Dateien und Codes, welche ebenfalls im repository hinterlegt sind.

## [Installationsschritte](#installationen)
Im folgenden sieht man einige Befehle, die man im CLI ausführen muss, damit die nötigen Bibliotheken installiert werden:

pip install pybluez
sudo apt-get install apache2
sudo apt-get -y install mariadb-server-10.0 php7.3-mysql mariadb-client-10.0
Sudo apt-get install php5-mysql libapache2-mod-auth-mysql phpMyAdmin

sudo apt install mariadb-server
--> Danach kann ein Passwort gefragt werden
--> Geben sie ein Passwort ein 
--> Falls kein passwort benötigt wird 
--> Bedeutet dass das  sie ohne Passwort zugreifen können

Um den Mysql Prozess zu starten wird der Befehl sudo mysql_secure_installation benötigt
-->	Passwort eintippen 
-->	Falls du noch kein Passwort besitzt gebe ein neues Passwort 
-->	! PASSWORT AUFSCHREIBEN

sudo mysql -u root -p
-->	Passwort eingeben
-->	Datenbank erstellen
 ![grafik](https://user-images.githubusercontent.com/71693193/114920914-40541780-9e2a-11eb-962a-1a680ed8a684.png)
-->	Mit quit kann man die Datenbank dann verlassen
-->	Oder man kann mit CTRL +D verlassen

Wie installiere ich mysql connector für python 
Die folgenden Befehle eingeben
-->	PYTHON 2
-->	sudo pip install mysql-connector-python
-->	PYtHON 3
-->	sudo pip3 install mysql-connector-python

Wo habe ich nun Zugriff auf phpmaydmin 
-->	Sudo apt install phpmaydmin
![grafik](https://user-images.githubusercontent.com/71693193/114921021-611c6d00-9e2a-11eb-8484-9c6211a2f2cc.png)
-->	PHP myadmin konfigurieren 
-->	Sudo apt-get install phpmyadmin
![grafik](https://user-images.githubusercontent.com/71693193/114921074-71344c80-9e2a-11eb-9894-32014cd2d4a3.png)
-->	Apache auswählen
-->	Passwort eintippen 
-->	Passwort aufschreiben

Eine Möglichkeit apache webserver mit phpmyadmin zu verbinden
![grafik](https://user-images.githubusercontent.com/71693193/114921168-8ad59400-9e2a-11eb-80fe-2acc6b5e6806.png)
-->	Ip adresse herausfinden
![grafik](https://user-images.githubusercontent.com/71693193/114921213-9759ec80-9e2a-11eb-8abc-aafba1d90b1d.png)
-->	In diesem Fall ist die IP-Adresse 192.168.1.8







