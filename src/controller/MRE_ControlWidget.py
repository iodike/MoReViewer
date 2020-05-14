"""
Imports
"""
from src.stats.MRE_StatsWindow import *


class MRE_ControlWidget(QWidget):
    '''
    ControlWidget class
    Creates a widget with multiple controls, that can
    manipulate subwindows within the given MDI window.
    '''

    def __init__(self, win: QMainWindow, mdi: QMdiArea):
        '''
        Constructor
        '''
        super().__init__()

        # win
        self.win = win

        # mdi
        self.mdi = mdi

        # table
        self.tw = self.mdi.currentSubWidget()

        # stats
        self.sw = None

        # trigger
        self.mdi.subWindowActivated.connect(self.updateSubWindow)

        # layout
        self.layout = QGridLayout()

        # create controls
        self.showControls()

        # init controls
        self.initControls()

        return

    def updateSubWindow(self):
        '''
        Updates the controls for the active subwindow.
        When no window is selected, the controls are disabled.
        '''
        if self.mdi.currentSubWidget():

            if self.tw == self.mdi.currentSubWidget():
                return

            self.tw = self.mdi.currentSubWidget();
            self.disableControls(False)
            self.updateControls()
        else:
            self.disableControls(True)
        return

    def showControls(self):
        '''
        Creates the layouts and controls for the widget.
        '''

        # group boxes
        gbox1 = QGroupBox("Filter by Lexis")
        gbox2 = QGroupBox("Filter by Number")
        gbox3 = QGroupBox("Filter by Cases")
        gbox4 = QGroupBox("Filter by Mood")
        gbox5 = QGroupBox("Filter by Tense")
        gbox6 = QGroupBox("Filter by Person")
        gbox7 = QGroupBox("Filter by Regex")
        gbox8 = QGroupBox("Filter by Distance (>=)")
        gbox9 = QGroupBox("Filter by Word Count (>=)")
        gbox10 = QGroupBox("Select Statistics")
        gbox11 = QGroupBox("Reset Settings")

        gbox1.setMaximumSize(200, 200)
        gbox2.setMaximumSize(200, 200)
        gbox3.setMaximumSize(200, 200)
        gbox4.setMaximumSize(200, 200)
        gbox5.setMaximumSize(200, 200)
        gbox6.setMaximumSize(200, 200)
        gbox7.setMaximumSize(450, 200)
        gbox8.setMaximumSize(200, 200)
        gbox9.setMaximumSize(200, 200)
        gbox10.setMaximumSize(450, 200)
        gbox11.setMaximumSize(450, 200)

        # group layouts
        gl1 = QVBoxLayout()
        gbox1.setLayout(gl1)
        gl2 = QVBoxLayout()
        gbox2.setLayout(gl2)
        gl3 = QVBoxLayout()
        gbox3.setLayout(gl3)
        gl4 = QVBoxLayout()
        gbox4.setLayout(gl4)
        gl5 = QHBoxLayout()
        gbox5.setLayout(gl5)
        gl6 = QVBoxLayout()
        gbox6.setLayout(gl6)
        gl7 = QVBoxLayout()
        gbox7.setLayout(gl7)
        gl8 = QVBoxLayout()
        gbox8.setLayout(gl8)
        gl9 = QVBoxLayout()
        gbox9.setLayout(gl9)
        gl10 = QHBoxLayout()
        gbox10.setLayout(gl10)
        gl11 = QVBoxLayout()
        gbox11.setLayout(gl11)

        # widgets - Tags
        self.selects = []
        for key, value in GRAMMAR.items():
            e = ["ALL"]
            e += list(value.keys())
            s = QListWidget()
            s.addItems(e)
            self.selects.append(s)

        # widget 7 - Regex
        self.edit1 = QLineEdit(DEFAULT_REGEX)

        # widget 8 - Distance
        self.spin1 = QSpinBox()
        self.spin1.setValue(0)

        # widget 9 - Word Count
        self.spin2 = QSpinBox()
        self.spin2.setValue(0)

        # widget 10 - Statistics
        stats = ["Select Statistic"]
        stats += STATS_OPTIONS
        self.combo2 = QComboBox()
        self.combo2.addItems(stats)
        self.button2 = QPushButton("SHOW")

        # widget 11 - Default
        self.button3 = QPushButton("RESET")

        # add layouts
        gl1.addWidget(self.selects[0])
        gl2.addWidget(self.selects[1])
        gl3.addWidget(self.selects[2])
        gl4.addWidget(self.selects[3])
        gl5.addWidget(self.selects[4])
        gl6.addWidget(self.selects[5])
        gl7.addWidget(self.edit1)
        gl8.addWidget(self.spin1)
        gl9.addWidget(self.spin2)
        gl10.addWidget(self.combo2)
        gl10.addWidget(self.button2)
        gl11.addWidget(self.button3)

        # add widget (yp, xp, yw, xw)
        self.layout.addWidget(gbox1, 0, 0, 1, 1)
        self.layout.addWidget(gbox2, 0, 1, 1, 1)
        self.layout.addWidget(gbox3, 1, 0, 1, 1)
        self.layout.addWidget(gbox4, 1, 1, 1, 1)
        self.layout.addWidget(gbox5, 2, 0, 1, 1)
        self.layout.addWidget(gbox6, 2, 1, 1, 1)
        self.layout.addWidget(gbox7, 3, 0, 1, 2)
        self.layout.addWidget(gbox8, 4, 0, 1, 1)
        self.layout.addWidget(gbox9, 4, 1, 1, 1)
        self.layout.addWidget(gbox10, 5, 0, 1, 2)
        self.layout.addWidget(gbox11, 6, 0, 1, 2)

        # set layout
        self.setLayout(self.layout)

        return

    def updateSettings(self):
        '''
        Updates the values of the current subwindow with the values from the controls.
        '''
        if not self.mdi.currentSubWidget():
            return

        # distance
        distance = self.spin1.value()
        self.mdi.currentSubWidget().distance = distance

        # word count
        wordCount = self.spin2.value()
        self.mdi.currentSubWidget().wordCount = wordCount

        # regex
        pattern = self.edit1.text()
        if pattern:
            self.mdi.currentSubWidget().regex = pattern

        # tags
        tags = []
        for select in self.selects:

            if select.currentRow() != 0:
                tags.append((select.currentRow(), select.selectedItems()[0].text()))
            else:
                tags.append((select.currentRow(), ""))

        self.mdi.currentSubWidget().tags = tags

        # filter
        self.mdi.currentSubWidget().filter()

        return

    def reset(self):
        '''
        Resets the table of the active subwindow.
        '''
        self.resetControls()
        if self.mdi.currentSubWidget():
            self.mdi.currentSubWidget().resetTable()
        return

    def resetControls(self):
        '''
        Resets the controls to default values.
        '''
        self.edit1.setText(DEFAULT_REGEX)
        self.spin1.setValue(0)
        self.spin2.setValue(0)
        self.combo2.setCurrentIndex(0)
        for s in self.selects:
            s.setCurrentRow(0)
        return

    def initControls(self):
        '''
        Initialize controls with default values.
        Registers the triggers for the controls.
        '''

        # regex
        self.edit1.setText(DEFAULT_REGEX)

        # distance
        self.spin1.setValue(0)

        # word count
        self.spin2.setValue(0)

        # tags
        for s in self.selects:
            s.setCurrentRow(0)

        # statistics
        self.combo2.setCurrentIndex(0)

        # set trigger
        for s in self.selects:
            s.itemSelectionChanged.connect(self.updateSettings)

        self.button2.clicked.connect(self.showStatistics)
        self.button3.clicked.connect(self.reset)
        self.spin1.valueChanged.connect(self.updateSettings)
        self.spin2.valueChanged.connect(self.updateSettings)
        self.edit1.returnPressed.connect(self.updateSettings)
        return

    def showStatistics(self):
        '''
        Creates a statistic window and displays the selected statistic.
        '''
        dl = self.mdi.currentDataList()
        if dl:
            index = self.combo2.currentIndex()
            self.sw = MRE_StatsWindow(self.win, dl)
            if self.sw:
                if index == 1:
                    self.sw.distance_amount()
                elif index == 2:
                    self.sw.tag_amount()
                elif index == 3:
                    self.sw.tag_mediandistance()
                elif index == 4:
                    self.sw.tag_meandistance()
                else:
                    self.win.logger.log("Please select a statistic.", LOG_INFO)
        else:
            self.win.logger.log("No data found.", LOG_ERROR)
        return

    def getSelectedColumn(self):
        '''
        Returns the selected table column of the active subwidget.
        '''
        col = -1
        if self.mdi.currentSubWidget():
            col = self.mdi.currentSubWidget().currentColumn()
        return col

    def getSelectedRow(self):
        '''
        Returns the selected table row of the active subwidget.
        '''
        col = -1
        if self.mdi.currentSubWidget():
            col = self.mdi.currentSubWidget().currentRow()
        return col

    def updateControls(self):
        '''
        Updates all controls within the control widget with the values from the active subwidget.
        '''
        if self.mdi.currentSubWidget():

            # regex
            self.edit1.setText(self.mdi.currentSubWidget().regex)

            # distance
            self.spin1.setValue(self.mdi.currentSubWidget().distance)

            # word count
            self.spin2.setValue(self.mdi.currentSubWidget().wordCount)

            # tags
            tags = self.mdi.currentSubWidget().tags
            if tags:
                i = 0
                for s in self.selects:
                    s.setCurrentRow(tags[i][0])
                    i += 1

        return

    def disableControls(self, disabled: bool):
        '''
        Disables all controls within the control widget.
        '''
        self.resetControls()
        for s in self.selects:
            s.setDisabled(disabled)
        self.edit1.setDisabled(disabled)
        self.spin1.setDisabled(disabled)
        self.spin2.setDisabled(disabled)
        self.combo2.setDisabled(disabled)
        self.button2.setDisabled(disabled)
        self.button3.setDisabled(disabled)
        return
