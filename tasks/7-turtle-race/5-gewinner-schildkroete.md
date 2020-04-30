### >>> Aufgabe 5: Name der Gewinner-Schildkröte ausgeben

**ACHTUNG: ```if```-statement sollte vor der Aufgabe kurz erklärt werden**

Um in Python zu überprüfen, ob Wert A größer als Wert B ist, gibt es ```if```-Anweisungen. 
Schreibe das nachfolgende Beispiel ab und schau welcher Text ausgegeben wird. 
Ändere den Wert ```a``` auf 10 und schau wie sich die Textausgabe verändert. 

Probiere statt "Größer" ```>``` und "Kleiner" ```<``` auch "Größer gleich" ```>=``` 
und "Kleiner gleich" ```<=``` aus.

```python
a = 5
b = 9

if( a > b ):
  print("a ist größer als b")
if( a < b ):
  print("a ist kleiner als b")  
```



Wir möchten nun den Namen der Schildkröte ausgeben, die als erstes die Ziellinie erreicht. 
Dazu erweitern wir die ```for```-Schleife aus Aufgabe 3 und packen diese 
in die Funktion ```startRace()```.

Nachdem sich eine Schildkröte fortbewegt hat, überprüfen wir jedes Mal, 
ob die Schildkröte bereits die Ziellinie erreicht hat. 

Wir wissen, dass die Zielline bei x=200 liegt. Die aktuelle Position einer Schildkröte 
auf der x-Achse können wir mit ```xcor()``` abfragen. Wenn wir nun nach 
jedem mal ```forward()``` abfragen, ob die x-Koordinate der Schildkröte größer als 
die x-Koordinate der Ziellinie ist, wissen wir wann die Schildkröte über der Ziellinie ist. 
In der  ```if```-Abfrage geben wir mit ```print("XYZ hat gewonnen!")``` den Namen der 
Gewinner-Schildkröte aus.

Füge die gerade eben erstellte ```if```-Abfrage nach jedem ```forward()``` von 
den 3 Schildkröten ein. Damit die Schildkröten nicht weiterlaufen, müssen wir 
die ```startRace```-Funktion verlassen. Füge hierzu noch jeweils an das Ende der 
drei ```if```-Anweisungen ein ```return```.

Nun fehlt nur noch der Aufruf der Funktion ```startRace()```. 