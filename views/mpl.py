from time import monotonic

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.widgets as wid

from ..base_classes import View

class MatplotlibView(View):
   def __init__(self, dispatch_event):
      print("initializing MatplotlibView")
      self.figure = plt.figure()
      self.ax = self.figure.add_subplot(111)
      self.ax.set_xlabel("Time")
      self.ax.set_ylabel("Value of n")
      self.timestamps = []
      self.series = []
      self.line, = self.ax.plot(np.array([]), "ko-")
      self.but = wid.Button(self.ax, "")
      self.but.on_clicked(lambda _: dispatch_event("increment"))
      plt.show(block=False)
      self.figure.canvas.mpl_connect("close_event", lambda _: dispatch_event(("unsubscribe", self)))
   def inform(self, model_data):
      n = model_data["n"]
      self.timestamps.append(monotonic())
      self.series.append(n)
      x, y = np.array(self.timestamps), np.array(self.series)
      self.line.set_data(x, y)
      self.ax.relim()
      self.ax.autoscale_view()
      self.figure.canvas.draw()
   def mainloop(self):
      plt.show()