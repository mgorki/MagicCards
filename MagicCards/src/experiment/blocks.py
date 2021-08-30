import random
from psychopy import core, visual, core
#from threading import Thread
from experiment.cards_and_questions import Cards, Questions
from general.init import waitForKey, waitForDecision
from general.config_hardware import tk, dummyMode, WIN
from general.messages import present_message
from experiment.trials import trial
from general.board import card_input#, readSer
from general.questionnaires import formUnintentional
import general.variables as variables
#from general.variables import ser, ITI500, RandomMapping#, q
from experiment.config_experiment import behaviour, trial_max
from experiment.show_image import show_cardimage
import pylink


def checkTrueResponse(word_number, card_number, assignedMapping):  # Function returns whether response is correct or not (boolean)
    if (int(word_number) in (Cards[int(card_number)]["questions_yes"])):  # true if answer should be yes
        trueResponse = assignedMapping["KeyYes"]
    else:
        trueResponse = assignedMapping["KeyNo"]

    return trueResponse


def checkCorrectness(word_number, card_number, data, assignedMapping):  # Function returns whether response is correct or not (boolean)
    trueResponse = checkTrueResponse(word_number, card_number, assignedMapping)
    if data["Response"] == trueResponse:  # True if the actual response matches the correct response
        return True
    else:
        return False


def checkMeaning(key):  # Function returns whether keypress means yes or no
    if key == variables.Mapping["KeyYes"]:  # true if answer should be yes
        meaning = True
    else:
        meaning = False

    return meaning


def sendBehavData(data):
    print(data, file=behaviour)  # prints data to the console and appends it to magic_cards_behaviour.txt
    if not dummyMode:
        tk.sendMessage('TRIALID')
        tk.sendCommand("record_status_message 'Block: %s Trial number: %s'" % (data["BlockNumber"], data["TrialNumber"]))
        tk.sendMessage('!V TRIAL_VAR CardNumber %s' % data["CardNumber"])
        tk.sendMessage('!V TRIAL_VAR TooEarly %s' % data["TooEarly"])
        tk.sendMessage('!V TRIAL_VAR TooSlow %s' % data["TooLate"])
        tk.sendMessage('!V TRIAL_VAR InTime %s' % data["InTime"])
        tk.sendMessage('!V TRIAL_VAR Response %s' % data["Response"])
        tk.sendMessage('!V TRIAL_VAR Stimulus %s' % data["Stimulus"])
        tk.sendMessage('!V TRIAL_VAR RT %s' % data["RTTime"])
        tk.sendMessage('!V TRIAL_VAR Correct %s' % data["ResponseCorrect"])
    else:
        pass

def block(expInfo, practice, block_number):
    ################ Block structure (after choosing a card) ################
    ##Preparing the next trials
    if not dummyMode:  #if not (dummyMode or practice):
        present_message("calibration")
        waitForKey(variables.ser)
        tk.doTrackerSetup() #Calibrating the eyetracker
    core.wait(0.5)
    # io.clearEvents(device_label='all')  #Flushing the buffer. In the final experiment to be replaced by the following line
    variables.ser.reset_input_buffer()

    ##Creating a randomized List of questions for one block
    card_number = (card_input['card_selected'])
    questionlist = Cards[int(card_number)]["questions_asked"]  # Getting the List of questions according to the card selected as defined in the dictionary
    random.shuffle(questionlist)  # Randomizing the list
    print(card_input['card_selected'])  #For testing only

    ## Setting number of initial trial to 1
    trial_number = 1

    present_message("start_ready")  # "Einrichtung abgeschlossen. Zum STARTEN: RECHTS"
    waitForKey(variables.ser)
    variables.ser.reset_input_buffer()
    wordlist = []  # flushing wordlist used later for intentionality check
    blockData = []  # For storing data of ALL trials within the block

    ##Setting up a trial-counter and a loop for a block of 10 trials
    while trial_number <= trial_max:
        '''thr1 = Thread(target=readSer)
        thr1.daemon = True
        thr1.start()'''

        ##Defining the word used in the respective trial from the randomized wordlist
        word_number = questionlist[int(trial_number - 1)]  # Choosing the 1st, 2nd 3rd... word from the (randomized) list. This variable could also be just the variable "word" used below but I defined an extra variable for more clarity.
        word = Questions[int(word_number)]["text"]  # The translation of the words number into actual text (according to the "Questions" dictionary)
        wordlist.append(word)
        # print(word) #for testing only
        core.wait(0.5)

        tk.setOfflineMode()
        pylink.pumpDelay(50)
        err = tk.startRecording(1,1,1,1)
        pylink.pumpDelay(50)
        eyeTracked = tk.eyeAvailable()
        if eyeTracked==2:
            eyeTracked = 1

        ##Writing information on the trial into a data dictionary
        trialData = {
            "Subject_No": expInfo['Subject'],
            "BlockNumber": block_number,
            "TrialNumber": trial_number,
            "ITIoffset": round(variables.ITI500, 4),
            "CardNumber": card_number,
            **variables.Mapping  # Adds informations concerning the mapping of the keys for yes/no and the colors of the effects (circles)
        }
        trialData.update(trial(word, variables.Mapping["DelayEffectLeft"], variables.Mapping["DelayEffectRight"]))  # Calling trial function and appending data from this trial to data dictionary.
        trialData.update({"ResponseCorrect": checkCorrectness(word_number, card_number, trialData, variables.Mapping)})  # Checking whether response was correct and appending this information (boolean) to data
        trialData.update({"TrueResponseWouldBe": checkTrueResponse(word_number, card_number, variables.Mapping)})
        trialData.update({"DelayEffectLeft": variables.Mapping["DelayEffectLeft"], "DelayEffectRight": variables.Mapping["DelayEffectRight"]})
        tk.sendCommand('clear_screen 0')
        if not practice:
            #sendBehavData(data)  # Writing data to the behaviour-file and sending it (if not in dummy mode) to the eyetracker.
            blockData.append(trialData)
        tk.stopRecording()
        tk.sendMessage('TRIAL_RESULT')
        pylink.pumpDelay(50)

        trial_number = trial_number + 1

        variables.ser.reset_input_buffer()  # flush the input buffer
        #variables.q.queue.clear()  # flushing the queue

    ## sequence of showing the cards image and asking whether it was the correct one ##
    present_message("card_image")  # Your card was probably:
    core.wait(4)
    image_presented = show_cardimage(card_number, block_number)  # Present image of card
    core.wait(5)
    if variables.Mapping['KeyYes'] == 'r':
        present_message("card_correct_right")
    else:
        present_message("card_correct_left")
    decision = waitForDecision(variables.ser)

    '''
    ## sequence asking whether there were any unintentional reactions and if so which ##
    if variables.Mapping['KeyYes'] == 'r':
        present_message("unintentional_response_right")
    else:
        present_message("unintentional_response_left")
    core.wait(0.7)
    anyUnintentional = checkMeaning(waitForDecision(variables.ser))
    if anyUnintentional == True:
        #whichUnintentional = "TEST123" # for testing ONLY. Must not be activre oin final experiment
        whichUnintentional = formUnintentional(wordlist)  # Present form asking for which responses were unintentional
    else:
        whichUnintentional = "None"
    '''

    whichUnintentional = formUnintentional(wordlist)  # Present form asking for which responses were unintentional

    if not practice:
        for storedTrialData in blockData:
            storedTrialData.update({
                "CardImagePresented": image_presented,
                "CardImageReportedlyCorrect": checkMeaning(decision),
                # "AnyUnintentionalReactions": anyUnintentional,
                "whichUnintentionalReactions(form)": whichUnintentional[blockData.index(storedTrialData)]
            })  # Appending information  to data on the presented card image (int) and whether participant evaluated it to be the correct card (boolean)
            sendBehavData(storedTrialData)  # Writing data to the behaviour-file and sending it (if not in dummy mode) to the eyetracker.
        #sendBehavData("ENDofBLOCK") 
        print(len(blockData))  # For Testing only
