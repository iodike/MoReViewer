'''
Imports
'''
from src.main.MRE_Settings import *
from src.handler.MRE_ActionHandler import *
from src.start.MRE_StartWidget import *
from src.controller.MRE_MainWidget import *
from src.handler.MRE_Config import *


class MRE_MainWindow(QMainWindow):
    '''
    MainWindow class
    Creates the main window.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()

        # logger
        self.logger = MRE_LogArea(self)

        # settings
        self.settings = MRE_Settings(self)

        # action handler
        self.ah = MRE_ActionHandler(self)

        # main widget
        self.mw = None

        # set central widget
        self.start = MRE_StartWidget(self)
        self.setCentralWidget(self.start)

        # small window
        self.setFixedSize(800, 500)

        # global actions
        self.save_action = QAction('Save As...', self)

        # init bars
        self.setupStatusbar()
        self.setupMenubar()

        return

    def reset(self):
        '''
        Closes the main widget.
        '''
        if self.mw:
            if self.mw.close():
                return True
        else:
            return True
        return False

    def setupStatusbar(self):
        '''
        Create the status bar.
        '''
        self.statusBar().showMessage('Ready')
        return

    def setupToolbar(self):
        '''
        Create the tool bar.
        '''
        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("bug.png"), "Bug", self)
        button_action.setStatusTip("Check for bugs")
        button_action.triggered.connect(self.onToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("fix3.png"), "Fix", self)
        button_action2.setStatusTip("Fix it")
        button_action2.triggered.connect(self.onToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        return

    def setupMenubar(self):
        '''
        Create the menu bar.
        '''
        menubar = self.menuBar()

        # Top Menus
        fileMenu = menubar.addMenu('File')
        editMenu = menubar.addMenu('Edit')
        filterMenu = menubar.addMenu('Filter')
        modelMenu = menubar.addMenu('Model')
        logMenu = menubar.addMenu('Log')
        statsMenu = menubar.addMenu('Stats')

        # Sub Menus
        settingsMenu = fileMenu.addMenu('Project Settings')

        # Top Actions

        # new
        new_action = QAction('New Project...', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.ah.newProject)

        # open
        open_action = QAction('Open Project...', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.ah.openProject)

        # save
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.triggered.connect(self.ah.saveProject)
        self.save_action.setDisabled(True)

        # undo
        undo_action = QAction('Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.triggered.connect(self.ah.undoAction)

        # redo
        redo_action = QAction('Redo', self)
        redo_action.setShortcut('Ctrl+Y')
        redo_action.triggered.connect(self.ah.redoAction)

        # add
        add_action = QAction('Add...', self)
        add_action.setShortcut('Ctrl+A')
        add_action.triggered.connect(self.ah.addDocument)

        # clear settings
        cs_action = QAction('Clear Settings', self)
        cs_action.setShortcut('Ctrl+C')
        cs_action.triggered.connect(self.settings.clearSettings)

        # clear log
        cl_action = QAction('Clear Log', self)
        cl_action.setShortcut('Alt+C')
        cl_action.triggered.connect(self.logger.clearLog)

        # filter notes
        fino_action = QAction('Filter Notes', self)

        # Add Actions (File)
        fileMenu.addAction(new_action)
        fileMenu.addAction(open_action)
        fileMenu.addAction(self.save_action)
        fileMenu.addSeparator()
        fileMenu.addMenu(settingsMenu)

        settingsMenu.addAction(cs_action)

        # Add Actions (Edit)
        editMenu.addAction(undo_action)
        editMenu.addAction(redo_action)

        # Add Actions (Filter)
        filterMenu.addAction(fino_action)

        # Add Actions (Model)
        modelMenu.addAction(add_action)

        # Add Actions (Log)
        logMenu.addAction(cl_action)
        logMenu.addSeparator()
        logLevelMenu = logMenu.addMenu('Log Level')

        # log level menu
        level_group = QActionGroup(logLevelMenu)
        log_levels = list(LOG_LEVELS.keys())
        for level in log_levels:
            action = QAction(level, logLevelMenu, checkable=True, checked=(level == log_levels[self.logger.level]))
            logLevelMenu.addAction(action)
            level_group.addAction(action)
        level_group.setExclusive(True)
        level_group.triggered.connect(self.onLogLevelChanged)

        # Add Actions (Stats)
        scaleMenu = statsMenu.addMenu('Set Scale')

        # scale menu
        scale_group = QActionGroup(scaleMenu)
        for scale in PLOT_SCALES:
            action = QAction(scale, scaleMenu, checkable=True, checked=(scale == PLOT_SCALES[0]))
            scaleMenu.addAction(action)
            scale_group.addAction(action)
        scale_group.setExclusive(True)
        scale_group.triggered.connect(self.onPlotScaleChanged)

        return

    def onLogLevelChanged(self, action):
        '''
        Trigger when log level changed.
        Set new log level.
        '''
        level = LOG_LEVELS[action.text()]
        self.logger.setLogLevel(level)
        self.logger.log("Log level set to '" + action.text() + "'", level)
        return

    def onPlotScaleChanged(self, action):
        '''
        Trigger when plot scale changed.
        Set new plot scale.
        '''
        if action.text() == LOGARITHMIC:
            self.settings.setLogScale(True)
        else:
            self.settings.setLogScale(False)
        self.logger.log("Plot scale set to '" + action.text() + "'", LOG_INFO)
        return
