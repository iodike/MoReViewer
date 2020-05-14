'''
Imports
'''
from src.include.globals import *


class MRE_MdiSubWindow(QMdiSubWindow):
    '''
    MDISubwindow class
    Creates a subwindow for the MDI area.
    '''

    def __init__(self, win: QMainWindow):
        '''
        Constructor
        '''
        super().__init__()
        self.win = win
        return

    def closeEvent(self, QCloseEvent):
        '''
        Triggers before sub window is closing.
        Prevents closing sub window without saving project.
        '''
        close = QMessageBox.question(self.win, '', 'Are you sure you want to delete the current document? '
                                               'Unsaved changes will get lost.',
                                     QMessageBox.Yes | QMessageBox.No)

        if close == QMessageBox.Yes:
            self.deleteLater()
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
        return
