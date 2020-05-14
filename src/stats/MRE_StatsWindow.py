'''
Imports
'''
from src.stats.MRE_PlotCanvas import *
from src.stats.MRE_Statistics import *


class MRE_StatsWindow(QWidget):
    '''
    StatsWindow class
    Creates a statistics window with a plot canvas.
    '''

    def __init__(self, win, dl):
        '''
        Constructor
        '''
        super().__init__()
        self.win = win
        self.stats = MRE_Statistics(self.win, dl)
        self.setFixedSize(800, 600)
        self.plot = MRE_PlotCanvas(self)
        return

    def distance_amount(self):
        '''
        Creates and displays the 'Distance Amount' plot.
        '''
        xdict = self.stats.getDistanceAmounts()
        if self.plot.create(xdict, "Amount per Distance", "Distance", "Amount"):
            self.show()
        else:
            self.win.logger.log("Failed to create plot", LOG_ERROR)
        return

    def tag_amount(self):
        '''
        Creates and displays the 'Tag Amount' plot.
        '''
        xdict = self.stats.getTagAmounts()
        if self.plot.create(xdict, "Amount per Tag", "Tag", "Amount"):
            self.show()
        else:
            self.win.logger.log("Failed to create plot", LOG_ERROR)
        return

    def tag_mediandistance(self):
        '''
        Creates and displays the 'Tag Median Distance' plot.
        '''
        xdict = self.stats.getTagMedianDistance()
        if self.plot.create(xdict, "Median Distance per Tag", "Tag", "Median Distance"):
            self.show()
        else:
            self.win.logger.log("Failed to create plot", LOG_ERROR)
        return

    def tag_meandistance(self):
        '''
        Creates and displays the 'Tag Mean Distance' plot.
        '''
        xdict = self.stats.getTagMeanDistance()
        if self.plot.create(xdict, "Average Distance per Tag", "Tag", "Average Distance"):
            self.show()
        else:
            self.win.logger.log("Failed to create plot", LOG_ERROR)
        return
