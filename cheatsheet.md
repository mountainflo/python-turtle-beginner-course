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

tina.begin_fill() # Kreis ausfüllen
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


