'''
Imports
'''
from src.include.globals import *


class MRE_Thread(QThread):
    '''
    Thread class
    Creates a thread.
    '''

    def __init__(self, win):
        '''
        Constructor
        '''
        super().__init__()
        self.win = win
        return
