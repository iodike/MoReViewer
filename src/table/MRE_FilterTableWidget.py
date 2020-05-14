'''
Imports
'''
from src.table.MRE_TableWidget import *


class MRE_FilterTableWidget(MRE_TableWidget):
    '''
    FilterTableWidget class
    '''

    def __init__(self, win, dl):
        '''
        Constructor
        '''
        super().__init__(win, dl)

        ##
        self.items = self.getAllItems()

        ##
        self.rows = self.getAllRows()

        ##
        self.distance = 0

        ## (index, tag)
        self.tags = []
        for i in range(0, len(GRAMMAR)):
            self.tags.append((0, ""))

        ##
        self.wordCount = 0

        ##
        self.regex = DEFAULT_REGEX

        return

    def hideAll(self):
        '''
        Hide all rows.
        '''
        for row in self.getAllRows():
            self.hideRow(row)
        return

    def showAll(self):
        '''
        Show all rows.
        '''
        for row in self.getAllRows():
            self.showRow(row)
        return

    def filter(self):
        '''
        Filter rows.
        '''

        self.rows = self.getAllRows()

        self.filterByDistance()

        self.filterByTags()

        self.filterByWordCount()

        self.filterByRegex()

        self.showItems()

        return

    def filterByDistance(self):
        '''
        Filter rows by distance.
        '''
        frows = []

        indexes = self.dl.ih.getTableIndexes()

        for row in self.rows:

            item = self.item(row, indexes[DINDEX])

            if int(item.text()) >= self.distance:

                frows.append(row)

        self.rows = intersection(self.rows, frows)

        return

    def filterByTags(self):
        '''
        Filter rows by grammatical tag.
        '''

        frows = []

        indexes = self.dl.ih.getTableIndexes()

        for row in self.rows:

            item = self.item(row, indexes[TINDEX])

            if isSublistOf(self.getTagWords(), parseTags(item.text())):

                frows.append(row)

        self.rows = intersection(self.rows, frows)

        return

    def filterByWordCount(self):
        '''
        Filter rows by word count.
        '''

        frows = []

        indexes = self.dl.ih.getTableIndexes()

        for row in self.rows:

            item = self.item(row, indexes[IINDEX])

            if len(item.text().split()) >= self.wordCount:

                frows.append(row)

        self.rows = intersection(self.rows, frows)

        return

    def filterByRegex(self):
        '''
        Filter rows by regular expression.
        '''

        frows = []

        indexes = self.dl.ih.getTableIndexes()

        for row in self.rows:

            item = self.item(row, indexes[IINDEX])

            if re.search(self.regex, item.text()):

                frows.append(row)

        self.rows = intersection(self.rows, frows)

        return

    def showItems(self):
        '''
        Show filtered rows.
        '''

        # hide all
        for row in self.getAllRows():
            self.hideRow(row)

        # show filtered
        for row in self.rows:
            self.showRow(row)

        self.win.logger.log("Filter applied: " + str(len(self.rows)) + "/" + str(len(self.getAllRows())) +
                            " remaining.", LOG_INFO)

        return

    def getTagWords(self):
        '''
        Returns the tag words from the tags list.
        '''
        words = []
        for tag in self.tags:
            if tag[1]:
                words.append(tag[1])
        return words

    def resetTable(self):
        '''
        Resets the table.
        '''

        # reset items
        self.items = self.getAllItems()

        # reset rows
        self.rows = self.getAllRows()

        # reset values
        self.distance = 0

        self.tags = []
        for i in range(0, len(GRAMMAR)):
            self.tags.append((0, ""))

        self.wordCount = 0

        self.regex = DEFAULT_REGEX

        #
        self.filter()

        return

    def setDistance(self, distance: int):
        '''
        Sets and filters on the distance.
        '''
        self.distance = distance
        self.filterByDistance()
        return

    def setTags(self, tags: list):
        '''
        Sets and filters on tags.
        Tags are initialised as list of (index, tag)-tuples.
        '''
        self.tags = tags
        self.filterByTags()
        return

    def setWordCount(self, wordCount: int):
        '''
        Sets and filters on the word count.
        '''
        self.wordCount = wordCount
        self.filterByWordCount()
        return

    def setRegex(self, regex):
        '''
        Sets and filters on the regular expression.
        '''
        self.regex = regex
        self.filterByRegex()
        return
