'''
Imports
'''
from src.include.globals import *

'''
Constants
'''
Y_TICKS = 5
PRECISION = 1


class MRE_PlotCanvas(FigureCanvas):
    '''
    PlotCanvas class
    Creates a plot canvas.
    '''

    def __init__(self, parent=None, width=8, height=6, dpi=100):
        '''
        Constructor
        '''
        self.parent = parent

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.subplots_adjust(bottom=0.2)

        FigureCanvas.__init__(self, self.fig)

        self.setParent(self.parent)

        self.axes = None

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        return

    def create(self, xdict={}, title="", xlabel="", ylabel=""):
        '''
        Creates a plot.
        '''

        # x values
        xvals = list(xdict.keys())

        # y values
        yvals = list(xdict.values())

        # check
        if len(xvals) == 0 or len(yvals) == 0:
            return False

        # y max value
        ymax = max(yvals)

        # axe ticks / values
        ymeans = tuple(self.computeMeans(yvals))
        xnum = numpy.arange(len(ymeans)).tolist()

        self.setAxes(ymeans, xnum)
        self.setTicks(xnum)

        ynum = self.computeTickNumber(ymax, Y_TICKS, PRECISION)

        # axe labels
        xtlabels = xvals
        ytlabels = numpy.arange(0, ymax+ynum, ynum).tolist()

        self.setAxesLabels(xlabel, ylabel)

        # title
        self.setTitle(title)

        # fix ytlabels
        ytlabels2 = []
        for label in ytlabels:
            ytlabels2.append(round(label, PRECISION))

        # tick labels
        self.setTickLabels(xtlabels, ytlabels2)

        return True

    def setAxes(self, means, num):
        '''
        Sets the axes of the plot.
        '''

        # set axes
        self.axes = self.fig.add_subplot(111, label=randomString())

        # number of bars, mean values, width, color
        p1 = self.axes.bar(num, means, 0.5, color='#5500ff')

        # log scale
        if self.parent.win.settings.logScale:
            self.axes.set_yscale('log')
        else:
            self.axes.set_yscale('linear')

        return

    def setTitle(self, title: str):
        '''
        Sets the title of the plot.
        '''
        self.axes.set_title(title)
        return

    def setTickLabels(self, xlabels: list, ylabels: list):
        '''
        Sets the X/Y-axes tick labels.
        '''
        self.axes.set_xticklabels(xlabels, rotation=45)
        self.axes.set_yticklabels(ylabels)
        return

    def setAxesLabels(self, xlabel="", ylabel=""):
        '''
        Sets the X/Y labels.
        '''
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        return

    def setLegend(self):
        '''
        Sets the plot legend.
        '''
        return

    def setTicks(self, num: int):
        '''
        Sets the X ticks.
        '''
        self.axes.set_xticks(num)
        return

    def computeMeans(self, values: list):
        '''
        Returns means from 'values'.
        '''
        means = []
        for v in values:
            means.append(v / 2)
        return means

    def computeTickNumber(self, maxt: int, scale: int, precision=0):
        '''
        Returns the tick frequency on the X-axes based on
        - maxt: maximum number of ticks
        - scale: the maximum scale on the X-axes
        - precision: float precision of tick frequency
        '''
        t = (maxt / scale)
        t = round(t, precision)
        if t == 0:
            t = pow(10, -precision)
        return t
