### >>> Aufgabe 3: Schildkröten um Zufallswert bewegen

In einer Schleife, die wir 150 mal durchlaufen, lassen wir nun die Schildkröten 
um einen Zufallswert zwischen 1 und 5 nach vorne bewegen.

Zufallswerte können mit ```randint(a,b)``` erstellt werden.  ```a``` ist die untere 
Grenze und ```b```  die obere Grenze zwischen denen der Zufallswert liegen soll. 
Für unser Spiel brauchen wir somit ```randint(1,5)```.

Weil ```randint(a,b)``` nicht standardmäßig vorhanden ist, müssen wir es erst mit der 
folgenden Zeile importieren:

```python
from random import randint
```

Du hast nun die erste einfache Version des Spiels fertig. Starte das Programm 
und schaue welche Schildkröte am Ende vorne liegt.