'''
Imports
'''
from src.wizard.MRE_ConclusionWizardPage import *
from src.wizard.MRE_ImportWizardPage import *
from src.wizard.MRE_IntroWizardPage import *


class MRE_ImportWizard(QWizard):
    '''
    ImportWizard class
    Creates and displays an import wizard.
    '''

    def __init__(self, win, ph):
        '''
        Constructor
        '''
        super().__init__()

        self.setModal(True)

        self.setWindowTitle("Import Wizard")

        self.ph = ph
        self.win = win

        self.page1 = MRE_IntroWizardPage(self.win, self.ph)
        self.page2 = MRE_ImportWizardPage(self.win, self.ph)
        # self.page3 = MRE_FormatWizardPage(self.win, self.ph)
        # self.page4 = MRE_ConfigWizardPage(self.win, self.ph)
        self.page5 = MRE_ConclusionWizardPage(self.win, self.ph)

        self.addPage(self.page1)
        self.addPage(self.page2)
        # self.addPage(self.page3)
        # self.addPage(self.page4)
        self.addPage(self.page5)

        # create new project
        self.button(QWizard.FinishButton).clicked.connect(self.ph.createNewProject)

        self.setFixedSize(800, 500)

        self.show()

        return

    def getDataList(self):
        '''
        Returns the imported data list.
        '''
        return self.page5.dl
