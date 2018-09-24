from abc import ABC, abstractmethod
from functools import wraps

class SingleInheritance(type):
   """
   A metaclass for disallowing multiple inheritance.
   """
   @classmethod
   def __prepare__(mcs, name, bases, *kwds):
      if len(bases) <= 1:
         return dict()
      else:
         raise RuntimeError(f"{name} inherits from multiple classes, "
                            "but at least one of them only supports single inheritance")

def informs(f):
   """
   A decorator forcing the method to inform the controller.
   Should be used in a Model subclass.
   """
   @wraps(f)
   def wrapper(self, *args, **kwargs):
      result = f(self, *args, **kwargs)
      data = self.current_data()
      self.controller.inform(data)
      return result
   return wrapper

class Model(metaclass=SingleInheritance): # TODO: why did I need it to be SingleInheritance?
   """
   0. Your model should inherit from Model.
   1. Your model should have a class attribute _inform_about, which is a sequence (usually a tuple) of field names.
   If you want to mutate it, it can be an instance attribute and a list of field names.
   Alternatively, you can override current_data, because it is the only method that uses _inform_about.
   2. Decorate with @informs any public method that changes your model
   """
   def current_data(self):
      return {name: getattr(self, name) for name in self._inform_about}

class View(ABC):
   @abstractmethod
   def inform(self, model_data):
      pass
   @abstractmethod
   def mainloop(self):
      pass

class Controller(ABC):
   def __init__(self, model_class):
      self.model = model_class()
      self.model.controller = self
      self.views = []
   def inform(self, data):
      for view in self.views:
         view.inform(data)
   def subscribe(self, view):
      print(f"subscribing {view.__class__.__name__} to the model")
      self.views.append(view)
      data = self.model.current_data()
      view.inform(data)
   def unsubscribe(self, view):
      for i, v in enumerate(self.views):
         if v is view:
            self.views.pop(i)
   @abstractmethod
   def dispatch_event(self, event):
      pass
