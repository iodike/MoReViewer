'''
Imports
'''
from src.include.globals import *


class MRE_RecentWidget(QListWidget):
    '''
    RecentWidget class
    Creates a widget that displays recent projects.
    '''

    def __init__(self, win):
        '''
        Constructor
        '''
        super().__init__()
        self.win = win
        self.setStyleSheet("QListWidget::item{line-height: 1.5}")
        self.projects = self.win.settings.getProjects()
        self.itemDoubleClicked.connect(self.onDoubleClick)
        self.initUI()
        return

    def initUI(self):
        '''
        Adds all projects to the widget.
        '''
        self.clear()
        for i in range(0, len(self.projects)):
            self.addProject(self.projects[i][0], self.projects[i][1])
        return

    def addProject(self, name, path):
        '''
        Add the project with name 'name' and path 'path' to the widget.
        '''
        if name and path:
            item = QListWidgetItem(" " + name + "\n" + " " + path)
            item.setFont(QFont("Helvetica", 14))
            item.setSizeHint(QSize(50, 50))
            self.addItem(item)
        return

    def onDoubleClick(self, item):
        '''
        Triggers when project is double clicked.
        Opens the clicked project.
        '''
        index = self.row(item)
        projectFile = self.projects[index][1] + "/" + self.projects[index][0] + PRO_EXT
        configFile = self.projects[index][1] + CFG_FILE
        self.win.ah.ph.openProject(projectFile, configFile)
        return
