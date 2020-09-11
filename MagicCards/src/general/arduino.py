from psychopy import core, event, gui
from general.config_hardware import WIN
from general.variables import ser, q


##Selected Card of a certain block (Dictionary)
    # For storing the information on the card selected for the current block. "input" is a placeholder for the data placed here by chooseCard()

card_input = {"card_selected": "input"} #For storing the information on the card selected for the current block. "input" is a placeholder for the data placed here by chooseCard()
##############################################

def readSer():
    while True:
        key_input = ser.readline().decode().strip('\r\n')
        if (len(key_input) > 0) and not (key_input == 0):
            print(key_input + " pressed")     # For testing
            q.put(key_input)
            break


def chooseCard():  ##Opens a dialog for entering a cards number (== variablename without the "c" at the beginning).
    ser.reset_input_buffer()
    core.wait(0.5)
    ser.reset_input_buffer()

    ## Code for using the keypad (Arduino) ##
    pad = ser.readline().decode().rstrip().strip('#')  # read a byte string, decode this byte string into Unicode and remove \n and \r and #
    if pad != "":
        print(pad) #for testing
        if pad != "99" and pad != 'r' and pad != 'l':  # r and l are explicitly excluded here in order to avoid data-type-errors caused by unintentional button presses (of left or right button)
            card_input["card_selected"] = pad.lstrip('0') # strip the input of any leading zeros
            # pad_data.append(pad_int) # add to the end of data list
        elif pad == "99":
        ###Showing a window to confirm aborting the experiment. This is intended as a measure against aborting the whole experiment by accident.
            cardDlg = gui.Dlg(title="Abort/Continue")
            cardDlg.addText('You are about to abort the experiment! Press OK to abort or Cancel to continue')
            ok_data = cardDlg.show()  # show dialog and wait for OK or Cancel
            if cardDlg.OK:
                print('user cancelled')
                exit()
            else:
                chooseCard()
        else:
            chooseCard()

    WIN.flip()
    event.clearEvents()
    core.wait(1)

