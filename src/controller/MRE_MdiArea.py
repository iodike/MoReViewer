'''
Imports
'''
from src.include.globals import *


class MRE_MdiArea(QMdiArea):
    '''
    MDIArea class
    Creates an MDI area widget that allows
    to add multiple MDI Subwindows.
    '''

    def __init__(self, win: QMainWindow):
        '''
        Constructor
        '''
        super().__init__()
        self.win = win
        return

    def currentSubWidget(self):
        '''
        Returns the widget of the active MDI subwindow.
        '''
        subwindow = self.currentSubWindow()
        if subwindow:
            return subwindow.widget()
        else:
            self.win.logger.log("No subwindow selected.", LOG_INFO)
        return None

    def currentDataList(self):
        '''
        Returns the datalist of the active MDI subwindow.
        '''
        subwidget = self.currentSubWidget()
        if subwidget:
            return subwidget.dl
        else:
            self.win.logger.log("No subwidget found.", LOG_ERROR)
        return None
