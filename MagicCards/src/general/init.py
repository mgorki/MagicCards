from psychopy import gui, core
import serial, serial.tools.list_ports
import time
from general.config_hardware import WIN, tk, scnWIDTH, scnHEIGHT, BAUDRATE, ARD_VID_PID, ARD_NAME
import os
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
import pylink
from experiment.config_experiment import behaviour, edfDataFolder
import random
import general.variables as variables


def initLog():
    myDlg = gui.Dlg(title="Magic Cards (TEST)")
    myDlg.addText('Subject info')
    myDlg.addField('Subject number:', str(159))
    myDlg.addField('Sex:', choices=["Female", "Male", "Other"])
    myDlg.addField('Age:', 20)
    myDlg.addField('Dominant eye:', choices=["right", "left"])
    myDlg.addField('Dominant hand:', choices=["right", "left"])
    myDlg.addText('Experiment Info')

    ok_data = myDlg.show()  # show dialog and wait for OK or Cancel
    if myDlg.OK:  # or if ok_data is not None
        print(dict(zip(['Subject', 'Sex', 'Age', 'Dominant_eye', 'Dominant_hand'], ok_data)), file=behaviour)
        return dict(zip(['Subject', 'Sex', 'Age', 'Dominant_eye', 'Dominant_hand'], ok_data))
    else:
        print('user cancelled')
        exit()


def initSer():  # set up the serial line for numberpad input and for the buttons I used via the same Arduino
    ports = list(serial.tools.list_ports.comports(include_links=False))
    arduinos = []
    for port in ports:
        if (str(ARD_VID_PID) in port.description) or (str(ARD_NAME) in port.description):
            arduinos.append(port.device)
            print("Arduino found at: " + str(port.device))
        else:
            pass

    if len(arduinos) == 0:
        print("No Arduino found! Is it connected to a valid port? Crashing now")
    elif len(arduinos) == 1:
        try:
            ser = serial.Serial(arduinos[0], BAUDRATE)  # init the buttons
            variables.ser = ser
            print("connected to Arduino at: %s with baudrate %s" % (arduinos[0], BAUDRATE))
        except:
            print("There was an error while connecting to the Arduino. Is everything coinnected and configured properly?")
    else:
        print("More than one Arduino connected! Make sure only one such device is connected and retry. Crashing now.")

    time.sleep(1)

#    variables.ser = serial.Serial("COM5", 38400)  # for testing only


def waitForKey(ser):
    core.wait(0.2)
    ser.reset_input_buffer()  # reset buttons

    while True:
        a = ser.read()
        print(a)  # for testing
        if a == b"*":
            a = ser.read(size=2)
            print("button state")  # for testing
            print(a)
            if a != b'01':
                pass
            else:
                ser.reset_input_buffer()  # reset buttons
                break


def waitForDecision(ser):
    core.wait(.1)
    ser.reset_input_buffer()  # reset buttons

    while True:
        a = ser.read()
        print(a)  # for testing
        if a == b"*":
            a = ser.read(size=2)
            print("button state")  # for testing
            print(a)
            if (a != b'01') and (a != b'10'):
                pass
            else:
                ser.reset_input_buffer()  # reset buttons
                if a == b'01':
                    a = 'r'
                else:
                    a = 'l'
                return a


def initTk(expInfo):
    ## Data host ##
    if not os.path.exists(edfDataFolder):
        os.makedirs(edfDataFolder)
    dataFileName = (expInfo['Subject'] + '.EDF')
    tk.openDataFile(dataFileName)
    # add personalized data file header (preamble text)
    tk.sendCommand("add_file_preamble_text 'Psychopy Waaaaazzzzzzooooo'")
    tk.sendMessage('Subject_No %s' % expInfo["Subject"])

    ## Init parameters
    genv = EyeLinkCoreGraphicsPsychoPy(tk, WIN)
    pylink.openGraphicsEx(genv)

    tk.setOfflineMode()
    tk.sendCommand('sample_rate 500')
    tk.sendCommand("screen_pixel_coords = 0 0 %d %d" % (scnWIDTH - 1, scnHEIGHT - 1))
    tk.sendMessage("DISPLAY_COORDS = 0 0 %d %d" % (scnWIDTH - 1, scnHEIGHT - 1))
    #tk.sendCommand("hostVer = HV5")
    tk.sendCommand("recording_parse_type = GAZE")

    eyelinkVer = tk.getTrackerVersion()
    if eyelinkVer >= 2:
        tk.sendCommand('select_parser_configuration 0')

    hostVer = 0
    if eyelinkVer == 3:
        tvstr = tk.getTrackerVersionString()
        vindex = tvstr.find("EYELINK CL")
        hostVer = int(float(tvstr[(vindex + len("EYELINK CL")):].strip()))

    tk.sendCommand("file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT")
    tk.sendCommand("link_event_filter = LEFT,RIGHT,FIXATION,FIXUPDATE,SACCADE,BLINK,BUTTON,INPUT")

    if hostVer >= 4:
        tk.sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,HTARGET,INPUT")
        tk.sendCommand("link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,HTARGET,INPUT")
    else:
        tk.sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,INPUT")
        tk.sendCommand("link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,INPUT")

    return dataFileName

def receiveData(dataFileName):
    if not os.path.exists('edfData'):
        os.mkdir('edfData')
    tk.receiveDataFile(dataFileName, 'edfData' + os.sep + dataFileName)
    print("Data saved to: " + edfDataFolder, os.sep + dataFileName)  # For testing


def initRandomMapping():
    ## Randomized assignment of left/right key to answer yes/no ##
    randmap = random.getrandbits(1)
    if int(randmap) == 0:
        KeyMapping = {
            "KeyYes": 'r',
            "KeyNo": 'l'
        }
    else:
        KeyMapping = {
            "KeyYes": 'l',
            "KeyNo": 'r'
        }

    ## Randomized assignment of colors to the effects of keypresses (circles) ##
    randeff = random.getrandbits(1)
    if int(randeff) == 0:
        ColorMapping = {
            "ColorLeft": 'yellow',
            "ColorRight": 'blue'
        }
    else:
        ColorMapping = {
            "ColorLeft": 'blue',
            "ColorRight": 'yellow'
        }

    variables.RandomMapping = {**KeyMapping, **ColorMapping}  # Stores assignments in variables.RandomMapping dict
