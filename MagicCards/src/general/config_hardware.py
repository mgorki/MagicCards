from psychopy import visual, monitors
import pylink

### Monitor configuration ###
scnWIDTH = 1920
scnHEIGHT = 1080
MON = monitors.Monitor('myMac15', width=53.0, distance=60.0) # Has to be adjusted in the final experiment
MON.setSizePix((scnWIDTH, scnHEIGHT))

#WIN = visual.Window((1200, 900), monitor='testMonitor', units='deg', allowStencil=True, color=[-1, -1, -1])  # Just for TESTING. In the final experiment the line below should be activate
WIN = visual.Window((scnWIDTH, scnHEIGHT), fullscr=True, monitor=MON, units='deg', allowStencil=True, color=[-1,-1,-1])

### Eyetracker configuration ###
dummyMode = False  # Tracker simulation if set to True. If the experiment is run with the eyetracker dummyMode must be set to FALSE

if not dummyMode:
    tk = pylink.EyeLink('100.1.1.1')
else:
    tk = pylink.EyeLink(None)

### Use of external buttons ###
BUTTONMODE = False # Set to True if external buttons are used. Otherwise keyboard keys are used.

### Board configuration ###
BOARD_VID_PID = "VID:PID=2341:0043"  # The VID/PID of the Arduino that is used (has to be adjusted according to the model)
BOARD_NAMES = ["Arduino", "USB-SERIAL CH340"]  # List of clear names of any Arduino or other Microcontroler that may be used (has to be adjusted specific model(s) if more than one are connected at the same time)
BAUDRATE = 38400 if BUTTONMODE == True else 9600 # Baudrate depending on whether using a board with buttons or only using board for input of card number
