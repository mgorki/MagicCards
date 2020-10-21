from psychopy import core, event, gui
from general.config_hardware import WIN
import general.variables as variables #import ser#, q


##Selected Card of a certain block (Dictionary)
    # For storing the information on the card selected for the current block. "input" is a placeholder for the data placed here by chooseCard()

card_input = {"card_selected": 0} #For storing the information on the card selected for the current block. "input" is a placeholder for the data placed here by chooseCard()
##############################################

'''def readSer():
    while True:
        key_input = variables.ser.read()
        if key_input == b"*":
            key_input = variables.ser.read(size=2)
            if key_input != b"00":  # If any button is pressed
                print(str(key_input) + " pressed")  # For testing
                variables.q.put(key_input)
                break
'''
'''       key_input = ser.readline().decode().strip('\r\n')
        if (len(key_input) > 0) and not ((key_input == "00") or (key_input == 0)):
            print(key_input + " pressed")     # For testing
            q.put(key_input)
            break'''


def chooseCard():  ##Opens a dialog for entering a cards number (== variablename without the "c" at the beginning).
    ser = variables.ser
    ser.reset_input_buffer()
    core.wait(0.5)
    ser.reset_input_buffer()

    print(ser)  # for testing
    ## Code for using the keypad (Arduino) ##
    while True:
        pad = ser.read()
        if pad == b"*":
            pad = ser.read(size=2)
            print("waiting")
            print(pad)
        if pad == b'#':
            print(pad)  # for testing
            pad = ser.readline().decode().rstrip()
            print(pad)  # for testing
            pad = int(pad)
            if pad in range(1, 22):  # If input is an existing card number
                print(pad)  # for testing
                card_input["card_selected"] = pad
                # pad_data.append(pad_int) # add to the end of data list
                ser.reset_input_buffer()
                break
            elif pad == 99:
            ###Showing a window to confirm aborting the experiment. This is intended as a measure against aborting the whole experiment by accident.
                cardDlg = gui.Dlg(title="Abort/Continue")
                cardDlg.addText('You are about to abort the experiment! Press OK to abort or Cancel to continue')
                ok_data = cardDlg.show()  # show dialog and wait for OK or Cancel
                if cardDlg.OK:
                    print('user cancelled')
                    ser.reset_input_buffer()
                    exit()
                    break
                else:
                    chooseCard()
            else:
                pass
        else:
            pass


    WIN.flip()
    event.clearEvents()
    core.wait(1)
