from psychopy import visual, monitors, gui, core
import pylink
import serial, serial.tools.list_ports
import time
from general.config_hardware import scnWIDTH, scnHEIGHT
import os
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
import pylink
import general.variables as variables

tk = pylink.EyeLink('100.1.1.1')
edfDataFolder = (os.getcwd() + "\\data_recorded\\edfData")
expInfo = {'Subject': '159', 'Sex': 'Female', 'Age': 20, 'Dominant_eye': 'right', 'Dominant_hand': 'right'}
WIN = visual.Window((1200, 900), monitor='testMonitor', units='deg', allowStencil=True, color=[-1, -1, -1])  # Just for TESTING. In the final experiment the line below should be activate



def initTk(expInfo):
    ## Data host ##
    if not os.path.exists(edfDataFolder):
        os.makedirs(edfDataFolder)
    dataFileName = 'Test1234' + '.EDF'
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
    tk.receiveDataFile(dataFileName, str(edfDataFolder + os.sep + dataFileName))
    print("Data saved to: " + dataFileName, edfDataFolder + os.sep + dataFileName)  # For testing

dataFileName = initTk(expInfo)
receiveData(dataFileName)
print("finished")




## presenting the card ##
card_image = "../../MagicCards/resources/images/card_1.jpg"
img = visual.ImageStim(WIN, image=card_image, size=(24, 36))  # All images of cards are roughly 1200 x 1800 pixel
img.draw(WIN)
WIN.flip()
