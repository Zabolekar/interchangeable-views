from .mvc import Controller
from .my_model import MyModel

class MyController(Controller):
   _model_class = MyModel
   def dispatch_event(self, event):
      if event == "increment":
         self._model.inc()
      else:
         print(f"Warning: unknown event {event}")