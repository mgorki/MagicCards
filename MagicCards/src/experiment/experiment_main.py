from psychopy import core, event
from general.init import initLog, initTk, waitForKey, receiveData, initRandomMapping
from general.config_hardware import WIN, tk, dummyMode
from general.messages import present_message
from experiment.blocks import block
from experiment.config_experiment import behaviour, block_max
from general.variables import ser
from general.arduino import chooseCard


def main():
    ###################Experiment starting sequence###########################
    tk.sendMessage('%d ITIoffset' % 0)

    ## 2 Basic info dialog, defining participants number, dominant eye & hand, basic demografics ##
    expInfo = initLog()  # participant info

    ## Initializing Eyetracker ##
    dataFileName = initTk(expInfo)  # inits the eyetracker and returns the name of the eyetracker-data file

    ## Initializing randomization of response keys ##
    KeyMapping = initRandomMapping()  # Creating a dictionary which defines the keys for yes and no (randomized)

    ################################# Experiment ###########################################

    #######Wellcoming message#######
    ## Pick a card from the stack
    present_message("welcome")
    waitForKey(ser)
    ser.reset_input_buffer()

    ######

    ##Explanations of what to do
    if KeyMapping["KeyYes"] == 'r':
        present_message("explanation_initial_yes_right")
    else:
        present_message("explanation_initial_yes_left")
    waitForKey(ser)
    ser.reset_input_buffer()
    ######

    ###### Practice #####
    ##First some questions for practice
    present_message("practice")
    waitForKey(ser)
    ser.reset_input_buffer()


    ################ Block Structure ################
    ## Setting up a block-counter and a loop of 10 blocks ##
    block_number = 1
    while block_number <= block_max:  # Set block_max in the config_experiment file in order to run more or less blocks
        if block_number == 0:
            practice = True
        else:
            practice = False

        ## Choosing a (new) card and running a block ##
        if practice:
            present_message("practice_ready")  # "Please advice the researcher when you are ready"
        else:
            present_message("choose_ready")  # "Choose a new card and advice the researcher when you are ready"
        chooseCard()  # Opens a dialog for entering a cards variable name. In the final experiment this of course should be done from another device without the dialog being shown to the participant.
        block(practice, block_number, KeyMapping)  # Runs a block of 10 trials

        if practice:
            if KeyMapping["KeyYes"] == 'r':
                present_message("explanation_remember_yes_right")
            else:
                present_message("explanation_remember_yes_left")

            waitForKey(ser)
            ser.reset_input_buffer()

        block_number = block_number + 1  # raises the block_number after each block by one

    ## Receiving data from the eyetracker (if not in dummy mode) ##
    if not dummyMode:
        receiveData(dataFileName)
    else:
        print("No eyetracker data received because you are running the experiment in dummy mode")

    ################  Thank you message and end sequence  ################
    present_message("thanks")
    waitForKey(ser)
    event.clearEvents()
    print("experiment completed", file=behaviour)
    #############################################################################

    # make sure everything is closed down
    behaviour.close()
    tk.close()
    ser.close()
    WIN.close()
    core.quit()


if __name__ == '__main__':
    main()

