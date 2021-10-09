import os

behaviour = open((os.getcwd() + "\\data_recorded\\behaviouralData\\magic_cards_behaviour.csv"), "a")  # defining the file to which behavioral data is saved
edfDataFolder = (os.getcwd() + "\\data_recorded\\edfData")
MAPPING_BY_DIALOG = True  # If true the assignment of the key for yes/no and the colors of the effects (circles) are defined in the biginning via dialog box. If false: random assignment in the beginning.
block_max = 22 #10  # Number of blocks to be performed (including one practice block at the beginning) LOW NUMBER ONLY FOR DEBUGING! ADJUST IT IN THE FINAL EXPERIMENT!!!
trial_max = 10  # Number of TRIALS to be performed per block
NUMOFCARDS = 26  # Total number of cards from which the participant(s) can choose
NUMOFIMAGES = 34  # Total number of images, including cards from which the participant(s) cannot choose
PERCENTAGECORRECTCARD = [0, 0, 0, 0, 0, 20, 20, 20, 20, 20, 20, 50, 50, 50, 50, 50, 50, 50, 50, 50, 80, 80] # The chance (in percent) that the image of the correct card is presented by the computer at the end of a given block. This list must have as many elements as there are blocks.
#TIME_TOOEARLY = 0.05  # Before this time (seconds) from target onset response is marked as too early. To avoid participants just blindly pressing any button as soon, as the fixation cross disappears.
TIME_TOOLATE = 2.0  # After this time (seconds) from target onset response is too late
DURATION_SPAN_FIXATION = (2.0, 2.5)  # Duration range (seconds) of fixation cross. Within this range the duration is random
DURATION_TARGET = 0.2  # Duration (seconds) of target (word) presentation
DURATION_EFFECT = 0.5  # Duration (seconds) of effect (circle) presentation
DURATION_MESSAGE_TOOEARLY = 1  # Duration (seconds) of presentation of the too early message
DURATION_MESSAGE_TOOLATE = 1  # Duration (seconds) of presentation of the too late message
DELAY_INITIAL = 0.0  # Initial delay / ITI (blackscreen) before fixation cross appears (in seconds)
DELAY_TARGET = 0.0  # Delay (blackscreen) between fixation cross offset and target (word) onset (in seconds)
DELAY_EFFECT_LONG = 0.8  # Delay between reaction and effect (circle) onset (in seconds) for key1
DELAY_EFFECT_SHORT = 0.2  # Delay between reaction and effect (circle) onset (in seconds) for key2
