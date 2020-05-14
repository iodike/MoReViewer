'''
Imports
'''
from src.include.globals import *


class MRE_NumericWidgetItem(QTableWidgetItem):
    '''
    NumericWidgetItem class
    Creates a table widget item that sorts on numbers.
    '''

    def __init__(self, text, sortKey):
        '''
        Constructor
        '''
        QTableWidgetItem.__init__(self, text, QTableWidgetItem.UserType)
        self.sortKey = sortKey

    def __lt__(self, other):
        '''
        Overwrites '__lt__' function
        '''
        return self.sortKey < other.sortKey
