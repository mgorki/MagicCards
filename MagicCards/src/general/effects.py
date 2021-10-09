from psychopy import visual, core
import random
from general.config_hardware import WIN
import general.variables as variables
from experiment.config_experiment import DURATION_EFFECT


def circle(side):
    circleD = visual.GratingStim(WIN, color=(0, 1, 1), colorSpace='rgb', tex=None, mask='circle', size=3, pos=(0, 0))

    if side == 'right':
        circleD.color = str(variables.Mapping["ColorLeft"])
        circleD.pos = (15, 0)
    else:
        circleD.color = str(variables.Mapping["ColorRight"])
        circleD.pos = (-15, 0)

    circleD.draw()
    WIN.flip()
    core.wait(DURATION_EFFECT)


def reaction(key):
    if key == 'r':
        circle(side='right')
    elif key == 'l':
        circle(side='left')
    WIN.flip()
    #core.wait(0.5)


def cross():
    # cross = visual.ShapeStim(WIN, vertices=((0, -0.5), (0, 0.5), (0, 0), (-0.5, 0), (0.5, 0)), lineWidth=5, closeShape=False, lineColor="white")
    cross = visual.GratingStim(WIN, color="white", colorSpace='rgb', tex=None, mask='cross', size=1)
    cross.draw()
    WIN.flip()

