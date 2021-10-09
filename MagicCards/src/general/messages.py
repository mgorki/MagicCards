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


WEITER mit RECHTS""",

    "welcome_2": """Wir haben die Spielkarten bewusst so gewählt, dass diese vielfältige Fragen erlauben, aber keinerlei Aussagen über dich persönlich ermöglichen. Das heißt, der Computer kann aus deinen Antworten KEINE persönlichen Informationen über dich herausfinden. Weiterhin werden alle Daten komplett anonymisiert gespeichert, so dass nach Abschluss des Experiments keine Verbindung zwischen dir und deinen Daten hergestellt werden kann.

Für unser Experiment ist es essentiell, dass du ganz natürlich antwortest und uns bei Rückfragen zu den Fragen, bei denen du gelogen hast, die Wahrheit sagst!

Bitte bestätige der Versuchleitung, dass du diese Informationen zur Kenntnis genommen hast.


STARTEN mit RECHTS""",

    "welcome_3": """Vor dir liegt ein Stapel mit Spielkarten. Aus diesem Kartenstapel wirst du im Verlauf des Experiments nach und nach mehrere Spielkarten ziehen und anschließend Fragen zu diesen beantworten. Die Fragen beziehen sich immer darauf, ob bestimmte Elemente auf der Spielkarte enthalten sind (z.B. Personen, bestimmte Gegenstände, bestimmte Landschaftsmerkmale). Wenn du eine Spielkarte gezogen hast, schau sie dir bitte ganz genau an und nimm dir Zeit, um dir zu merken, was abgebildet ist. Während die Fragen zur Spielkarte gestellt werden, wirst du nicht nochmal auf die Karte schauen können.


WEITER mit RECHTS""",

    "welcome_4": """Bitte wähle jetzt für die Übung eine Spielkarte, schaue dir genau an, was auf ihr abgebildet ist und merke dir so gut du kannst, was auf der Spielkarte abgebildet ist.

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


    "explanation_initial_important": """WICHTIG!

Beim Beantworten der Fragen sollst du selbst wählen, wann du die Wahrheit sagst und wann du lügst. Mit Lügen ist hierbei gemeint, dass du bewusst und absichtlich genau die gegenteilige Antwort gibst. Wenn also beispielsweise ein bestimmtes Merkmal auf der Spielkarte enthalten ist, gibst du absichtlich an, dass das Merkmal NICHT enthalten sei.

Wähle bei jeder Frage bitte ganz spontan, als würdest du eine Münze werfen, ob du lügen oder die Wahrheit sagen willst. Bitte triff diese Entscheidung bereits bevor der Begriff erscheint, das heißt während noch das Fixationskreuz + zu sehen ist. Wenn dann der Begriff erscheint, antworte so schnell und richtig wie möglich wahrheitsgemäß bzw. mit einer Lüge, je nachdem, wofür du dich entschieden hast.


WEITER mit RECHTS""",


    "explanation_initial_important_2": """Versuche dabei insgesamt bitte ungefähr gleich oft zu lügen und die Wahrheit zu sagen.

Bitte merke dir, auf welche Frage du gelogen bzw. wahrheitsgemäß geantwortet hast. Du wirst nach einigen Fragen gebeten, dies anzugeben, damit der Algorithmus entsprechend lernen kann.



WEITER mit RECHTS""",



    "explanation_initial_procedure": """Das Experiment läuft so ab, dass jeweils pro Spielkarte mehrere Fragen direkt nacheinander gestellt werden. Nach deiner Antwort siehst du als Bestätigung kurz einen farbigen Kreis. Danach erscheint das nächste Fixationskreuz + und darauf folgt der nächste Begriff.

Wähle jeweils, wie beschrieben schon beim Fixationskreuz +, wo du lügen oder die Wahrheit sagen willst und antworte dann so schnell und richtig wie möglich, sobald der Begriff erscheint.


WEITER mit RECHTS""",


    "explanation_initial_procedure_2": """Nach einigen Begriffen wirst du gebeten, anzugeben bei welchen Fragen/Begriffen du gelogen bzw. die Wahrheit gesagt hast. Dazu siehst du eine List der Begriffe in der Reihenfolge, in der sie erschienen sind. Verwende bitte die Maus, um anzugeben, ob du für den jeweiligen Begriff gelogen („Lüge“) oder die Wahrheit gesagt („Wahrheit“) hast. Falls du bei einem Begriff versehentlich einen Fehler gemacht und dich vertippt hast, wähle bitte „Fehler“. Im Fall, dass du dich für einen Begriff nicht mehr erinnern kannst, wähle bitte die Option „vergessen“ aus.

Nachdem du alle Begriffe eingeordnet hast, kannst du eine Pause machen und anschließend mit der nächsten Spielkarte fortfahren.

HAST DU FRAGEN?
Dann wende dich bitte jetzt an die Versuchsleitung.


WEITER mit RECHTS""",


### practice ###
    "practice": """Üben wir zunächst mit einer Spielkarte. Nimm dir jetzt bitte nochmal einen Moment Zeit, um dir die Spielkarte, die du vorhin bereits angeschaut hast, nochmal anzusehen und zu merken.
Wenn du dir die Spielkarte gemerkt hast, lege sie bitte offen auf den Ablagestapel, platziere deine Finger auf den Tasten und lege deinen Kopf in die Kinnstütze.

Bevor die Fragen starten wird die Versuchsleitung jetzt und vor den Fragen zu jeder weiteren Spielkarte, den Eye-Tracker auf deine Augen einstellen.


WEITER mit RECHTS""",

### practice_ready ###
    "practice_ready": """Bitte sag der Versuchsleitung Bescheid, wenn du bereit bist,


DANACH: Weiter mit RECHTS""" ,


### practice_finished ###
    "practice_finished": """SUPER!
Du hast die Übung abgeschlossen.

HAST DU NOCH FRAGEN?
Wenn ja, wende dich bitte jetzt an die Versuchsleitung.


WEITER mit RECHTS
""",


### choose_ready ###
    "choose_ready": """Wähle eine neue Spielkarte, betrachte diese genau und merke sie dir.


Fragen STARTEN mit RECHTS""" ,

### initialization ###
    "initialization": """Experiment wird initialisiert.

Dies kann einen Moment dauern.""",

### ready to start ###
    "start_ready": """Einrichtung abgeschlossen.


Zum STARTEN: RECHTS""",

    "test":""" 123 123 123 test size""",


### explanation_remember ###
    "explanation_remember_yes_right": """ERINNERUNG

    +
-> Enscheide! Lüge oder Wahrheit? Wähle beides jeweils ca. gleich oft

Begriff
-> Antworte so schnell und richtig wie möglich!

•	Antwort: MERKMAL vorhanden -> RECHTE TASTE
•	Antwort: MERKMAL NICHTvorhanden <- LINKE TASTE

Merke dir, wann du lügst bzw. die Wahrheit sagst!

Gib nach den Fragen bitte an, für welche Frage du gelogen/die Wahrheit gesagt hast.

    Fragen zur Spielkarte STARTEN mit RECHTS""",

    "explanation_remember_yes_left": """ERINNERUNG

    +
-> Enscheide! Lüge oder Wahrheit? Wähle beides jeweils ca. gleich oft

Begriff
-> Antworte so schnell und richtig wie möglich!

•	Antwort: MERKMAL vorhanden -> LINKE TASTE
•	Antwort: MERKMAL NICHTvorhanden <- RECHTE TASTE

Merke dir, wann du lügst bzw. die Wahrheit sagst!

Gib nach den Fragen bitte an, für welche Frage du gelogen/die Wahrheit gesagt hast.

    Fragen zur Spielkarte STARTEN mit RECHTS""",


### calibration ###
    "calibration": """Bitte folge den Anweisungen der Versuchsleitung zur Einstellung des Eye-Trackers. Merke dir währenddessen deine Spielkarte.""",

### the card was probably ###
    "card_image": "Der Computer vermutet, dass das deine Karte war:",

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
    "thanks": """GESCHAFFT!

Vielen Dank für deine Teilnahme!

Fülle jetzt bitte noch kurz den Nachbefragungszettel aus, den dir die Versuchsleitung gibt.

"""
}


def present_message(msg):
    message = visual.TextStim(WIN, text=messages[msg], pos=[0, 0], alignHoriz='center', wrapWidth=40)
    message.draw()
    WIN.flip()
