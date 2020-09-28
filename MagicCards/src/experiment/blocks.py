import random
from psychopy import core
from threading import Thread
from experiment.cards_and_questions import Cards, Questions
from general.init import waitForKey
from general.config_hardware import tk, dummyMode
from general.messages import present_message
from experiment.trials import trial
from general.variables import ser, ITI500#, q
from experiment.config_experiment import behaviour, trial_max
from general.arduino import card_input, readSer


def checkCorrectness(word_number, card_number, data, KeyMapping):  # Function returns whether response is correct or not (boolean)
    if (int(word_number) in (Cards[int(card_number)]["questions_yes"])):  # true if answer should be yes
        response_should = KeyMapping["KeyYes"]
    else:
        response_should = KeyMapping["KeyNo"]

    if data["Response"] == response_should:  # True if the actual response matches the correct response
        return True
    else:
        return False


def sendBehavData(data):
    print(data, file=behaviour)  # prints data to the console and appends it to magic_cards_behaviour.txt
    if not dummyMode:
        tk.sendMessage('TRIALID')
        tk.sendCommand("record_status_message 'Block: %s Trial number: %s'" % (data["BlockNumber"], data["TrialNumber"]))
        tk.sendMessage('!V TRIAL_VAR CardNumber %s' % data["Card_number"])
        tk.sendMessage('!V TRIAL_VAR TooEarly %s' % data["TooEarly"])
        tk.sendMessage('!V TRIAL_VAR TooSlow %s' % data["TooLate"])
        tk.sendMessage('!V TRIAL_VAR InTime %s' % data["InTime"])
        tk.sendMessage('!V TRIAL_VAR Response %s' % data["Response"])
        tk.sendMessage('!V TRIAL_VAR Stimulus %s' % data["Stimulus"])
        tk.sendMessage('!V TRIAL_VAR RT %s' % data["RTTime"])
        tk.sendMessage('!V TRIAL_VAR Correct %s' % data["ResponseCorrect"])
    else:
        pass

def block(practice, block_number, KeyMapping):
    ################ Block structure (after choosing a card) ################
    ##Preparing the next trials
    if not (dummyMode or practice):
        present_message("calibration")
        waitForKey(ser)
        tk.doTrackerSetup() #Calibrating the eyetracker
    core.wait(0.5)
    # io.clearEvents(device_label='all')  #Flushing the buffer. In the final experiment to be replaced by the following line
    ser.reset_input_buffer()

    ##Creating a randomized List of questions for one block
    card_number = (card_input['card_selected'])
    questionlist = Cards[int(card_number)]["questions_asked"]  # Getting the List of questions according to the card selected as defined in the dictionary
    random.shuffle(questionlist)  # Randomizing the list

    ## Setting number of initial trial to 1
    trial_number = 1

    ##Setting up a trial-counter and a loop for a block of 10 trials
    while trial_number <= trial_max:
        # thr1 = Thread(target=readSer)
        # thr1.daemon = True
        # thr1.start()

        ##Defining the word used in the respective trial from the randomized wordlist
        word_number = questionlist[int(trial_number - 1)]  # Choosing the 1st, 2nd 3rd... word from the (randomized) list. This variable could also be just the variable "word" used below but I defined an extra variable for more clarity.
        word = Questions[int(word_number)]["text"]  # The translation of the words number into actual text (according to the "Questions" dictionary)
        # print(word) #for testing only
        core.wait(0.5)

        ##Writing information on the trial into a data dictionary
        data = {
            "BlockNumber": block_number,
            "TrialNumber": trial_number,
            "ITIoffset": ITI500,
            "CardNumber": card_number,
            "KeyMapping": KeyMapping,
        }
        data.update(trial(word))  # Calling trial function and appending data from this trial to data dictionary.
        data.update({"ResponseCorrect": checkCorrectness(word_number, card_number, data, KeyMapping)})  # Checking whether response was correct and appending this information (boolean) to data

        sendBehavData(data)  # Writing data to the behaviour-file and sending it (if not in dummy mode) to the eyetracker.

        trial_number = trial_number + 1

        ser.reset_input_buffer()  # flush the input buffer
#        q.queue.clear()  # flushing the queue
