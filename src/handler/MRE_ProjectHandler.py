'''
Imports
'''
from src.wizard.MRE_ImportWizard import *
from src.controller.MRE_MainWidget import *


class MRE_ProjectHandler:
    '''
    ProjectHandler class
    Creates a handler for projects.
    '''

    def __init__(self, win):
        '''
        Constructor
        '''
        self.win = win
        self.wiz = None
        return

    def createProjectFolder(self):
        '''
        Create the application project folder.
        '''
        path = getProjectFolder()
        try:
            os.mkdir(path)

        except OSError:
            print("Creation of directory %s failed (might already exist)" % path)

        else:
            print("Successfully created directory %s " % path)

        return

    def startWizard(self):
        '''
        Start the import wizard.
        '''
        self.createProjectFolder()
        self.wiz = MRE_ImportWizard(self.win, self)
        return

    def openProject(self, datafile, configfile):
        '''
        Open an existing project.
        '''
        if not datafile or not configfile:
            showMessage("Project files missing.")
            return

        elif getFileExtension(datafile) != PRO_EXT:
            showMessage("Wrong project format.", "Expected " + PRO_EXT + " file but got " + getFileExtension(datafile) +
                        " file.")
            return

        else:
            self.win.mw = MRE_MainWidget(self.win)

            # create data list
            dl = MRE_DataList(self.win)
            dl.init(datafile, configfile, True)

            # add sub window
            self.win.mw.addSubWindow(dl, "")

            # show main widget
            self.win.hide()
            self.win.mw.showFullScreen()

            # enable saving
            self.win.save_action.setDisabled(False)

            # add project to settings
            self.win.settings.setProjectSettings(getNameFromFile(datafile), getPathFromFile(datafile))

        return

    def saveProject(self):
        '''
        Saves the current project.
        '''
        # data file
        dfile, fmt = QFileDialog.getSaveFileName(self.win.mw, 'Save Project', getProjectFolder(), "MoRe Project(*.mrp)",
                                                options=QFileDialog.DontUseNativeDialog)

        if dfile:
            # rename data file
            rdfile = renameDataFile(dfile)

            # data list
            dlist = self.win.mw.mdi.currentDataList()

            # get output
            out = dlist.toString()

            # save data
            dpath = writeFile(rdfile, out)

            # config file
            cfile = dlist.ih.config.getFile()

            # rename config
            rcfile = dpath + CFG_FILE

            # save config
            copy(cfile, rcfile)

            # add project to settings
            self.win.settings.setProjectSettings(getNameFromFile(rdfile), getPathFromFile(rdfile))

        return

    def deleteProject(self, projectID):
        '''
        Deletes a project with the ID 'projectID'.
        '''
        return

    def createNewProject(self):
        '''
        Creates a new project.
        '''
        # get data from wizard
        dl = self.wiz.getDataList()

        # change function to initialise project from given files
        # dl = MRE_DataList(self.win)
        # dataFile = self.wiz.field("dataFile")
        # configFile = self.wiz.field("configFile")
        # dl.init(dataFile, configFile, False)

        # create widget
        if dl:
            # add sub window
            self.win.mw = MRE_MainWidget(self.win)
            self.win.mw.addSubWindow(dl, "")

            # show main widget
            self.win.hide()
            self.win.mw.showFullScreen()

            # enable saving
            self.win.save_action.setDisabled(False)

        else:
            showMessage("Failed to create new project!")

        return
