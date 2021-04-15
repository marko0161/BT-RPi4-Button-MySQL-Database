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

pip install pybluez <br>
--> sudo apt-get install apache2 <br>
--> sudo apt-get -y install mariadb-server-10.0 php7.3-mysql mariadb-client-10.0 <br>
--> sudo apt-get install php5-mysql libapache2-mod-auth-mysql phpMyAdmin <br>

sudo apt install mariadb-server <br>
--> Danach kann ein Passwort gefragt werden <br>
--> Geben sie ein Passwort ein <br>
--> Falls kein passwort benötigt wird <br>
--> Bedeutet dass das  sie ohne Passwort zugreifen können <br>

Um den Mysql Prozess zu starten wird der Befehl sudo mysql_secure_installation benötigt <br>
-->	Passwort eintippen <br>
-->	Falls du noch kein Passwort besitzt gebe ein neues Passwort <br> 
-->	! PASSWORT AUFSCHREIBEN <br>

sudo mysql -u root -p <br>
-->	Passwort eingeben <br>
-->	Datenbank erstellen <br>
 ![grafik](https://user-images.githubusercontent.com/71693193/114920914-40541780-9e2a-11eb-962a-1a680ed8a684.png) <br>
-->	Mit quit kann man die Datenbank dann verlassen <br>
-->	Oder man kann mit CTRL +D verlassen <br>

Wie installiere ich mysql connector für python <br> 
Die folgenden Befehle eingeben <br>
-->	PYTHON 2 <br>
-->	sudo pip install mysql-connector-python <br>
-->	PYtHON 3 <br>
-->	sudo pip3 install mysql-connector-python <br>

Wo habe ich nun Zugriff auf phpmaydmin <br>
-->	Sudo apt install phpmaydmin <br>
![grafik](https://user-images.githubusercontent.com/71693193/114921021-611c6d00-9e2a-11eb-8484-9c6211a2f2cc.png) <br>
-->	PHP myadmin konfigurieren <br>
-->	Sudo apt-get install phpmyadmin <br>
![grafik](https://user-images.githubusercontent.com/71693193/114921074-71344c80-9e2a-11eb-9894-32014cd2d4a3.png) <br>
-->	Apache auswählen <br>
-->	Passwort eintippen <br>
-->	Passwort aufschreiben <br>

Eine Möglichkeit apache webserver mit phpmyadmin zu verbinden <br>
![grafik](https://user-images.githubusercontent.com/71693193/114921168-8ad59400-9e2a-11eb-80fe-2acc6b5e6806.png) <br>
-->	Ip adresse herausfinden <br>
![grafik](https://user-images.githubusercontent.com/71693193/114921213-9759ec80-9e2a-11eb-8abc-aafba1d90b1d.png) <br>
-->	In diesem Fall ist die IP-Adresse 192.168.1.8 <br>







