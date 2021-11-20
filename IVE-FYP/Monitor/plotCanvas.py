from PyQt5.QtWidgets import QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import QTimer


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=1, height=1, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def init_plot(self, title, unit, time):
        self.title = title
        self.unit = unit
        self.time = time
        self.axes.set_title(self.title)
        self.axes.set_ylabel(self.unit)
        self.axes.set_xlabel(self.time)

    def update_figure(self, x, y):
        self.axes.cla()
        self.axes.set_title(self.title)
        self.axes.set_ylabel(self.unit)
        self.axes.set_xlabel(self.time)
        self.axes.plot(x, y)
        self.draw()

    def outputImage(self, title):
        self.fig.savefig(title + '.png')
