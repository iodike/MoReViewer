'''
Imports
'''
from src.include.globals import *


class MRE_LabelWidgetItem(QTableWidgetItem):
    '''
    LabelWidgetItem class
    Creates a table widget item that sorts on labels.
    '''

    def __lt__(self, other):
        '''
        Overwrites '__lt__' function.
        '''
        return self.data(Qt.UserRole) < other.data(Qt.UserRole)

    def updateValue(self, value):
        '''
        Overwrites 'updateValue' function.
        '''
        self.setData(Qt.UserRole, value)
