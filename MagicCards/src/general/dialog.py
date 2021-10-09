from psychopy import gui, core
import general.variables as variables
from experiment.config_experiment import MAPPING_BY_DIALOG

def infoDialog():
    myDlg = gui.Dlg(title="Magic Cards")
    myDlg.addText('Subject info')
    myDlg.addField('Subject number:', str(159))
    myDlg.addField('Sex:', choices=["Female", "Male", "Diverse"])
    myDlg.addField('Age:', 20)
    myDlg.addField('Student:', choices=["No student", "Psychology Student", "Student, other field"])
    myDlg.addField('Dominant eye:', choices=["right", "left"])
    myDlg.addField('Dominant hand:', choices=["right", "left"])
    if MAPPING_BY_DIALOG == True:
        myDlg.addField('BM:', choices=["yl", "nl"])
        myDlg.addField('CM:', choices=["yl", "yr"])
        myDlg.addField('DM:', choices=["sl", "ll"])

    myDlg.addText('Experiment Info')


    ok_data = myDlg.show()  # show dialog and wait for OK or Cancel
    if myDlg.OK:  # or if ok_data is not None
        #print(dict(zip(['Subject', 'Sex', 'Age', 'Dominant_eye', 'Dominant_hand', 'Button_mapping', 'Color_mapping'], ok_data)))
        if MAPPING_BY_DIALOG == True:
            variables.infoBuffer = dict(zip(['Subject', 'Sex', 'Age', 'Student', 'Dominant_eye', 'Dominant_hand', 'Button_mapping', 'Color_mapping', 'Delay_Mapping'], ok_data))
        else:
            variables.infoBuffer = dict(zip(['Subject', 'Sex', 'Age', 'Student', 'Dominant_eye', 'Dominant_hand'], ok_data))
        print(variables.infoBuffer)
        core.wait(2)
    else:
        print('user cancelled')
        exit()
