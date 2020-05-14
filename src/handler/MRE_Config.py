'''
Imports
'''
from src.include.globals import *


class MRE_Config:
    '''
    Config class
    Creates a configuration using a configuration file.
    '''

    def __init__(self, win: QMainWindow, file: str):
        '''
        Constructor
        '''
        self.win = win

        self.file = file

        self.data = {}

        self.indexes = []

        self.init()
        return

    def init(self):
        '''
        Initialise the configuration.
        '''
        self.readConfig()
        return

    def readConfig(self):
        '''
        Read the configuration file.
        '''
        with open(self.file) as json_data_file:
            self.data = json.load(json_data_file)
        return

    def writeConfig(self, data):
        '''
        Write the configuration file.
        '''
        with open(self.file, 'w') as outfile:
            json.dump(data, outfile)
        self.data = data
        return

    def getColumns(self):
        '''
        Returns the 'columns' config.
        '''
        if not self.data:
            return {}
        return self.data['columns']

    def getInputIndex(self):
        '''
        Returns the column index for the 'input'.
        '''
        if self.data:
            index = int(self.data['columns']['input'])
            if index > 0:
                return index - 1
        return -1

    def getPredictionIndex(self):
        '''
        Returns the column index for the 'prediction'.
        '''
        if self.data:
            index = int(self.data['columns']['prediction'])
            if index > 0:
                return index - 1
        return -1

    def getTagsIndex(self):
        '''
        Returns the column index for the 'tags'.
        '''
        if self.data:
            index = int(self.data['columns']['tags'])
            if index > 0:
                return index - 1
        return -1

    def getGroundtruthIndex(self):
        '''
        Returns the column index for the 'groundtruth'.
        '''
        if self.data:
            index = int(self.data['columns']['ground-truth'])
            if index > 0:
                return index - 1
        return -1

    def getAlignmentIndex(self):
        '''
        Returns the column index for the 'alignment'.
        '''
        if self.data:
            index = int(self.data['columns']['alignment'])
            if index > 0:
                return index - 1
        return -1

    def getFeaturesIndex(self):
        '''
        Returns the column index for the 'features'.
        '''
        if self.data:
            index = int(self.data['columns']['features'])
            if index > 0:
                return index - 1
        return -1

    def getImportCount(self):
        '''
        Returns the number of specified columns.
        '''
        count = 0
        if self.data:
            for v in self.data['columns'].values():
                if int(v) > 0:
                    count += 1
        return count

    def getFile(self):
        '''
        Returns the configuration file.
        '''
        return self.file
