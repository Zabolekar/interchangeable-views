from .helpers.mvc import Controller

class MyController(Controller):
   def dispatch_event(self, event):
      if event == "increment":
         self._model.inc()
      else:
         print(f"Warning: unknown event {event}")
