'''
Imports
'''
from src.include.globals import *


class MRE_InfoWidget(QWidget):
    '''
    InfoWidget class
    Creates an info widget with multiple
    subviews to display information.
    '''

    def __init__(self, win: QMainWindow, mdi: QMdiArea):
        '''
        Constructor
        '''
        super().__init__()

        # main window
        self.win = win

        # mdi
        self.mdi = mdi

        # table
        self.tw = self.mdi.currentSubWidget()

        # row
        self.row = -1

        # layout
        self.layout = QGridLayout()

        # controls
        self.featureTable = QTableWidget()
        self.markers = QListWidget()
        self.notes = QPlainTextEdit()

        # init
        self.initUI()

        return

    def initUI(self):
        '''
        Initializes the layouts and widgets.
        '''
        #
        gbox1 = QGroupBox("Alignments/Features")
        gbox2 = QGroupBox("Marker")
        gbox3 = QGroupBox("Notes")

        gbox1.setMinimumSize(360, 200)
        gbox2.setMinimumSize(360, 200)
        gbox3.setMinimumSize(360, 200)

        #
        gl1 = QHBoxLayout()
        gbox1.setLayout(gl1)

        gl2 = QHBoxLayout()
        gbox2.setLayout(gl2)

        gl3 = QHBoxLayout()
        gbox3.setLayout(gl3)

        # widget 1 - Features
        self.featureTable.setColumnCount(3)
        self.featureTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.featureTable.setHorizontalHeaderLabels(["Prediction", "Alignment", "Features"])

        # widget 2 - Marker
        self.markers.addItem("COPY ERROR")
        self.markers.setDisabled(True)

        # widget3 - Notes
        self.notes.setStatusTip("Insert your notes.")
        self.notes.setReadOnly(True)

        #
        gl1.addWidget(self.featureTable)
        gl2.addWidget(self.markers)
        gl3.addWidget(self.notes)

        #
        self.layout.addWidget(gbox1, 0, 0, 1, 10)
        self.layout.addWidget(gbox2, 1, 0, 1, 10)
        self.layout.addWidget(gbox3, 2, 0, 1, 10)

        # set layout
        self.setLayout(self.layout)

        # trigger
        self.mdi.subWindowActivated.connect(self.updateSubWindow)
        self.notes.textChanged.connect(self.saveNotes)

        return

    def saveNotes(self):
        '''
        Saves the notes to the data list.
        '''
        if self.tw:
            if self.row >= 0:
                if self.tw.dl:
                    text = self.notes.toPlainText()
                    self.tw.dl.getDataRow(self.row).setNotes(text)
        return

    def updateSubWindow(self):
        '''
        Resets the info tab widgets.
        '''
        if self.mdi.currentSubWidget():

            # same subwindow
            if self.tw == self.mdi.currentSubWidget():
                return

            self.tw = self.mdi.currentSubWindow().widget()
            if self.tw:
                self.clearControls()
        return

    def onItemClicked(self, item: QTableWidgetItem):
        '''
        Trigger: Click on TableWidgetItem.
        Action: Updates info widgets.
        '''
        self.row = item.row()
        self.updateControls()
        return

    def updateControls(self):
        '''
        Updates all widgets on document switch.
        '''
        self.updateFeatureTable()
        self.updateMarkers()
        self.updateNotes()
        return

    def updateFeatureTable(self):
        '''
        Updates the features widget on document switch.
        '''
        self.featureTable.clearContents()

        prediction = ""
        alignment = ""
        features = ""

        if self.tw:

            # indexes
            indexes = self.tw.dl.ih.getTableIndexes()

            # prediction
            item1 = self.tw.item(self.row, indexes[PINDEX])
            if item1:
                prediction = item1.data(Qt.UserRole)

            # alignment
            item2 = self.tw.item(self.row, indexes[AINDEX])
            if item2:
                alignment = parseAlignment(item2.text())

            # features
            item3 = self.tw.item(self.row, indexes[FINDEX])
            if item3:
                features = parseFeatures(item3.text())

            # max size
            maxs = max(len(prediction), len(alignment), len(features))

            # row count
            self.featureTable.setRowCount(maxs)

            #
            if prediction:
                for i in range(len(prediction)):
                    item = QTableWidgetItem(prediction[i])
                    item.setTextAlignment(Qt.AlignCenter)
                    self.featureTable.setItem(i, 0, item)

            if alignment:
                for i in range(len(alignment)):
                    item = QTableWidgetItem(alignment[i])
                    item.setTextAlignment(Qt.AlignCenter)
                    self.featureTable.setItem(i, 1, item)

            if features:
                for i in range(len(features)):
                    item = QTableWidgetItem(features[i])
                    item.setTextAlignment(Qt.AlignCenter)
                    self.featureTable.setItem(i, 2, item)

        return

    def updateMarkers(self):
        '''
        Updates the markers widget on document switch.
        '''
        if self.tw:
            self.markers.setCurrentRow(0)
        return

    def updateNotes(self):
        '''
        Updates the notes widget on document switch.
        '''
        if self.tw:

            # enable
            self.notes.setReadOnly(False)

            # get notes
            txt = ""
            if self.tw.dl:
                txt = self.tw.dl.getDataRow(self.row).getNotes()

            # set notes
            self.notes.setPlainText(txt)

        return

    def clearControls(self):
        '''
        Resets the contents of the widgets.
        '''
        self.featureTable.clearContents()
        self.markers.setCurrentRow(0)
        self.notes.clear()
        self.notes.setReadOnly(True)
        return

