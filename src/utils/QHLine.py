'''
Imports
'''
from PyQt5.QtWidgets import QFrame


class QHLine(QFrame):
    '''
    QHLine class
    Creates a horizontal line.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        return
