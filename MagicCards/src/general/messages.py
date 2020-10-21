from psychopy import visual
from general.config_hardware import WIN

messages = {
### early, late, blacscreen ###
    "early": "Zu früh!",
    "late": "Zu spät!",
    "blackscreen": "",

### welcome ###
    "welcome": """Herzlich Willkommen zum Experiment!

Vor dir liegt ein Stapel mit Karten. Bitte wähle eine Karte.



WEITER mit RECHTS (press RIGHT to CONTINUE)""",

### explanation_initial ###
    "explanation_initial_yes_right": """Bitte lege nun deine ZEIGEFINGER auf die beiden Tasten vor dir.
Bei diesem Experiment musst du möglichst schnell reagieren.

Im Folgenden werden dir einige Begriffe auf dem Bildschirm angezeigt.
Deine Aufgabe ist es, zu entscheiden, ob es auf der Karte vor dir etwas gibt, das dem Begriff entspricht.
Wenn also z.B. das Wort "Blüte" erscheint, sollst du entscheiden, ob auf der Karte eine Blüte zu sehen ist.

Um deine Entscheidung mitzuteilen, benutze bitte die folgenden Tasten:


    es gibt etwas, dass dem Begriff entspricht:
        RECHTE TASTE

    es gibt nichts, dass dem Begriff entspricht:
        LINKE TASTE


HAST DU NOCH FRAGEN?
Dann wende dich bitte an den Versuchsleiter.


WEITER mit RECHTS (press RIGHT to CONTINUE)""",

    "explanation_initial_yes_left": """Bitte lege nun deine ZEIGEFINGER auf die beiden Tasten vor dir.
Bei diesem Experiment musst du möglichst schnell reagieren.

Im Folgenden werden dir einige Begriffe auf dem Bildschirm angezeigt.
Deine Aufgabe ist es, zu entscheiden, ob es auf der Karte vor dir etwas gibt, das dem Begriff entspricht.
Wenn also z.B. das Wort "Blüte" erscheint, sollst du entscheiden, ob auf der Karte eine Blüte zu sehen ist.

Um deine Entscheidung mitzuteilen, benutze bitte die folgenden Tasten:


    es gibt etwas, dass dem Begriff entspricht:
        LINKE TASTE

    es gibt nichts, dass dem Begriff entspricht:
        RECHTE TASTE


HAST DU NOCH FRAGEN?
Dann wende dich bitte an den Versuchsleiter.


WEITER mit RECHTS (press RIGHT to CONTINUE)""",

### practice ###
    "practice": """Zunächst ein paar Fragen zum Üben.


WEITER mit RECHTS""",

### practice_ready ###
    "practice_ready": """Bitte sag dem Versuchsleiter Bescheid, wenn du bereit bist,


DANACH: Weiter mit RECHTS""" ,

### choose_ready ###
    "choose_ready": """Wähle eine neue Karte und sag dem Versuchsleiter Bescheid, wenn du bereit bist


DANACH: Weiter mit RECHTS""" ,

### initialization ###
    "initialization": """Experiment wird initialisiert.

Dies kann einen Moment dauern.""",

### ready to start ###
    "start_ready": """Einrichtung abgeschlossen.


Zum STARTEN: RECHTS""",

### explanation_remember ###
    "explanation_remember_yes_right": """Something, something, something...

        Zur Erinnerung:

        es gibt etwas, dass dem Begriff entspricht:
        RECHTE TASTE

        es gibt nichts, dass dem Begriff entspricht:
        LINKE TASTE


    HAST DU NOCH FRAGEN?
    Dann wende dich bitte an den Versuchsleiter.


    WEITER mit RECHTS (press RIGHT to CONTINUE)""",

    "explanation_remember_yes_left": """Something, something, something...

        Zur Erinnerung:

        es gibt etwas, dass dem Begriff entspricht:
        LINKE TASTE

        es gibt nichts, dass dem Begriff entspricht:
        RECHTE TASTE


    HAST DU NOCH FRAGEN?
    Dann wende dich bitte an den Versuchsleiter.


    WEITER mit RECHTS (press RIGHT to CONTINUE)""",

### calibration ###
    "calibration": "Kalibrierung des Eyetrackers \n\nSTARTEN mit RECHTS",

### the card was probably ###
    "card_image": "Die Karte war wahrscheinlich:",

### was this the correct card?  ###
    "card_correct_right": """War das die richtige Karte?

        Falls ja:
        RECHTE TASTE

        Falls nein:
        LINKE TASTE""",

    "card_correct_left": """War das die richtige Karte?

        Falls ja:
        LINKE TASTE

        Falls nein:
        RECHTE TASTE""",



### thanks ###
    "thanks": """
GESCHAFFT!

Vielen Dank für deine Teilnahme!

Fülle jetzt bitte noch kurz den Nachbefragungszettel aus, den dir der Versuchsleiter gibt.
"""
}


def present_message(msg):
    message = visual.TextStim(WIN, text=messages[msg], pos=[0, 0], alignHoriz='center')
    message.draw()
    WIN.flip()
