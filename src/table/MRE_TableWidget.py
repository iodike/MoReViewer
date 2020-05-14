'''
Imports
'''
from src.table.MRE_LabelWidgetItem import *
from src.table.MRE_NumericWidgetItem import *


class MRE_TableWidget(QTableWidget):
    '''
    TableWidget class
    Creates a table widget.
    '''

    def __init__(self, win, dl):
        '''
        Constructor
        '''
        super().__init__()

        self.win = win
        self.dl = dl

        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.createTable()

        palette = self.palette()

        if darkdetect.isDark():
            palette.setBrush(QPalette.Highlight, QBrush(Qt.black))
            palette.setBrush(QPalette.HighlightedText, QBrush(Qt.white))
        else:
            palette.setBrush(QPalette.Highlight, QBrush(Qt.white))
            palette.setBrush(QPalette.HighlightedText, QBrush(Qt.black))

        self.setPalette(palette)

        self.itemDoubleClicked.connect(self.win.mw.iw.onItemClicked)

        return

    def createTable(self):
        '''
        Initialises the data table.
        '''

        data = self.dl.getData()

        # get sort
        self.setSortingEnabled(False)
        sindex = self.horizontalHeader().sortIndicatorSection()
        sorder = self.horizontalHeader().sortIndicatorOrder()

        # set table
        self.setHidden(True)
        self.clearContents()
        self.initColumns(self.dl.ih.getTableColumnCount())
        self.initRows(self.dl.numRows)
        self.initHeaders()
        self.showData(data)
        self.setHidden(False)

        # set sort
        self.sortItems(sindex, sorder)
        self.setSortingEnabled(True)

        return

    def showData(self, data):
        '''
        Inserts the datalist 'data' into the table.
        '''

        indexes = self.dl.ih.getTableIndexes()

        si = 0
        for row in data:

            #
            ip = row.getInput()

            #
            tags = SEMIC_SPLIT.join(row.getTags())

            #
            pd = row.getPrediction()

            #
            gt = row.getGroundTruth()

            #
            ld = row.getDistance()

            #
            al = MINUS_SPLIT.join(row.getAlignment())

            #
            ft = SPACE_SPLIT.join(row.getFeatures())

            #
            # set items
            #

            # input
            if ip:
                self.setItem(si, indexes[IINDEX], QTableWidgetItem(ip))

            # prediction
            if pd:
                plabel = QLabel(row.getPredictionLabel())
                plabel.setTextFormat(Qt.RichText)
                pitem = MRE_LabelWidgetItem()
                pitem.setData(Qt.UserRole, pd)
                self.setItem(si, indexes[PINDEX], pitem)
                self.setCellWidget(si, indexes[PINDEX], plabel)

            # ground truth
            if gt:
                glabel = QLabel(row.getGroundTruthLabel())
                glabel.setTextFormat(Qt.RichText)
                gitem = MRE_LabelWidgetItem()
                gitem.setData(Qt.UserRole, gt)
                self.setItem(si, indexes[GINDEX], gitem)
                self.setCellWidget(si, indexes[GINDEX], glabel)

            # tags
            if tags:
                self.setItem(si, indexes[TINDEX], QTableWidgetItem(tags))

            # levenshtein distance
            if ld != -1:
                self.setItem(si, indexes[DINDEX], MRE_NumericWidgetItem(str(ld), ld))

            # alignment
            if al:
                self.setItem(si, indexes[AINDEX], QTableWidgetItem(al))

            # features
            if ft:
                self.setItem(si, indexes[FINDEX], QTableWidgetItem(ft))

            # next row
            si += 1

        self.hideColumn(indexes[AINDEX])
        self.hideColumn(indexes[FINDEX])

        return

    def initColumns(self, ncols):
        '''
        Initialises the table columns.
        '''
        if ncols:
            self.setColumnCount(ncols)

            for i in range(0, ncols):
                self.setColumnWidth(i, 150)
        else:
            self.setColumnCount(0)
        return

    def initRows(self, nrows):
        '''
        Initialises the table rows.
        '''
        if nrows:
            self.setRowCount(nrows)
        else:
            self.setRowCount(0)
        return

    def initHeaders(self):
        '''
        Initialises the table headers.
        '''
        labels = self.dl.ih.getIndexLabels()
        self.setHorizontalHeaderLabels(labels)
        return

    def getAllItems(self):
        '''
        Returns all data rows.
        '''
        items = []
        for row in range(0, self.rowCount()):
            for column in range(0, self.columnCount()):
                items.append(self.item(row, column))
        return items

    def getAllRows(self):
        '''
        Returns the number of rows.
        '''
        return range(0, self.rowCount())

