from psychopy import visual
from general.config_hardware import WIN
import general.variables as variables


### A form asking which responses were unintentional ###
def formUnintentional(wordlist):
    numQuestions = len(wordlist)
    surveyDicts = []
    i = 1
    j = i - 1

    for question in range(0, (numQuestions)):
        questionDict = {"index": i, "itemText": wordlist[j], "itemWidth": 0.05, "type": "choice", "responseWidth": 0.4, "options": ["kein Versehen", "Versehen"], "ticks": [1,2], 'markerColor': [0.89, -0.35, -0.50], "layout": "horiz"}
        surveyDicts.append(questionDict)
        i += 1
        j += 1

    survey = visual.Form(WIN, name='default', items=surveyDicts, size=(1.2, 1.0), pos=(0.0, 0.0), itemPadding=0.008, textHeight= 0.015 , autoLog=True)
    survey.autoDraw = True
    descript = visual.TextStim(WIN, text="Bestätigen mit RECHTER TASTE", pos=(0,-10))
    descript.autoDraw = True
    WIN.flip(clearBuffer=False)

    variables.io.clearEvents(device_label='all')  # Flushing the buffer.

    while True:
        WIN.flip(clearBuffer=False)
        keyboardActivity = variables.io.devices.keyboard.getKeys()  # check for any keypress
        if not keyboardActivity == [] and keyboardActivity[0].key == 'l':  # if 'l' key pressed
            numAnswers = 0
            for question in range(0, (numQuestions)):
                if survey.getData()[question]['response'] != None:
                    numAnswers += 1
            if numAnswers == numQuestions:  # If there is an answer to every question
                answers = []
                for question in range(0, (numQuestions)):
                    answers.append(survey.getData()[question]['response'])
                break

    survey.autoDraw = False
    descript.autoDraw = False
    WIN.flip(clearBuffer=True)
    print(answers)  # For testing only
    return answers
    #print(survey.getData())  # For testing only
    #return survey.getData()  # For getting the full survey data (it's a lot...) 
