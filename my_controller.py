from .base_classes import Controller

class MyController(Controller):
   def dispatch_event(self, event):
      if event == "increment":
         self.model.inc()
      elif len(event) == 2 and event[0] == "unsubscribe":
         self.unsubscribe(event[1])
      else:
         print(f"Warning: unknown event {event}")
