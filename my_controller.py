from .base_classes import Controller

class MyController(Controller):
   def dispatch_event(self, event):
      if event == "increment":
         self.model.inc()
      else:
         print(f"Warning: unknown event {event}")
