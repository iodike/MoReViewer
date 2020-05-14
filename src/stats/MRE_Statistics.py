'''
Imports
'''
from src.include.globals import *


class MRE_Statistics:
    '''
    Statistics class
    Manages the statistics.
    '''

    def __init__(self, win: QMainWindow, dl):
        '''
        Constructor
        '''
        self.win = win
        self.dl = dl
        return

    def getDistanceAmounts(self):
        '''
        Returns the count number for each distance.
        '''
        if self.dl:
            xlist = []
            for i in range(0, self.dl.maxDistance + 1):
                xlist.append(0)

            for row in self.dl.dataList:
                distance = row.getDistance()
                xlist[distance] += 1

            return toDict(xlist)
        return {}

    def getTagAmounts(self):
        '''
        Returns the count number for each tag.
        '''
        if self.dl:
            xdict = {}
            for i in range(0, len(self.dl.tags)):
                e = self.dl.tags[i]
                xdict[e] = 0

            for row in self.dl.dataList:
                for tag in row.getTags():
                    xdict[tag] += 1

            return xdict
        return {}

    def getTagMeanDistance(self):
        '''
        Returns the mean distance for each tag.
        '''
        if self.dl:
            xdict = {}
            distList = {}

            for i in range(0, len(self.dl.tags)):
                e = self.dl.tags[i]
                xdict[e] = 0
                distList[e] = []

            for row in self.dl.dataList:
                for tag in row.getTags():
                    distList[tag].append(row.getDistance())

            for k in xdict.keys():
                xdict[k] = statistics.mean(distList[k])

            return xdict
        return {}

    def getTagMedianDistance(self):
        '''
        Returns the median distance for each tag.
        '''
        if self.dl:
            xdict = {}
            distList = {}

            for i in range(0, len(self.dl.tags)):
                e = self.dl.tags[i]
                xdict[e] = 0
                distList[e] = []

            for row in self.dl.dataList:
                for tag in row.getTags():
                    distList[tag].append(row.getDistance())

            for k in xdict.keys():
                xdict[k] = statistics.median(distList[k])

            return xdict
        return {}
