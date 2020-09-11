from psychopy import visual, core
from general.config_hardware import WIN

def circle(side):
    circleD = visual.GratingStim(WIN, color=(0, 1, 1), colorSpace='rgb', tex=None, mask='circle', size=30, pos=(0, 0))

    if side == 'right':
        circleD.color = "blue"
        circleD.pos = (120, 0)
    else:
        circleD.color = "yellow"
        circleD.pos = (-120, 0)

    circleD.draw()
    WIN.flip()
    core.wait(0.400)

def reaction(key):
    if key == 'r':
        circle(side='right')
    elif key == 'l':
        circle(side='left')
    WIN.flip()
    core.wait(0.5)