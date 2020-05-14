'''
Imports
'''
from src.start.MRE_RecentWidget import *


class MRE_StartWidget(QWidget):
    '''
    StartWidget class
    Creates the start widget.
    '''

    def __init__(self, win):
        '''
        Constructor
        '''
        super().__init__()
        self.win = win
        self.rwidget = MRE_RecentWidget(self.win)
        self.initUI()
        return

    def initUI(self):
        '''
        Initialises the layouts and widgets.
        '''
        gLayout = QGridLayout()

        ## new
        button1 = QPushButton("New Project...")
        button1.clicked.connect(self.win.ah.newProject)
        button1.setMinimumSize(200, 50)
        button1.setIcon(QIcon(NEW_WHITE))
        button1.setIconSize(QSize(16, 16))

        ## open
        button2 = QPushButton("Open Project...")
        button2.clicked.connect(self.win.ah.openProject)
        button2.setMinimumSize(200, 50)
        button2.setIcon(QIcon(OPEN_WHITE))
        button2.setIconSize(QSize(16, 16))

        pixLabel = QLabel()
        pixmap = QPixmap(ICON)
        pixLabel.setPixmap(pixmap)
        pixLabel.setAlignment(Qt.AlignCenter)

        titleWidget = QWidget()

        titleLabel = QLabel(self.win.settings.applicationName() + BETA)
        titleLabel.setFont(QFont("Helvetica", 32, QFont.Bold))

        titleLayout = QVBoxLayout()
        titleLayout.addWidget(pixLabel)
        titleLayout.addWidget(titleLabel)
        titleLayout.setAlignment(Qt.AlignCenter)
        titleLayout.setContentsMargins(0, 0, 0, 0)

        titleWidget.setLayout(titleLayout)

        # y, x, yw, xw
        gLayout.addWidget(titleWidget, 0, 0, 4, 4)
        gLayout.addWidget(button1, 4, 0, 1, 4)
        gLayout.addWidget(button2, 5, 0, 1, 4)
        gLayout.addWidget(self.rwidget, 0, 6, 8, 4)
        gLayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(gLayout)
        return
