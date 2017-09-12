import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.widgets as wid

from ..helpers.mvc import View

class MatplotlibView(View):
   def __init__(self, dispatch_event):
      print("initializing MatplotlibView")
      self.figure = plt.figure()
      self.ax = self.figure.add_subplot(111)
      self.series = []
      self.line, = self.ax.plot(np.array([]), "ko-")
      self.but = wid.Button(self.ax, "")
      self.but.on_clicked(lambda _: dispatch_event("increment"))
      plt.show(block=False)
   def inform(self, model_data):
      n = model_data["n"]
      self.series.append(n)
      x, y = np.arange(len(self.series)), np.array(self.series)
      self.line.set_data(x, y)
      self.ax.relim()
      self.ax.autoscale_view()
      self.figure.canvas.draw()
   def mainloop(self):
      plt.show()