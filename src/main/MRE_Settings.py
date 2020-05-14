'''
Imports
'''
from src.include.globals import *


class MRE_Settings(QSettings):
    '''
    Settings class
    Manages the application settings.
    '''

    def __init__(self, win):
        '''
        Constructor
        '''
        super().__init__()
        self.pid = self.getProjectSize()
        self.logScale = False
        self.win = win
        return

    def getProjectName(self, pid):
        '''
        Returns the name of the project with ID 'pid'.
        '''
        return self.value("projects/project" + str(pid) + "/name")

    def getProjectPath(self, pid):
        '''
        Returns the path to the project with ID 'pid'.
        '''
        return self.value("projects/project" + str(pid) + "/path")

    def existProject(self, name, path):
        '''
        Checks whether a project with name 'name'
        in path 'path' exists.
        '''
        projects = self.getProjects()
        for p in projects:
            if p[0] == name:
                if p[1] == path:
                    return True
        return False

    def setProjectSettings(self, name, path):
        '''
        Add project to settings using project 'name' and 'path'.
        '''
        if self.existProject(name, path):
            return

        self.beginWriteArray("projects")
        self.setArrayIndex(self.pid)
        self.setValue("name", name)
        self.setValue("path", path)
        self.endArray()
        self.pid += 1
        return

    def getSettingsFile(self):
        '''
        Returns the settings file.
        '''
        return self.fileName()

    def getProjects(self):
        '''
        Returns a list of all projects.
        Each project is represented as tuple (name, path).
        '''
        projects = []
        size = self.beginReadArray("projects")
        for i in range(0, size):
            self.setArrayIndex(i)
            name = self.value("name")
            path = self.value("path")
            project = (name, path)
            projects.append(project)
        self.endArray()
        return projects

    def getProjectSize(self):
        '''
        Returns number of projects.
        '''
        size = self.value("projects/size")
        if size:
            return int(size)
        return 0

    def clearSettings(self):
        '''
        Clears all settings.
        '''
        delete = QMessageBox.question(self.win, '', 'Warning: Deleting all settings deletes also all imported projects.\n'
                                                  'Are you sure you want to reset all the settings?',
                                      QMessageBox.Yes | QMessageBox.No)

        if delete == QMessageBox.Yes:
            self.clear()
            return True

        return False

    def setLogScale(self, scale: bool):
        '''
        Sets the log scale.
        '''
        self.logScale = scale
        return
