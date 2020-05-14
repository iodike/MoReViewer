'''
Imports
'''
from src.controller.MRE_ControlWidget import *
from src.table.MRE_FilterTableWidget import *
from src.controller.MRE_InfoWidget import *
from src.controller.MRE_TabWidget import *
from src.controller.MRE_LogArea import *
from src.controller.MRE_MdiSubWindow import *
from src.controller.MRE_MdiArea import *


class MRE_MainWidget(QWidget):
    '''
    MainWidget class
    Creates a main widget.
    '''

    def __init__(self, win: QMainWindow):
        '''
        Constructor
        '''
        super().__init__()
        self.win = win
        self.mdi = MRE_MdiArea(self.win)
        self.cw = MRE_ControlWidget(self.win, self.mdi)
        self.iw = MRE_InfoWidget(self.win, self.mdi)
        self.initUI()

        return

    def initUI(self):
        '''
        Initialise layouts and widgets.
        '''
        glayout = QGridLayout()

        # info tab
        sa1 = QScrollArea()
        sa1.setWidget(self.iw)

        # filter tab
        sa2 = QScrollArea()
        sa2.setWidget(self.cw)

        # tab
        tab = MRE_TabWidget(self.win, sa1, sa2)

        # splitter
        splitter1 = QSplitter()
        splitter1.setOrientation(Qt.Horizontal)
        splitter1.addWidget(self.mdi)
        splitter1.addWidget(tab)

        splitter2 = QSplitter()
        splitter2.setOrientation(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.win.logger)

        glayout.addWidget(splitter2, 0, 0)

        self.setLayout(glayout)
        return

    def addSubWindow(self, dl, name: str):
        '''
        Creates a FilterTable widget from the datalist 'dl'
        and adds it to the MDI area with the name 'name'.
        '''

        # table
        fwidget = MRE_FilterTableWidget(self.win, dl)

        # sub
        sub = MRE_MdiSubWindow(self.win)
        sub.setWindowTitle(name)
        sub.setWidget(fwidget)

        # mdi
        self.mdi.addSubWindow(sub)
        sub.show()

        return

    def closeEvent(self, QCloseEvent):
        '''
        Triggers before main widget is closing.
        Prevents closing main widget without saving project.
        '''
        close = QMessageBox.question(self.win, '', 'Are you sure you want to close the current project? '
                                               'Unsaved changes will get lost.',
                                     QMessageBox.Yes | QMessageBox.No)

        if close == QMessageBox.Yes:
            # show
            self.showNormal()
            self.win.showNormal()
            # delete
            self.deleteLater()
            self.win.mw = None
            self.win.logger = MRE_LogArea(self)
            # accept
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
        return
