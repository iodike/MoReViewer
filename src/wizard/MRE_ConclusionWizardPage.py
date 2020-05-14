'''
Imports
'''
from src.data.MRE_DataList import *


class MRE_ConclusionWizardPage(QWizardPage):
    '''
    ConclusionWizardPage class
    Creates a wizard page for conclusion.
    '''

    def __init__(self, win, ph):
        '''
        Constructor
        '''
        super().__init__()

        self.win = win
        self.ph = ph
        self.dl = MRE_DataList(self.win)

        self.setFinalPage(True)

        self.setTitle("Conclusion")
        self.label = QLabel("You have successfully imported your file.")
        self.label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        return

    def initializePage(self):
        '''
        Initialises the wizard page. (When clicking 'Next')
        '''
        dataFile = self.wizard().field("dataFile")
        configFile = self.wizard().field("configFile")

        # create data object
        self.dl.init(dataFile, configFile, False)

        if not self.dl.isEmpty():
            self.label.setText("You have successfully imported your file.")
        else:
            self.label.setText("Sorry, failed to import file.")
        return

    def cleanupPage(self):
        '''
        Cleans up the wizard page. (When clicking 'Back')
        '''
        self.dl = MRE_DataList(self.win)
        return

    def isComplete(self):
        '''
        Checks whether the wizard step is completed.
        '''
        return not self.dl.isEmpty()
