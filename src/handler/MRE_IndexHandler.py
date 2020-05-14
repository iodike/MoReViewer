'''
Imports
'''
from src.include.globals import *


class MRE_IndexHandler:
    '''
    IndexHandler class
    '''

    def __init__(self, win, config):
        '''
        Constructor
        '''

        # window
        self.win = win

        # config
        self.config = config

        # position of items in file
        self.fileIndexes = initNumList(-1, INDEX_SIZE)

        # position of items in project
        self.projectIndexes = initNumList(-1, INDEX_SIZE)

        # position of items in table
        self.tableIndexes = initNumList(-1, INDEX_SIZE)

        # init
        self.init()

        return

    def init(self):
        '''
        Initialise the index handler.
        '''
        self.createFileIndexes()
        self.createProjectIndexes()
        self.createTableIndexes()
        return

    def getFileIndexes(self):
        '''
        Returns the indexes for the data file.
        '''
        return self.fileIndexes

    def getProjectIndexes(self):
        '''
        Returns the indexes for the project file.
        '''
        return self.projectIndexes

    def getTableIndexes(self):
        '''
        Returns the indexes for the data list.
        '''
        return self.tableIndexes

    def getFileColumnCount(self):
        '''
        Returns the number of indexes/columns for the config file.
        '''
        count = 0
        for index in self.fileIndexes:
            if index != -1:
                count += 1
        return count

    def getProjectColumnCount(self):
        '''
        Returns the number of indexes/columns for the project file.
        '''
        count = 0
        for index in self.projectIndexes:
            if index != -1:
                count += 1
        return count

    def getTableColumnCount(self):
        '''
        Returns the number of indexes/columns for the data list.
        '''
        count = 0
        for index in self.tableIndexes:
            if index != -1:
                count += 1
        return count

    def createFileIndexes(self):
        '''
        Retrieves the indexes from the config file.
        '''
        self.fileIndexes[IINDEX] = self.config.getInputIndex()
        self.fileIndexes[TINDEX] = self.config.getTagsIndex()
        self.fileIndexes[PINDEX] = self.config.getPredictionIndex()
        self.fileIndexes[GINDEX] = self.config.getGroundtruthIndex()
        self.fileIndexes[AINDEX] = self.config.getAlignmentIndex()
        self.fileIndexes[FINDEX] = self.config.getFeaturesIndex()
        self.fileIndexes[DINDEX] = -1
        self.fileIndexes[MINDEX] = -1
        self.fileIndexes[NINDEX] = -1

        return

    def createProjectIndexes(self):
        '''
        Creates the indexes for the project file.
        '''
        i = 0

        if self.config.getInputIndex() != -1:
            self.projectIndexes[IINDEX] = i
            i += 1

        if self.config.getTagsIndex() != -1:
            self.projectIndexes[TINDEX] = i
            i += 1

        if self.config.getPredictionIndex() != -1:
            self.projectIndexes[PINDEX] = i
            i += 1

        if self.config.getGroundtruthIndex() != -1:
            self.projectIndexes[GINDEX] = i
            i += 1

        if self.config.getAlignmentIndex() != -1:
            self.projectIndexes[AINDEX] = i
            i += 1

        if self.config.getFeaturesIndex() != -1:
            self.projectIndexes[FINDEX] = i
            i += 1

        self.projectIndexes[MINDEX] = i
        i += 1

        self.projectIndexes[NINDEX] = i

        return

    def createTableIndexes(self):
        '''
        Creates the indexes for the data list.
        '''
        i = 0

        if self.config.getInputIndex() != -1:
            self.tableIndexes[IINDEX] = i
            i += 1

        if self.config.getTagsIndex() != -1:
            self.tableIndexes[TINDEX] = i
            i += 1

        if self.config.getPredictionIndex() != -1:
            self.tableIndexes[PINDEX] = i
            i += 1

        if self.config.getGroundtruthIndex() != -1:
            self.tableIndexes[GINDEX] = i
            i += 1

        self.tableIndexes[DINDEX] = i
        i += 1

        if self.config.getAlignmentIndex() != -1:
            self.tableIndexes[AINDEX] = i
            i += 1

        if self.config.getFeaturesIndex() != -1:
            self.tableIndexes[FINDEX] = i

        return

    def getIndexLabels(self):
        '''
        Returns the labels for the data indexes.
        '''
        labels = []
        i = 0

        for index in self.tableIndexes:
            if index != -1:
                labels.append(INDEX_LABELS[i])
            i += 1

        return labels
