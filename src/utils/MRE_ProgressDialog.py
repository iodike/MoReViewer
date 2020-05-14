'''
Imports
'''
from src.utils.MRE_Thread import *


class MRE_ProgressDialog(QProgressDialog):
    '''
    ProgressDialog class
    Creates a progress dialog.
    '''

    def __init__(self,  parent, labelText="Please wait...", cancelButtonText="Cancel", minimum=0, maximum=100):
        '''
        Constructor
        '''
        super().__init__(labelText, cancelButtonText, minimum, maximum, parent)

        self.setWindowModality(Qt.WindowModal)
        self.setAutoReset(True)
        self.setAutoClose(True)
        self.resize(300, 100)
        return

    def start(self, maxv=100):
        '''
        Start the progress dialog.
        '''
        self.setMaximum(maxv)
        self.show()
        self.setValue(0)
        return

    def stop(self):
        '''
        Stop the progress dialog.
        '''
        self.setValue(self.maximum())
        self.hide()
        return
