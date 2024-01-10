#!/usr/bin/python3
'''

This script plots bars for raw data captured by the linksys router iterativetly and massively and compared them with the X scatterplot of groundtrugh logfile collected during the execution

'''
import sys
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
import pandas as pd
import time
from datetime import datetime as dt

class ScrollableWindow(QtWidgets.QMainWindow):
    def __init__(self, fig, ax, step=0.1):
        plt.close("all")
        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        QtWidgets.QMainWindow.__init__(self)
        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QtWidgets.QVBoxLayout())
        self.widget.layout().setContentsMargins(0,0,0,0)
        self.widget.layout().setSpacing(0)

        self.fig = fig
        self.ax = ax
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.scroll = QtWidgets.QScrollBar(QtCore.Qt.Horizontal)
        self.step = step
        self.setupSlider()
        self.nav = NavigationToolbar(self.canvas, self.widget)
        self.widget.layout().addWidget(self.nav)
        self.widget.layout().addWidget(self.canvas)
        self.widget.layout().addWidget(self.scroll)

        self.canvas.draw()
        self.show()
        self.app.exec_()

    def setupSlider(self):
        self.lims = np.array(self.ax.get_xlim())
        self.scroll.setPageStep(self.step*100)
        self.scroll.actionTriggered.connect(self.update)
        self.update()

    def update(self, evt=None):
        r = self.scroll.value()/((1+self.step)*100)
        l1 = self.lims[0]+r*np.diff(self.lims)
        l2 = l1 +  np.diff(self.lims)*self.step
        self.ax.set_xlim(l1,l2)
        #print(self.scroll.value(), l1,l2)
        self.fig.canvas.draw_idle()

# capdata (captured data)
capdata = pd.read_csv("/Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksys_analysis/trace/capture00500ms_seg0104.csv")
capdata = capdata.query("Dev == '64:F2:FB:DF:FB:E1'")
capdata["TS"] = capdata["TS"].apply(lambda a: round(np.compat.long(a),1))
yts = capdata["TS"]
ydt = capdata["TS"].apply(lambda a: dt.fromtimestamp(a).strftime('%Y-%m-%d %H:%M:%S'))

# TIME SHIFT 2h
startDate=dt(2022,9,20,17,19,0)
sdts=round(float(startDate.timestamp()),1)
endDate=dt(2022,9,20,19,19,0)
edts=round(float(endDate.timestamp()),1)
yticksts = np.arange(sdts,edts,1*60)
yticksdt = list(map(lambda elem: dt.fromtimestamp(elem).strftime('%Y-%m-%d %H:%M:%S') , yticksts))

# potrei creare una query che filtra i dati in base al campo TS
pltcapdata = capdata.query("TS > {} and TS < {}".format(sdts,edts))

# create a figure 
fig, ax = plt.subplots()
ax.bar(pltcapdata["TS"],pltcapdata["SumTcpDLpckSz"],align='center',width=2,color='g')
#ax.bar(yts[0:200],data["SumTcpDLpckSz"][0:200],align='center',width=2)
ax.grid(True)
ax.set_title("Network Traffic smart device")
ax.set_xlabel("Timestamp [s]")
ax.set_ylabel("Packet Size [B]")
ax.set_xticks(yticksts)
#ax.set_xticks(yts[0:200])
#ax.set_xticks(ax.get_xticks())
ax.set_xticklabels(yticksdt,rotation=90,size=8)
#ax.set_xticklabels(ydt[0:200],rotation=90,size=8)
#ts = list(map(lambda elem: dt.fromtimestamp(elem).strftime('%Y-%m-%d %H:%M:%S') , ax.get_xticks()))
#ax.set_xticklabels(ts,rotation=90,size=8)
fig.tight_layout()

# grtdata (groundtruth data)
grtdata = pd.read_csv("/Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksys_analysis/test_di_scrittura.csv")
grtdata = grtdata.query('APP == "EZVIZ" and DEVICE == "Smart Bulb"')
rests = grtdata["TIMESTAMP"].apply(lambda x: time.mktime(dt.strptime(x, "%Y-%m-%d %H:%M:%S.%f").timetuple()))
pltgrtdata = grtdata
pltgrtdata["TIMESTAMP"] = pltgrtdata["TIMESTAMP"].apply(lambda x: time.mktime(dt.strptime(x, "%Y-%m-%d %H:%M:%S.%f").timetuple()))
pltgrtdata = grtdata.query("TIMESTAMP > {} and TIMESTAMP < {}".format(sdts,edts))

ax.stem(pltgrtdata["TIMESTAMP"], np.multiply(np.ones(len(pltgrtdata["TIMESTAMP"])), 100),linefmt="r--",markerfmt="r.",basefmt="r.")
#ax.scatter(pltgrtdata["TIMESTAMP"], np.zeros(len(pltgrtdata["TIMESTAMP"])), marker='o', color='r', linewidths=0.5)
#ax.scatter(rests, np.zeros(len(rests)), marker='X', color='r', linewidths=0.5)

# pass the figure to the custom window
a = ScrollableWindow(fig,ax)
