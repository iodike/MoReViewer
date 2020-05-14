'''
Imports
'''
from src.include.globals import *


class MRE_IntroWizardPage(QWizardPage):
    '''
    IntroWizardPage class
    Creates a wizard page for introduction.
    '''

    def __init__(self, mw, ph):
        '''
        Constructor
        '''
        super().__init__()

        self.setTitle("Introduction")

        label = QLabel("The Import Wizard will guide you through the different steps to import your project.")
        label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        return
