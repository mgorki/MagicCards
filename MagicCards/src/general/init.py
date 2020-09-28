from psychopy import gui, core
import serial, serial.tools.list_ports
import time
from general.config_hardware import WIN, tk, scnWIDTH, scnHEIGHT, BAUDRATE, ARD_VID_PID
import os
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
import pylink
from experiment.config_experiment import behaviour, edfDataFolder
import random


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
    ports = serial.tools.list_ports.comports(include_links=False)
    i = len(ports)
    arduinos = []
    for port in ports:
        if ARD_VID_PID in port[i]:
            arduinos.append(port.device)  ## Init buttons
            print("Arduino found at: " + port.device)
        else:
            i = i - 1

    if len(arduinos) == 0:
        print("No Arduino found, is it connected to a valid port? Crashing now.")
    elif len(arduinos) == 1:
        try:
            ser = serial.Serial(arduinos[0], BAUDRATE)  ## Init buttons
            print("connected to Arduino at: %s with baudrate: %s" % (arduinos[0], BAUDRATE))
            return ser
        except:
            print("There was an error at connecting to the Arduino. Is everything connected and configured properly?")
    else:
        print("More than one Arduino connected! Make sure only one such device is connected and retry. Crashing now.")

    time.sleep(2)


def waitForKey(ser):
    core.wait(.5)
    ser.reset_input_buffer()  # reset buttons
    while True:
        a = ser.readline().decode().rstrip()  # read button inputs, decode byte string into Unicode, remove \n and \r
        if a != 'r':
            pass
        else:
            ser.reset_input_buffer()  # reset buttons
            break


def initTk(expInfo):
    ## Data host ##
    if not os.path.exists(edfDataFolder):
        os.makedirs(edfDataFolder)
    dataFileName = expInfo['Subject'] + '.EDF'
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
    tk.sendCommand("calibration_type = HV5")
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
    if not os.path.exists(edfDataFolder):
        os.mkdir(edfDataFolder)
    tk.receiveDataFile(dataFileName, 'edfData' + os.sep + dataFileName)
    print("Data saved to: " + dataFileName, 'edfData' + os.sep + dataFileName)  # For testing

def initRandomMapping():
    rand = random.getrandbits(1)
    if int(rand) == 0:
        key_yes = 'r'
        key_no = 'l'
    else:
        key_yes = 'l'
        key_no = 'r'

    KeyMapping = {
        "KeyYes": key_yes,
        "KeyNo": key_no,
    }

    print(KeyMapping)  # For testing
    return KeyMapping
