'''
Imports
'''
from src.include.globals import *


class MRE_ImportWizardPage(QWizardPage):
    '''
    ImportWizardPage class
    '''

    def __init__(self, mw, ph):
        '''
        Constructor
        Creates a wizard page for importing.
        '''
        super().__init__()

        # title
        self.setTitle("Import")
        self.setSubTitle("")

        # labels
        self.titleLabel = QLabel("Project Title:")
        self.dataLabel = QLabel("Choose model:")
        self.configLabel = QLabel("Choose configuration:")
        self.langLabel = QLabel("Choose language:")

        #
        # controls
        #

        self.titleLine = QLineEdit()
        self.titleLine.setStyleSheet("background-color: #fff; color: #666;")

        self.dataLine = QLineEdit()
        self.dataLine.setStyleSheet("background-color: #fff; color: #666;")

        self.dataButton = QPushButton("...")

        self.configLine = QLineEdit()
        self.configLine.setStyleSheet("background-color: #fff; color: #666;")

        self.configButton = QPushButton("...")

        self.langSelect = QComboBox()

        self.langButton = QPushButton("Auto-Detect")

        # language
        self.langSelect.addItem("Select Language")
        for lang in languages:
            self.langSelect.addItem(lang[1])

        # field
        self.registerField("projectTitle", self.titleLine)
        self.registerField("dataFile", self.dataLine)
        self.registerField("configFile", self.configLine)

        # layout
        self.gridLayout = QGridLayout()
        # title
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 8)
        self.gridLayout.addWidget(self.titleLine, 1, 0, 1, 8)
        # data
        self.gridLayout.addWidget(self.dataLabel, 2, 0, 1, 8)
        self.gridLayout.addWidget(self.dataLine, 3, 0, 1, 7)
        self.gridLayout.addWidget(self.dataButton, 3, 7, 1, 1)
        # config
        self.gridLayout.addWidget(self.configLabel, 4, 0, 1, 8)
        self.gridLayout.addWidget(self.configLine, 5, 0, 1, 7)
        self.gridLayout.addWidget(self.configButton, 5, 7, 1, 1)
        # lang
        self.gridLayout.addWidget(self.langLabel, 6, 0, 1, 8)
        self.gridLayout.addWidget(self.langSelect, 7, 0, 1, 6)
        self.gridLayout.addWidget(self.langButton, 7, 6, 1, 2)

        self.setLayout(self.gridLayout)

        #
        # trigger
        #

        # import
        self.dataButton.clicked.connect(self.importData)
        self.configButton.clicked.connect(self.importConfig)

        # complete
        self.titleLine.textChanged.connect(self.completeChanged)
        self.dataLine.textChanged.connect(self.completeChanged)
        self.configLine.textChanged.connect(self.completeChanged)
        self.langSelect.currentIndexChanged.connect(self.completeChanged)

        # lang
        self.langButton.clicked.connect(self.detectLanguage)

        return

    def initializePage(self):
        '''
        Initialises the wizard page. (When clicking 'Next')
        '''
        # self.dataLine.setText("/Users/ioannisdikeoulias/Documents/College/Semester_13/SPNN/Project/morpho/gui/examples/pred_epoch_43.txt")
        # self.configLine.setText("/Users/ioannisdikeoulias/Documents/College/Semester_13/SPNN/Project/morpho/gui/examples/config2.json")
        # self.detectLanguage()
        return

    def cleanupPage(self):
        '''
        Cleans up the wizard page. (When clicking 'Back')
        '''
        return

    def isComplete(self):
        '''
        Checks whether the wizard step is completed.
        '''
        c1 = QFile.exists(self.field("dataFile"))
        c2 = QFile.exists(self.field("configFile"))
        c3 = (self.langSelect.currentIndex() != 0)
        c4 = (self.titleLine.text() != "")
        return c1 and c2 and c3 and c4

    def importData(self):
        '''
        Imports the data from the data file.
        '''
        fd = QFileDialog()
        fname = fd.getOpenFileName(self, 'Choose model', '~', 'Data files (*.tsv *.txt)')

        if fname[0]:
            self.setField("dataFile", fname[0])

        return

    def importConfig(self):
        '''
        Imports the config from the config file.
        '''
        fd = QFileDialog()
        fname = fd.getOpenFileName(self, 'Choose config', '~', 'Config files (*.json)')

        if fname[0]:
            self.setField("configFile", fname[0])

        return

    ##
    def detectLanguage(self):
        '''
        Detects the language of the data file.
        '''
        words = []
        lang = ""
        seq = ""

        dataFile = self.wizard().field('dataFile')

        if dataFile:
            samples = readFileAsList(dataFile, 5)

            for sample in samples:
                words.append(sample[0])

            for word in words:
                seq += word + " "

            if seq:
                langcode = detect(seq)
                lang, index = getLanguage(langcode)
                self.langSelect.setCurrentIndex(index)

        else:
            showMessage("Please specify a model.")

        return lang
