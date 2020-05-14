'''
Imports
'''
from src.data.MRE_DataRow import *
from src.handler.MRE_Config import *
from src.handler.MRE_IndexHandler import *


class MRE_DataList:
    '''
    DataList class
    Creates an empty data list.
    '''

    def __init__(self, win: QMainWindow):
        '''
        Constructor
        '''

        # main window
        self.win = win

        # data
        self.dataList = []

        # stats
        self.maxDistance = 0
        self.tags = []

        # config
        self.ih = None

        return

    def init(self, dfile, cfile, isProject=False):
        '''
        Creates an 'index handler' with the config file 'cfile'.
        Initialises the data list with an 'index handler' and
        the data file 'dfile'.
        '''
        config = MRE_Config(self.win, cfile)
        self.ih = MRE_IndexHandler(self.win, config)
        self.createList(dfile, isProject)
        self.computeStatistics()
        return

    def update(self, rowList: list):
        '''
        Updates the dataList with the rows from the 'rowList'.
        '''
        self.dataList.clear()
        for row in rowList:
            self.addRow(row)
        self.computeStatistics()
        return self

    def toString(self):
        '''
        Returns the data list as string.
        '''
        xstr = ""

        # add data
        for i in range(0, self.getRowCount()):
            xstr += self.dataList[i].toString() + "\n"

        return xstr

    def isEmpty(self):
        '''
        Checks if the data list is empty.
        '''
        return self.getRowCount() == 0

    def getData(self):
        '''
        Returns the data list.
        '''
        return self.dataList

    def getDataRow(self, row: int):
        '''
        Returns the row at position 'row'.
        '''
        return self.dataList[row]

    def getTags(self):
        '''
        Returns a set of all tags from the data list.
        '''
        return self.tags

    def getMaxDistance(self):
        '''
        Returns the maximum Levenshtein distance within the data list.
        '''
        return self.maxDistance

    def getRowCount(self):
        '''
        Returns the number of rows within the data list.
        '''
        return len(self.dataList)

    def getColumnCount(self):
        '''
        Returns the number of columns within the data list.
        '''
        if self.getRowCount() > 0:
            return len(self.dataList[0])
        else:
            return 0

    def setData(self, data: list):
        '''
        Sets the data list to 'data'.
        '''
        self.dataList = data
        return

    def setDataRow(self, index: int, dataRow: MRE_DataRow):
        '''
        Sets the data row at position 'index' to 'dataRow'.
        '''
        self.dataList[index] = dataRow

    def addRow(self, dataRow: MRE_DataRow):
        '''
        Appends the 'dataRow' to the data list.
        '''
        self.dataList.append(dataRow)

    def getTagSet(self):
        '''
        Updates 'tags' with a set of all tags
        within the data list.
        '''
        tags = []
        for row in self.dataList:
            for tag in row.getTags():
                if tag not in tags:
                    tags.append(tag)
        self.tags = tags
        return

    def getMaxDistance(self):
        '''
        Updates 'maxDistance' with the maximum
        Levenshtein distance within the data list.
        '''
        maxd = 0
        for row in self.dataList:
            if row.getDistance() > maxd:
                maxd = row.getDistance()
        self.maxDistance = maxd
        return

    def createList(self, file: str, isProject: bool):
        '''
        Initialises the data list with data from the file 'file'.
        '''
        dataList = []
        rawList = readFileAsList(file)

        # check rows
        if self.getRowCount() == 0:
            return False

        if isProject:
            indexes = self.ih.getProjectIndexes()
        else:
            indexes = self.ih.getFileIndexes()

        # check sizes
        rsize = len(rawList[0])

        if isProject:
            esize = self.ih.getProjectColumnCount()

        else:
            esize = self.ih.getFileColumnCount()

        #
        # check
        #
        if esize != rsize:
            showMessage("File has too few columns.\nCheck your config file!",
                        "Expected " + str(esize) + ", but got " + str(rsize) + ".")
            return False

        # create list
        for raw in rawList:

            dataRow = MRE_DataRow(self.ih)

            # input
            if indexes[IINDEX] >= 0:
                dataRow.setInput(raw[indexes[IINDEX]])

            # tags
            if indexes[TINDEX] >= 0:
                dataRow.setTags(parseTags(raw[indexes[TINDEX]]))

            # prediction
            if indexes[PINDEX] >= 0:
                dataRow.setPrediction(raw[indexes[PINDEX]])

            # groundtruth
            if indexes[GINDEX] >= 0:
                dataRow.setGroundTruth(raw[indexes[GINDEX]])

            # alignment
            if indexes[AINDEX] >= 0:
                dataRow.setAlignment(parseAlignment(raw[indexes[AINDEX]]))

            # features
            if indexes[FINDEX] >= 0:
                dataRow.setFeatures(parseFeatures(raw[indexes[FINDEX]]))

            # markers
            if indexes[MINDEX] >= 0:
                if raw[indexes[MINDEX]] != STR_EMPTY:
                    dataRow.setMarkers(parseMarkers(raw[indexes[MINDEX]]))

            # notes
            if indexes[NINDEX] >= 0:
                if raw[indexes[NINDEX]] != STR_EMPTY:
                    dataRow.setNotes(raw[indexes[NINDEX]])

            # add to list
            dataRow.init()
            dataList.append(dataRow)

        #
        self.dataList = dataList
        return True

    def computeStatistics(self):
        '''
        Compute data list statistics:
        - maximum Levenshtein distance
        - tag set without duplicates
        '''
        self.computeMaxDistance()
        self.computeTagSet()
        return
