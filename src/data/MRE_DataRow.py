'''
Imports
'''
from src.handler.MRE_IndexHandler import *


class MRE_DataRow:
    '''
    DataRow class
    Creates an empty data row.
    '''

    def __init__(self, ih):
        '''
        Constructor
        '''
        #
        self.ih = ih

        # read
        self.input = ""
        self.tags = []
        self.prediction = ""
        self.groundtruth = ""
        self.alignment = []
        self.features = []

        # compute
        self.distance = -1
        self.markers = []
        self.notes = ""

        # highlighting
        self.phtml = ""
        self.ghtml = ""

        return

    def init(self):
        '''
        Initialises the data row.
        '''
        self.highlightPrediction()
        self.highlightGroundtruth()
        return

    def toString(self):
        '''
        Converts the data row to a string.
        '''
        # indexes
        indexes = self.ih.getProjectIndexes()

        # max index
        maxs = 0
        for index in indexes:
            maxs = max(maxs, index)

        # string list
        vlist = list(range(maxs+1))

        # fill list
        if indexes[IINDEX] != -1:
            vlist[indexes[IINDEX]] = self.input

        if indexes[TINDEX] != -1:
            vlist[indexes[TINDEX]] = SEMIC_SPLIT.join(self.tags)

        if indexes[PINDEX] != -1:
            vlist[indexes[PINDEX]] = self.prediction

        if indexes[GINDEX] != -1:
            vlist[indexes[GINDEX]] = self.groundtruth

        if indexes[AINDEX] != -1:
            vlist[indexes[AINDEX]] = MINUS_SPLIT.join(self.alignment)

        if indexes[FINDEX] != -1:
            vlist[indexes[FINDEX]] = SPACE_SPLIT.join(self.features)

        if indexes[MINDEX] != -1:
            if self.markers:
                vlist[indexes[MINDEX]] = SEMIC_SPLIT.join(self.markers)
            else:
                vlist[indexes[MINDEX]] = STR_EMPTY

        if indexes[NINDEX] != -1:
            if self.notes:
                vlist[indexes[NINDEX]] = self.notes
            else:
                vlist[indexes[NINDEX]] = STR_EMPTY

        # create output
        xstr = "\t".join(vlist)

        return xstr

    def highlightPrediction(self):
        '''
        Creates a formatted prediction string.
        '''
        out = ""
        if self.prediction and self.groundtruth:
            for i, s in enumerate(difflib.ndiff(self.prediction, self.groundtruth)):
                if s[0] == ' ':
                    out += "<span style='color:green'>" + s[-1] + "</span>"
                elif s[0] == '-':
                    ## False Positives
                    out += "<span style='color:red'>" + s[-1] + "</span>"
                elif s[0] == '+':
                    continue

        self.phtml = out
        return

    def highlightGroundtruth(self):
        '''
        Creates a formatted groundtruth string.
        '''
        out = ""
        if self.prediction and self.groundtruth:
            for i, s in enumerate(difflib.ndiff(self.prediction, self.groundtruth)):
                if s[0] == ' ':
                    out += "<span style='color:green'>" + s[-1] + "</span>"
                elif s[0] == '-':
                    continue
                elif s[0] == '+':
                    ## False Negatives
                    out += "<span style='color:orange'>" + s[-1] + "</span>"

        self.ghtml = out
        return

    def computeLevenshteinDistance(self):
        '''
        Compute the Levenshtein distance between 'prediction' and 'groundtruth'.
        '''
        if self.prediction and self.groundtruth:
            self.distance = jellyfish.levenshtein_distance(self.prediction, self.groundtruth)
        else:
            self.distance = -1
        return

    def getInput(self):
        '''
        Returns the input string.
        '''
        return self.input

    def getTags(self) -> list:
        '''
        Returns the tag list.
        '''
        return self.tags

    def getPrediction(self):
        '''
        Returns the prediction string.
        '''
        return self.prediction

    def getGroundTruth(self):
        '''
        Returns the groundtruth string.
        '''
        return self.groundtruth

    def getAlignment(self):
        '''
        Returns the alignment list.
        '''
        return self.alignment

    def getFeatures(self):
        '''
        Returns the features list.
        '''
        return self.features

    def getMarkers(self):
        '''
        Returns the markers list.
        '''
        return self.markers

    def getNotes(self):
        '''
        Returns the notes string.
        '''
        return self.notes

    def getDistance(self):
        '''
        Returns the Levenshtein distance.
        '''
        return self.distance

    def setInput(self, xinput: str):
        '''
        Sets the input string to 'xinput'.
        '''
        self.input = xinput
        return

    def setTags(self, tags: list):
        '''
        Sets the tags list to 'tags'.
        '''
        self.tags = tags
        return

    def setPrediction(self, prediction: str):
        '''
        Sets the prediction string to 'prediction'.
        '''
        self.prediction = prediction
        self.computeLevenshteinDistance()
        return

    def setGroundTruth(self, groundtruth: str):
        '''
        Sets the groundtruth string to 'groundtruth'.
        '''
        self.groundtruth = groundtruth
        self.computeLevenshteinDistance()
        return

    def setAlignment(self, alignment: list):
        '''
        Sets the alignment list to 'alignment'.
        '''
        self.alignment = alignment
        return

    def setFeatures(self, features: list):
        '''
        Sets the features list to 'features'.
        '''
        self.features = features
        return

    def setMarkers(self, markers: list):
        '''
        Sets the markers list to 'markers'.
        '''
        self.markers = markers
        return

    def setNotes(self, notes: str):
        '''
        Sets the notes string to 'notes'.
        '''
        self.notes = notes
        return

    def setDistance(self, distance: int):
        '''
        Sets the Levenshtein distance to 'distance'.
        '''
        self.distance = distance
        return

    def getPredictionLabel(self):
        '''
        Returns the formatted prediction string.
        '''
        return self.phtml

    def getGroundTruthLabel(self):
        '''
        Returns the formatted groundtruth string.
        '''
        return self.ghtml
