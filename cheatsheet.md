# Cheatsheet für Turtle Graphics mit Python

Vollständige und ausführliche Dokumentation:
[https://docs.python.org/3/library/turtle.html](https://docs.python.org/3/library/turtle.html)

Für Turtle Graphics musst du auf repl.it ein neues repl erstellen. 
Als Sprache muss dafür "Python (with Turtle)" ausgewählt werden.

## Getting Started

```python
import turtle
tina = turtle.Turtle()

tina.color("blue") # black, red, green, yellow, pink ...
tina.shape("turtle") # "arrow", "turtle", "circle", "square", "classic"
```

## Basisbewegungen

```python
tina.forward(100)
tina.backward(100)
tina.left(90) # Angabe in Grad
tina.right(90) # Angabe in Grad
tina.goto(0,0) # goto(x,y)
```

## Geschwindigkeit ändern

```python
tina.speed("normal") # "fastest", "fast", "normal", "slow", "slowest"
```

## Stift verändern

```python
tina.penup() # Stift anheben
tina.pendown() # Stift senken
tina.pensize(10) # Dicke des Stifts. Standard=1
```

## Kreise zeichnen

```python
tina.circle(100) # circle(radius) 
tina.circle(100, 180) # circle(radius, winkel)

tina.begin_fill() # Kreis füllen beginnen
tina.circle(100)
tina.end_fill() # Kreis füllen beenden
```

## Texte schreiben

```python
tina.write("text",align="center") # align kann “left”, “center” oder right” sein
```

## Aktuelle Position abfragen

```python
tina.pos() # gibt Vektor mit (x, y) zurück
tina.xcor() # gibt x Koordinate zurück
tiny.ycor() # gibt y Koordinate zurück
```

## Variablen

```python
square_color = "blue" # Texte stehen in Anführungszeichen
square_size = 10 # Zahlen stehen nicht in Anführungszeichen
```

## for-Schleife

```python
# Mit der Schleife wird ein Quadrat gezeichnet
for count in range(4): # Schleife wird 4 mal ausgeführt
    tina.forward(50)
    tina.left(90)
```

## Listen

```python
# Jede der vier Seiten des Quadrats hat eine andere Farbe
colors = ['red', 'purple', 'blue', 'green']
for i in range(4):
    tina.color(colors[i]) 
    tina.forward(100) 
    tina.left(90)
```

## Funktionen

```python
# Funktion, die Quadrate mit der Seitenlänge 50 zeichnet
def square():
  for count in range(4):
    tina.forward(50)
    tina.left(90)

square() # Aufruf der Funktion
```

```python
# Funktion, die Quadrate unterschiedlicher Seitenlänge zeichnet
# Es wird der Parameter "size" verwendet
def square(size):
  for count in range(4):
    tina.forward(size)
    tina.left(90)

square(100) # Aufruf der Funktion
```

## Bedingungen (if-Abfragen)

```python
a = 5
b = 9

if a > b :
  print("a ist größer als b") # wird nicht ausgeführt
if a < b :
  print("a ist kleiner als b") # wird ausgeführt, da 5 < 9
```

## Operatoren

| Operator          | Bezeichnung |
| ------------- | ----- |
| ```+```, ```-``` | Addition, Subtraktion |
| ```*```, ```/```, ```%``` | Multiplikation, Subtraktion, Modulo (Rest) |

### Vergleichsoperatoren

| Operator          | Bezeichnung |
| ------------- | ----- |
| ```<```, ```<=```  | "Kleiner" und "Kleiner Gleich" |
| ```>```, ```>=``` | "Größer" und "Größer Gleich" |
| ```==``` | Gleichheit |
| ```!=``` | Ungleichheit |

## Zufallszahlen

```python
from random import randint

untere_grenze = 5
obere_grenze = 10

randint(untere_grenze,obere_grenze)
```

