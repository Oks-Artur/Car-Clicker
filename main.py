import turtle

# Bildschirm erstellen und konfigurieren
wn = turtle.Screen()
wn.title("Car Clicker Game")
wn.bgcolor("blue")

# Bilder (GIFs) für Formen registrieren
wn.register_shape("Car.gif")
wn.register_shape("button.gif")

# Auto-Turtle erstellen und konfigurieren
car = turtle.Turtle()
car.shape("Car.gif")
car.speed(0)

# Button-Turtle erstellen und positionieren
button = turtle.Turtle()
button.shape("button.gif")
button.speed(0)
button.penup()
button.setpos(175, -175)

# Spielvariablen initialisieren
Kilometer = 0
auto_clickers = 0
auto_clicker_cost = 50

# Anzeige-Turtle für Kilometerstand erstellen
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"Kilometer: {Kilometer}", align="center", font=("Arial", 32, "normal"))

# Funktion: Wenn Auto geklickt wird, Kilometer erhöhen
def clicked(x, y):
    global Kilometer
    Kilometer += 1
    update_display()

# Funktion: Anzeige aktualisieren
def update_display():
    pen.clear()
    pen.write(f"Kilometer: {Kilometer}", align="center", font=("Arial", 32, "normal"))

# Klick-Ereignis für Auto setzen
car.onclick(clicked)

# Funktion: Autoklicker kaufen, wenn genug Kilometer vorhanden sind
def buy_auto_clicker(x, y):
    global Kilometer, auto_clickers, auto_clicker_cost
    if Kilometer >= auto_clicker_cost:
        Kilometer -= auto_clicker_cost
        auto_clickers += 1
        update_display()

# Funktion: Spielzustand regelmäßig aktualisieren (automatische Klicks)
def update_game_state():
    global Kilometer, auto_clickers
    Kilometer += auto_clickers
    update_display()
    wn.ontimer(update_game_state, 1000)  # Wiederhole jede Sekunde

# Automatische Aktualisierung starten
wn.tracer()  # Deaktiviert automatisches Zeichnen für Performance
update_game_state()

# Klick-Ereignis für Button setzen
button.onclick(buy_auto_clicker)

# Erstes Zeichnen auslösen
wn.update()

# Hauptspielschleife starten
wn.mainloop()
