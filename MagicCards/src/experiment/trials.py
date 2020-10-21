import general.variables as variables
#from general.variables import timer, ser#, q
from general.config_hardware import WIN, tk
from general.messages import present_message
from general import effects
from psychopy import visual, core, event


def trial(word):

    ## setting variables to their initial values
    tooEarly = False
    inTime = False
    tooLate = False
    key = ""
    timestamp_reaction = 0  # to make sure the value from the last trial is not carried over if no reaction in this one
    timestamp_effect = 0  # to make sure the value from the last trial is not carried over if no reaction in this one
    button_pressed = False

    ##Presenting the stimulus (i.e. the word)
    present_message("blackscreen")  # Blackscreen
    core.wait(0.5)
    tk.sendMessage('FixationCrossOnset')
    effects.cross()  # Displaying a fixation cross
    tk.sendMessage('FixationCrossEnd')


    target = visual.TextStim(WIN, text=word, pos=[0, 0], alignHoriz='center')  # stimulus (i.e. the word)
    target.draw()
    variables.ser.reset_input_buffer()  # flushing the input buffer
    core.wait(0.2)
    #q.queue.clear()  # flushing the queue
    variables.timer.reset(newT=0.0)
    print(word)  # for testing only
    timestamp_target = variables.timer.getTime()
    tk.sendMessage('%d TargetOnset' % timestamp_target)
    WIN.flip()  # display the stimulus

    screenRefreshed = False

    i = 0  # for testing only

    while True:
        i = i + 1  # for testing only
        key_input = variables.ser.read()
        if key_input == b"*": key_input = variables.ser.read(size=2)

        if key_input in [b'10', b'01'] and variables.timer.getTime() < timestamp_target + 0.07:  # Value to be adjusted for final experiment
            tk.sendMessage('tooEarlyOnset')
            WIN.flip()
            event.clearEvents()
            present_message("early")  # "Too early"
            tooEarly = True
            core.wait(1)
            tk.sendMessage('tooEarlyEnd')
            print(i)  # For testing only
            break


        if screenRefreshed == False and variables.timer.getTime() > (timestamp_target + 0.5):  # q.empty():  # Value to be adjusted for final experiment
            screenRefreshed = True
            WIN.flip()
            tk.sendMessage('Blackscreen')
            event.clearEvents()
            print(i)  # For testing only
            pass


        if key_input in [b'10', b'01']:  # If any button is pressed
            print("button pressed")  # For testing
            button_pressed = True
            timestamp_reaction = variables.timer.getTime()
            tk.sendMessage('Reaction')
            ##If the reaction is so early that no target-specific reaction can be assumed -> "Too early"
            if key_input == b'10': key = 'l'
            if key_input == b'01': key = 'r'
            #WIN.flip()
            core.wait(0.3)
            timestamp_effect = variables.timer.getTime()
            tk.sendMessage('EffectOnset')
            effects.reaction(key)
            tk.sendMessage('EffectEnd')
            inTime = True

            print(key)  # For testing
            print(i)  # For testing only
            inTime = True
            break


        ##If there is no response within the given timeframe -> "Too late"
        if variables.timer.getTime() > (timestamp_target + 2): #and not button_pressed:  # q.empty():
            event.clearEvents()
            present_message("late")  # "Too late"
            tk.sendMessage('tooLateOnset')
            tooLate = True
            core.wait(1)
            tk.sendMessage('tooLateEnd')
            print(i)  # For testing only
            break



    ### writing the data of the trial into the data dictionary ###
    trial_data = {
        "Stimulus": word,
        "Response": key,
        "RTTime": timestamp_reaction - timestamp_target,
        "ActionEffectOnsetTime": timestamp_effect,
        "TooEarly": tooEarly,
        "TooLate": tooLate,
        "InTime": inTime
    }

    return trial_data
