from .mvc import Controller
from .my_model import MyModel

class MyController(Controller):
   _model_class = MyModel
   def push_button(self):
      self._model.inc()