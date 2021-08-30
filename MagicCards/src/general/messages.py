from psychopy import visual
from general.config_hardware import WIN

messages = {
### early, late, blacscreen ###
    "early": "Zu früh!",
    "late": "Zu spät!",
    "blackscreen": "",

### welcome ###
    "welcome": """Herzlich Willkommen zum Experiment!

In diesem Experiment wollen wir menschliches Lügen untersuchen und herausfinden, ob ein Algorithmus trainiert werden kann, festzustellen, ob eine bestimmte Person lügt. Um dies zu untersuchen, werden wir dich bitten, dir einige Spielkarten anzuschauen und anschließend für den Computer zu beschreiben. Dabei sollst du manchmal die Wahrheit sagen und manchmal lügen.

Nach einigen Fragen werden wir dich dann jeweils bitten, nochmal anzugeben, bei welchen Fragen du gelogen hast, damit wir den Algorithmus basierend auf deinen Informationen anpassen können.


WEITER mit RECHTS (press RIGHT to CONTINUE)""",

    "welcome_2": """Wir haben die Spielkarten bewusst so gewählt, dass diese vielfältige Fragen erlauben, aber keinerlei Aussagen über dich persönlich ermöglichen. Das heißt, der Computer kann aus deinen Antworten KEINE persönlichen Informationen über dich herausfinden. Weiterhin werden alle Daten komplett anonymisiert gespeichert, so dass nach Abschluss des Experiments keine Verbindung zwischen dir und deinen Daten hergestellt werden kann.

Für unser Experiment ist es essentiell, dass du ganz natürlich antwortest und uns bei Rückfragen zu den Fragen, bei denen du gelogen hast, die Wahrheit sagst!

Bitte bestätige der Versuchleitung, dass du diese Informationen zur Kenntnis genommen hast.


STARTEN mit RECHTS""",

    "welcome_3": """Vor dir liegt ein Stapel mit Spielkarten. Aus diesem Kartenstapel wirst du im Verlauf des Experiments nach und nach mehrere Spielkarten ziehen und anschließend Fragen zu diesen beantworten. Die Fragen beziehen sich immer darauf, ob bestimmte Elemente auf der Spielkarte enthalten sind (z.B. Personen, bestimmte Gegenstände, bestimmte Landschaftsmerkmale). Wenn du eine Spielkarte gezogen hast, schau sie dir bitte ganz genau an und nimm dir Zeit, um dir zu merken, was abgebildet ist. Während die Fragen zur Spielkarte gestellt werden, wirst du nicht nochmal auf die Karte schauen können.


WEITER mit RECHTS""",

    "welcome_4": """Bitte wähle jetzt für die Übung eine Spielkarte,schaue dir genau an, was auf ihr abgebildet ist und merke dir so gut du kanns, was auf der Spielkarte abgebildet ist.

Wenn du damit fertig bist, lege die Spielkarte offen nach rechts auf den Ablagebereich, damit du sie nicht versehentlich später nochmal ziehst.



WEITER mit RECHTS""",


### explanation_initial ###
    "explanation_initial_general": """Bitte lege nun deinen RECHTEN und LINKEN ZEIGEFINGER auf die beiden markierten Tasten vor dir. Um die Fragen zu den Spielkarten zu beantworten, wirst du jeweils eine der beiden Tasten so schnell wie möglich drücken. Bitte vermeide dabei Fehler.

Der Computer stellt dir in Fragen zu deiner Spielkarte, indem jeweils ein Begriff auf dem Bildschirm angezeigt wird (z.B. bestimmte Gegenstände, bestimmte Landschaftsmerkmale).
Deine Aufgabe ist es, zu entscheiden, ob das entsprechende Merkmal auf deiner Spielkarte enthalten ist. Wenn beispielsweise das Wort "Blüte" erscheint, sollst du entscheiden, ob auf der Spielkarte an irgendeiner Stelle eine Blüte zu sehen ist.

Antworte dabei immer so schnell und richtig wie möglich!


WEITER mit RECHTS""",





    "explanation_initial_yes_right": """Um deine Antwort mitzuteilen, antworte bitte wie folgt:
Wenn das im Begriff beschriebene MERKMAL auf der Spielkarte vorkommt, drücke bitte so schnell wie möglich die RECHTE TASTE.
Wenn das im Begriff beschriebene MERKMAL auf der Spielkarte NICHT vorkommt, drücke bitte so schnell wie möglich die LINKE TASTE.


WEITER mit RECHTS""",

    "explanation_initial_yes_left": """Um deine Antwort mitzuteilen, antworte bitte wie folgt:
Wenn das im Begriff beschriebene MERKMAL auf der Spielkarte vorkommt, drücke bitte so schnell wie möglich die LINKE TASTE.
Wenn das im Begriff beschriebene MERKMAL auf der Spielkarte NICHT vorkommt, drücke bitte so schnell wie möglich die RECHTE TASTE.


WEITER mit RECHTS""",

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

    "test":""" 123 123 123 test size""",
### explanation_remember ###
    "explanation_remember_yes_right": """
        Zur Erinnerung:

        Bei diesem Experiment musst du möglichst schnell reagieren.

        Deine Aufgabe ist es, zu entscheiden, ob es auf der Karte vor dir etwas gibt, das dem Begriff entspricht. Wenn also z.B. das Wort "Blüte" erscheint, sollst du entscheiden, ob auf der Karte eine Blüte zu sehen ist.

        ABER: du kannst und sollst auch BLUFFEN. Bitte entscheide dafür zu ungefähr einem Drittel der Begriffe anders, als eigentlich richtig wäre.

        Um deine Entscheidung mitzuteilen, benutze bitte die folgenden Tasten:

        es gibt etwas, dass dem Begriff entspricht:
        RECHTE TASTE

        es gibt nichts, dass dem Begriff entspricht:
        LINKE TASTE


    HAST DU NOCH FRAGEN?
    Dann wende dich bitte an den Versuchsleiter.


    WEITER mit RECHTS (press RIGHT to CONTINUE)""",

    "explanation_remember_yes_left": """
        Zur Erinnerung:

        Bei diesem Experiment musst du möglichst schnell reagieren.

        Deine Aufgabe ist es, zu entscheiden, ob es auf der Karte vor dir etwas gibt, das dem Begriff entspricht. Wenn also z.B. das Wort "Blüte" erscheint, sollst du entscheiden, ob auf der Karte eine Blüte zu sehen ist.

        ABER: du kannst und sollst auch BLUFFEN. Bitte entscheide dafür zu ungefähr einem Drittel der Begriffe anders, als eigentlich richtig wäre.

        Um deine Entscheidung mitzuteilen, benutze bitte die folgenden Tasten:

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


### was this the correct card?  ###
    "unintentional_response_right": """Hast du bei irgendeinem Wort versehentlich anders reagiert, als du es wolltest?

        Falls ja:
        RECHTE TASTE

        Falls nein:
        LINKE TASTE""",

    "unintentional_response_left": """Hast du bei irgendeinem Wort versehentlich anders reagiert, als du es wolltest?

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
    message = visual.TextStim(WIN, text=messages[msg], pos=[0, 0], alignHoriz='center', wrapWidth=40)
    message.draw()
    WIN.flip()
