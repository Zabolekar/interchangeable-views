from .mvc import Controller
from .my_r_model import MyRModel

class MyRController(Controller):
   _model_class = MyRModel
   def dispatch_event(self, event):
      if event == "increment":
         self._model.inc()
      else:
         print(f"Warning: unknown event {event}")
