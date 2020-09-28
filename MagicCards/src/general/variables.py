import queue
from general import init
from psychopy import core

ser = init.initSer()  # init Arduino to which the buttons are connected
#q = queue.Queue()  # queue for threads
timer = core.Clock()  # init the timer
ITI500 = timer.getTime()