'''
Imports
'''
from src.include.globals import *

'''
Splash screen messages.
'''
messages = [
    'Convincing AI not to turn evil.'
]


class MRE_Splashscreen(QSplashScreen):
    '''
    SplashScreen class
    Creates a splash screen.
    '''

    def __init__(self, app):
        '''
        Constructor
        '''
        pixmap = QPixmap("media/splash/abstract-blur.png")
        super().__init__(pixmap)
        self.pbar = QProgressBar(self)
        self.app = app
        self.mctr = 0
        self.initUI()
        return

    def initUI(self):
        '''
        Initialises the splash screen.
        '''
        self.pbar.setMinimum(0)
        self.pbar.setMaximum(100)
        self.pbar.setValue(50)
        self.pbar.setFixedWidth(200)
        self.pbar.move(200, 300)
        self.pbar.show()
        self.show()
        return

    def drawContents(self, painter):
        '''
        Draws the contents of the splash screen.
        '''
        return

    def update(self):
        '''
        Updates the splash screen.
        '''
        self.showMessage(messages[self.mctr])
        self.app.processEvents()
        self.mctr += 1
        return
