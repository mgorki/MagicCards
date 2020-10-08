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
    core.wait(0.8)
    target = visual.TextStim(WIN, text=word, pos=[0, 0], alignHoriz='center')
    target.draw()
    variables.ser.reset_input_buffer()  # flushing the input buffer
    core.wait(0.2)
    #q.queue.clear()  # flushing the queue
    variables.timer.reset(newT=0.0)
    print(word)  # for testing only
    timestamp_target = variables.timer.getTime()
    tk.sendMessage('%d TargetOnset' % timestamp_target)
    WIN.flip()  # display the stimulus

    i = 0

    while True:
        key_input = variables.ser.read()
        i = i+1  # For testing
        if key_input == b"*":
            key_input = variables.ser.read(size=2)
            print(key_input)  # For testing
            print(i)  # For testing
            if (key_input == b'10') or (key_input == b'01'):  # If any button is pressed
                button_pressed = True
                timestamp_reaction = variables.timer.getTime()
                tk.sendMessage('%d ResponseFrameOnset')
                print("button pressed")  # For testing
                ##If the reaction is so early that no target-specific reaction can be assumed -> "Too early"
                if variables.timer.getTime() < timestamp_target + 0.07:  # Value to be adjusted for final experiment
                    WIN.flip()
                    event.clearEvents()
                    present_message("early")  # "Too early"
                    tooEarly = True
                    core.wait(1)
                    break

                else:
                    # key = q.get()
                    if key_input == b'10':
                        key = 'l'
                    else:
                        key = 'r'
                    WIN.flip()
                    effects.reaction(key)
                    inTime = True
                    timestamp_effect = variables.timer.getTime()
                    print(key)  # For testing
                    inTime = True
                    break

            else:
                print("no button pressed")  # For testing
                ##Presents a blackscreen after 0.5 seconds
                if (variables.timer.getTime() > (timestamp_target + 0.5)) and not button_pressed:  # q.empty():  # Value to be adjusted for final experiment
                    WIN.flip()
                    event.clearEvents()
                    present_message("blackscreen")  # Blackscreen
                    pass

                    ##If there is no response within the given timeframe -> "Too late"
                elif (variables.timer.getTime() > (timestamp_target + 2)): #and not button_pressed:  # q.empty():
                    event.clearEvents()
                    present_message("late")  # "Too late"
                    tooLate = True
                    core.wait(1)
                    break
                else:
                    pass



        '''key_input = ser.readline().decode().strip('\r\n')
        if (len(key_input) > 0) and not ((key_input == "00") or (key_input == '0')):
            button_pressed = True
            print(key_input)  # For testing
        #if not q.empty():
            timestamp_reaction = timer.getTime()
            tk.sendMessage('%d ResponseFrameOnset')

            ##If the reaction is so early that no target-specific reaction can be assumed -> "Too early"
            if timer.getTime() < timestamp_target + 0.07:  # Value to be adjusted for final experiment
                WIN.flip()
                event.clearEvents()
                present_message("early")  # "Too early"
                tooEarly = True
                core.wait(1)
                break

            else:
                #key = q.get()
                key = key_input
                WIN.flip()
                effects.reaction(key)
                inTime = True
                timestamp_effect = timer.getTime()
                print(key)  # For testing
                inTime = True
                break

        ##Presents a blackscreen after 0.5 seconds
        elif ((timestamp_target + 2) >= timer.getTime() > (timestamp_target + 0.5)) and not button_pressed: #q.empty():  # Value to be adjusted for final experiment
            WIN.flip()
            event.clearEvents()
            present_message("blackscreen")  # Blackscreen


        ##If there is no response within the given timeframe -> "Too late"
        elif (timer.getTime() > (timestamp_target + 2)) and not button_pressed: #q.empty():
            event.clearEvents()
            present_message("late")  # "Too late"
            tooLate = True
            core.wait(1)
            break'''

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
