import general.variables as variables
#from general.variables import timer, ser#, q
from general.config_hardware import WIN, tk, BUTTONMODE
from general.messages import present_message
from general import effects
from psychopy import visual, core, event
import experiment.config_experiment as config_experiment
import random


def buttonTrial(word, delayEffectLeft, delayEffectRight):
    ## setting variables to their initial values
    tooEarly = False
    inTime = False
    tooLate = False
    key = ""
    timestamp_reaction = 0  # to make sure the value from the last trial is not carried over if no reaction in this one
    timestamp_effect = 0  # to make sure the value from the last trial is not carried over if no reaction in this one
    button_pressed = False
    durationFixation = random.uniform(*config_experiment.DURATION_SPAN_FIXATION)  # Determining the random fixation period, within the predifined span

    ##Presenting the stimulus (i.e. the word)
    present_message("blackscreen")  # Blackscreen
    core.wait(config_experiment.DELAY_INITIAL)
    variables.ser.reset_input_buffer()  # Flushing the input buffer
    tk.sendMessage('Fixation_Onset')
    variables.timer.reset(newT=0.0)
    effects.cross()  # Displaying a fixation cross
    timestampFixation = variables.timer.getTime()

    while True:
        #i = i + 1  # for testing only
        keyInput = variables.ser.read()
        if keyInput == b"*": keyInput = variables.ser.read(size=2)

        if keyInput in [b'10', b'01'] and variables.timer.getTime() < (timestampFixation + durationFixation):
            tk.sendMessage('tooEarly_Onset')
            WIN.flip()
            event.clearEvents()
            present_message("early")  # "Too early"
            tooEarly = True
            if keyInput == b'10':
                key = 'l'
                core.wait(delayEffectLeft)
            if keyInput == b'01':
                key = 'r'
            core.wait(config_experiment.DURATION_MESSAGE_TOOEARLY)
            break


        if variables.timer.getTime() >= (timestampFixation + durationFixation):
            event.clearEvents()
            #print(i)  # For testing only
            break


    if not tooEarly:
        target = visual.TextStim(WIN, text=word, pos=[0, 0], alignHoriz='center')  # stimulus (i.e. the word)
        target.draw()
        variables.ser.reset_input_buffer()  # Flushing the input buffer
        core.wait(config_experiment.DELAY_TARGET)
        #q.queue.clear()  # flushing the queue
        variables.timer.reset(newT=0.0)
        print(word)  # for testing only
        timestamp_target = variables.timer.getTime()
        tk.sendMessage('%d TargetOnset' % timestamp_target)
        WIN.flip()  # display the stimulus

        screenRefreshed = False
        #i = 0  # for testing only

        while True:
            #i = i + 1  # for testing only
            keyInput = variables.ser.read()
            if keyInput == b"*": keyInput = variables.ser.read(size=2)

            if screenRefreshed == False and variables.timer.getTime() > (timestamp_target + config_experiment.DURATION_TARGET):  # q.empty():  # Value to be adjusted for final experiment
                screenRefreshed = True
                WIN.flip()
                tk.sendMessage('Target_Offset')
                event.clearEvents()
                #print(i)  # For testing only
                pass

            if keyInput in [b'10', b'01']:  # If any button is pressed
                print("button pressed")  # For testing
                button_pressed = True
                timestamp_reaction = variables.timer.getTime()
                tk.sendMessage('Reaction')
                ##If the reaction is so early that no target-specific reaction can be assumed -> "Too early"
                if keyInput == b'10':
                    key = 'l'
                    core.wait(delayEffectLeft)
                if keyInput == b'01':
                    key = 'r'
                    core.wait(delayEffectRight)
                #WIN.flip()
                timestamp_effect = variables.timer.getTime()
                tk.sendMessage('EffectOnset')
                effects.reaction(key)
                tk.sendMessage('Effect_Offset')
                inTime = True
                print(key)  # For testing
                #print(i)  # For testing only
                inTime = True
                break

            ##If there is no response within the given timeframe -> "Too late"
            if variables.timer.getTime() > (timestamp_target + config_experiment.TIME_TOOLATE): #and not button_pressed:  # q.empty():
                event.clearEvents()
                present_message("late")  # "Too late"
                tk.sendMessage('tooLate_Onset')
                tooLate = True
                core.wait(config_experiment.DURATION_MESSAGE_TOOLATE)
                tk.sendMessage('tooLate_Offset')
                #print(i)  # For testing only
                break

        ### writing the data of the trial into the data dictionary ###
        trial_data = {
            "Stimulus": word,
            "Response": key,
            "RTTime": round((timestamp_reaction - timestamp_target), 4),
            "ActionEffectOnsetTime": round(timestamp_effect, 4),
            "TooEarly": tooEarly,
            "TooLate": tooLate,
            "InTime": inTime,
            "DurationFixation": durationFixation
        }

    else:  # If tooEarly == True
        ### writing the data of the trial into the data dictionary ###
        trial_data = {
            "Stimulus": word,
            "Response": key,
            "RTTime": "none",
            "ActionEffectOnsetTime": "none",
            "TooEarly": tooEarly,
            "TooLate": tooLate,
            "InTime": inTime,
            "DurationFixation": durationFixation
        }

    return trial_data



def noButtonTrial(word, delayEffectLeft, delayEffectRight):
    ## setting variables to their initial values
    tooEarly = False
    inTime = False
    tooLate = False
    key = ""
    timestamp_reaction = 0  # to make sure the value from the last trial is not carried over if no reaction in this one
    timestamp_effect = 0  # to make sure the value from the last trial is not carried over if no reaction in this one
    button_pressed = False
    durationFixation = random.uniform(*config_experiment.DURATION_SPAN_FIXATION)  # Determining the random fixation period, within the predifined span


    ##Presenting the fixation cross
    present_message("blackscreen")  # Blackscreen
    core.wait(config_experiment.DELAY_INITIAL)
    variables.io.clearEvents(device_label='all')  #Flushing the buffer.
    tk.sendMessage('Fixation_Onset')
    effects.cross()  # Displaying a fixation cross
    variables.timer.reset(newT=0.0)
    timestampFixation = variables.timer.getTime()


    keyInput = []
    while True:
        #i = i + 1  # for testing only
        keyboardActivity = variables.io.devices.keyboard.getKeys()
        if keyboardActivity != []:
            keyInput = keyboardActivity[0].key

        if keyInput in ['s', 'l'] and variables.timer.getTime() < (timestampFixation + durationFixation):
            tk.sendMessage('tooEarly_Onset')
            WIN.flip()
            event.clearEvents()
            present_message("early")  # "Too early"
            tooEarly = True
            core.wait(config_experiment.DURATION_MESSAGE_TOOEARLY)
            tk.sendMessage('tooEarly_Offset')
            #print(i)  # For testing only
            break

        if variables.timer.getTime() > (timestampFixation + durationFixation):  # q.empty():
            event.clearEvents()
            #print(i)  # For testing only
            tk.sendMessage('Fixation_Offset')
            break


    if not tooEarly:
        target = visual.TextStim(WIN, text=word, pos=[0, 0], alignHoriz='center')  # stimulus (i.e. the word)
        target.draw()
        variables.io.clearEvents(device_label='all')  # Flushing the buffer.
        core.wait(config_experiment.DELAY_TARGET)
        #q.queue.clear()  # flushing the queue
        variables.timer.reset(newT=0.0)
        print(word)  # for testing only
        timestamp_target = variables.timer.getTime()
        tk.sendMessage('%d TargetOnset' % timestamp_target)
        WIN.flip()  # display the stimulus
        screenRefreshed = False
        #i = 0  # for testing only

        keyInput = []
        while True:
            #i = i + 1  # for testing only
            keyboardActivity = variables.io.devices.keyboard.getKeys()
            if keyboardActivity != []:
                keyInput = keyboardActivity[0].key

            if screenRefreshed == False and variables.timer.getTime() > (timestamp_target + config_experiment.DURATION_TARGET):  # q.empty():  # Value to be adjusted for final experiment
                screenRefreshed = True
                WIN.flip()
                tk.sendMessage('Target_Offset')
                event.clearEvents()
                #print(i)  # For testing only
                pass

            if keyInput in ['s', 'l']:  # If any button is pressed
                print("button pressed")  # For testing
                button_pressed = True
                timestamp_reaction = variables.timer.getTime()
                tk.sendMessage('Reaction')
                ##If the reaction is so early that no target-specific reaction can be assumed -> "Too early"
                if keyInput == 's':
                    key = 'l'
                    core.wait(delayEffectLeft)
                if keyInput == 'l':
                    key = 'r'
                    core.wait(delayEffectRight)
                #WIN.flip()
                timestamp_effect = variables.timer.getTime()
                tk.sendMessage('Effect_Onset')
                effects.reaction(key)
                tk.sendMessage('Effect_Offset')
                inTime = True

                print(key)  # For testing
                #print(i)  # For testing only
                inTime = True
                break

            ##If there is no response within the given timeframe -> "Too late"
            if variables.timer.getTime() > (timestamp_target + config_experiment.TIME_TOOLATE): #and not button_pressed:  # q.empty():
                event.clearEvents()
                present_message("late")  # "Too late"
                tk.sendMessage('tooLate_Onset')
                tooLate = True
                core.wait(config_experiment.DURATION_MESSAGE_TOOLATE)
                tk.sendMessage('tooLate_Offset')
                #print(i)  # For testing only
                break


        ### writing the data of the trial into the data dictionary ###
        trial_data = {
            "Stimulus": word,
            "Response": key,
            "RTTime": round((timestamp_reaction - timestamp_target), 4),
            "ActionEffectOnsetTime": round(timestamp_effect, 4),
            "TooEarly": tooEarly,
            "TooLate": tooLate,
            "InTime": inTime,
            "DurationFixation": durationFixation
        }

    else:  # If tooEarly == True
        ### writing the data of the trial into the data dictionary ###
        trial_data = {
            "Stimulus": word,
            "Response": key,
            "RTTime": "none",
            "ActionEffectOnsetTime": "none",
            "TooEarly": tooEarly,
            "TooLate": tooLate,
            "InTime": inTime,
            "DurationFixation": durationFixation
        }

    return trial_data



def trial(word, delayEffectLeft, delayEffectRight):
    if BUTTONMODE == True:
        trialData = buttonTrial(word, delayEffectLeft, delayEffectRight)
    else:
        trialData = noButtonTrial(word, delayEffectLeft, delayEffectRight)

    return trialData
