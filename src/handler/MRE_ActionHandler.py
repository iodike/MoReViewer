'''
Imports
'''
from src.handler.MRE_ProjectHandler import *


class MRE_ActionHandler:
    '''
    ActionHandler class
    Creates a handler for menu actions.
    '''

    def __init__(self, win):
        '''
        Constructor
        '''
        self.win = win
        self.ph = MRE_ProjectHandler(self.win)
        return

    def newProject(self):
        '''
        Create a new project.
        '''
        if self.win.reset():
            self.ph.startWizard()
        return

    def openProject(self):
        '''
        Open an existing project.
        '''
        if self.win.reset():

            dfile, fmt = QFileDialog.getOpenFileName(self.win, 'Open Project', getProjectFolder(),
                                                     'MoRe Projects (*.mrp)')

            pfolder = getPathFromFile(dfile)

            cfile = pfolder + CFG_FILE

            self.ph.openProject(dfile, cfile)

        return

    def saveProject(self):
        '''
        Save the current project.
        '''
        self.ph.saveProject()
        return

    def undoAction(self):
        '''
        Undo recent operation.
        '''
        showMessage("This action is not available!")
        return

    def redoAction(self):
        '''
        Redo recent operation.
        '''
        showMessage("This action is not available!")
        return

    def addDocument(self):
        '''
        Add document as additional window to the MDI area.
        '''
        if not self.win.mw:
            showMessage("Before adding documents you must create a project.")
            return

        dataFile, fmt = QFileDialog.getOpenFileName(self.win.mw, 'Save Project', getProjectFolder(),
                                                    'Data files (*.tsv *.txt)', options=QFileDialog.DontUseNativeDialog)

        dl = MRE_DataList(self.win)

        configFile = self.win.mw.mdi.currentDataList().ih.config.file

        if dataFile and configFile:
            dl.init(dataFile, configFile, False)
        else:
            self.win.logger.log("No data or config file found.", LOG_ERROR)
            return

        if not dl.isEmpty():
            self.win.mw.addSubWindow(dl, "")
        else:
            self.win.logger.log("Your imported file is empty.", LOG_ERROR)
            return

        return
