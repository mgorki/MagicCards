from general import dialog
from psychopy import core
dialog.infoDialog()

core.wait(1)

from experiment.experiment_main import main
main()
