from psychopy import core, event
from general.init import initLog, initTk, waitForKey, receiveData, initMapping, initSer
from general.config_hardware import WIN, tk, dummyMode
from general.messages import present_message
from experiment.blocks import block
from experiment.config_experiment import behaviour, block_max
import general.variables as variables
from general.board import chooseCard
#import ast


def main():
    ###################Experiment starting sequence###########################
    tk.sendMessage('%d ITIoffset' % 0)

    ## Initializing serial connection to Arduino ##
    initSer() ## stored in variables.ser
    print(variables.ser)  # For testing

    ## Basic info dialog, defining participants number, dominant eye & hand, basic demografics ##
    expInfo = variables.infoBuffer
    print(expInfo, file=behaviour)

    ## Initializing Eyetracker ##
    dataFileName = initTk(expInfo)  # inits the eyetracker and returns the name of the eyetracker-data file

    ## Initializing randomization of response keys and effect colors ##
    initMapping()  # Randomized assignment of effect colors and key for yes/no (stored in variables.RandomMapping)
    print(variables.Mapping)  # For testing
    print("variable mapping defined")  # For testing

    ################################# Experiment ###########################################

    if not dummyMode:
        print("tracker setup started")
        tk.doTrackerSetup()
    print("tracker setup done")  # for testing

    #######Wellcoming message#######
    present_message("welcome")
    core.wait(0.5)
    waitForKey(variables.ser)
    #variables.ser.reset_input_buffer()

    present_message("welcome_2")
    core.wait(0.5)
    waitForKey(variables.ser)
    #variables.ser.reset_input_buffer()

    present_message("welcome_3")
    core.wait(0.5)
    waitForKey(variables.ser)
    #variables.ser.reset_input_buffer()

    present_message("welcome_4")
    core.wait(0.5)
    waitForKey(variables.ser)
    #variables.ser.reset_input_buffer()

    ######

    ##Explanations of what to do
    present_message("explanation_initial_general")
    core.wait(0.5)
    waitForKey(variables.ser)
    #variables.ser.reset_input_buffer()

    if variables.Mapping["KeyYes"] == 'r':
        present_message("explanation_initial_yes_right")
    else:
        present_message("explanation_initial_yes_left")
    core.wait(0.5)
    waitForKey(variables.ser)
    #variables.ser.reset_input_buffer()

    ##important
    present_message("explanation_initial_important")
    core.wait(0.5)
    waitForKey(variables.ser)
    #variables.ser.reset_input_buffer()

    ##Explanations of what to do
    present_message("explanation_initial_procedure")
    core.wait(0.5)
    waitForKey(variables.ser)
    #variables.ser.reset_input_buffer()

    ##Explanations of what to do
    present_message("explanation_initial_procedure_2")
    core.wait(0.5)
    waitForKey(variables.ser)
    #variables.ser.reset_input_buffer()

    ######

    ###### Practice #####
    ##First some questions for practice
    present_message("practice")
    waitForKey(variables.ser)
    variables.ser.reset_input_buffer()


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
        core.wait(0.5)
        waitForKey(variables.ser)
        variables.ser.reset_input_buffer()

        ## Presenting a message about some initialization
        present_message("initialization")
        chooseCard()  # At this point the researcher gives input on the chosen card via the Arduino's numpad

        block(expInfo, practice, block_number)  # Runs a block of 10 trials

        if practice:
            present_message("practice_finished")
            core.wait(0.5)
            waitForKey(variables.ser)
            #variables.ser.reset_input_buffer()

        block_number += 1  # raises the block_number after each block by one

    ## Receiving data from the eyetracker (if not in dummy mode) ##
    if not dummyMode:
        receiveData(dataFileName)
    else:
        print("No eyetracker data received because you are running the experiment in dummy mode")

    ################  Thank you message and end sequence  ################
    present_message("thanks")
    core.wait(0.5)
    waitForKey(variables.ser)
    event.clearEvents()
    print("experiment completed", file=behaviour)
    #############################################################################

    # make sure everything is closed down
    behaviour.close()
    tk.close()
    variables.ser.close()
    WIN.close()
    core.quit()


if __name__ == '__main__':
    main()
