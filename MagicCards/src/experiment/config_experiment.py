import os

behaviour = open((os.getcwd() + "\\data_recorded\\behaviouralData\\magic_cards_behaviour.csv"), "a")  # defining the file to which behavioral data is saved
edfDataFolder = (os.getcwd() + "\\data_recorded\\edfData")
block_max = 5  # Number of blocks to be performed (if not aborted) ADJUST IT IN THE FINAL EXPERIMENT!!!
trial_max = 10  # Number of blocks to be performed per block
