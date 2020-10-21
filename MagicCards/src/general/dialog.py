from psychopy import gui, core
import general.variables as variables

def infoDialog():
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
        print(dict(zip(['Subject', 'Sex', 'Age', 'Dominant_eye', 'Dominant_hand'], ok_data)))
        variables.infoBuffer = dict(zip(['Subject', 'Sex', 'Age', 'Dominant_eye', 'Dominant_hand'], ok_data))
        print(variables.infoBuffer)
        core.wait(2)
    else:
        print('user cancelled')
        exit()
