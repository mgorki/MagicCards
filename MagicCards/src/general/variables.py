#import queue
#from general import init
from psychopy import core
from psychopy.iohub.client import launchHubServer

infoBuffer = {}  # Placeholder for information stored by te initial dialog (dialog.py)
ser = ''  # Placeholder: serial connection to Arduino to which the buttons are connected stored here by init.initSer()
#q = queue.Queue()  # queue for threads
timer = core.Clock()  # init the timer
ITI500 = timer.getTime()
RandomMapping = {}  # Placeholder: mapping of response keys and effect colors stored here by init.initRandomMapping()
io = launchHubServer() # Start the ioHub process. 'io' can now be used during the experiment to access iohub devices and read iohub device events.