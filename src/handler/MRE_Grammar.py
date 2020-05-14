'''
Imports
'''
from src.include.globals import *


class MRE_Grammar:
    '''
    Grammar class
    Creates a grammar using a grammar file.
    '''

    def __init__(self, win: QMainWindow, file: str):
        '''
        Constructor
        '''
        self.win = win

        self.file = file

        self.data = {}

        self.init()
        return

    def init(self):
        '''
        Initialise the grammar.
        '''
        self.read()
        return

    def read(self):
        '''
        Read the grammar file.
        '''
        with open(self.file) as json_data_file:
            self.data = json.load(json_data_file)
        return

    def write(self, data):
        '''
        Write to the grammar file.
        '''
        with open(self.file, 'w') as outfile:
            json.dump(data, outfile)
        self.data = data
        return

    def getGrammar(self):
        '''
        Returns the grammar.
        '''
        return self.data['grammar']

    def getGrammarDeps(self):
        '''
        Returns the grammar dependencies.
        '''
        return self.data['grammar-dependencies']
