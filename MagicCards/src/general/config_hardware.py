from psychopy import visual, monitors
import pylink

### Monitor configuration ###
scnWIDTH = 1920
scnHEIGHT = 1080
MON = monitors.Monitor('myMac15', width=53.0, distance=60.0) # Has to be adjusted in the final experiment
MON.setSizePix((scnWIDTH, scnHEIGHT))

WIN = visual.Window((1200, 900), monitor='testMonitor', units='deg', allowStencil=True, color=[-1, -1, -1])  # Just for TESTING. In the final experiment the line below should be activate
#WIN = visual.Window((scnWidth, scnHeight), fullscr=True, monitor=MON, units='deg', allowStencil=True, color=[-1,-1,-1])

### Eyetracker configuration ###
dummyMode = True  # Tracker simulation. If the experiment is run with the eyetracker dummyMode must be set to FALSE

if not dummyMode:
    tk = pylink.EyeLink('100.1.1.1')
else:
    tk = pylink.EyeLink(None)

### Arduino configuration ###
ARD_VID_PID = "VID:PID=2341:0043"  # The VID/PID of the Arduino that is used (has to be adjusted according to the model)
ARD_NAME = "Arduino"  # The clear name of the Arduino that is used (has to be adjusted specific model if more than one)
BAUDRATE = 38400
