'''
Imports
'''
from src.stats.MRE_Statistics import *


class MRE_TabWidget(QTabWidget):
    '''
    Creates a tab widget that organises multiple views as tabs:
    - Tab 1: InfoWidget
    - Tab 2: ControlWidget
    '''

    def __init__(self, win, infoTab, filterTab):
        '''
        Constructor
        '''
        super().__init__()

        self.win = win

        self.infoTab = infoTab
        self.filterTab = filterTab

        self.initUI()
        return

    def initUI(self):
        '''
        Initialises the tab widget.
        '''

        self.addTab(self.infoTab, "Info")
        self.addTab(self.filterTab, "Filter")
        return
