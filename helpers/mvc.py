from abc import ABC, abstractmethod
from functools import wraps

class SingleInheritance(type):
   """
   A metaclass for disallowing multiple inheritance.
   """
   @classmethod
   def __prepare__(metacls, name, bases, *kwds):
      if len(bases) <= 1:
         return dict()
      else:
         raise RuntimeError(f"{name} inherits from multiple classes but at least one of them only supports single inheritance")

def informs(f):
   """
   A decorator forcing the method to inform the observers.
   Should be used in a Model subclass.
   """
   @wraps(f)
   def wrapper(self, *args, **kwargs):
      result = f(self, *args, **kwargs)
      data = self.current_data()
      for view in self.observers:
         view.inform(data)
      return result
   return wrapper

class Model(metaclass=SingleInheritance): # TODO: why did I need it to be SingleInheritance?
   def __init__(self):
      self.observers = []
   def subscribe(self, view):
      print(f"subscribing {view.__class__.__name__} to the model")
      self.observers.append(view)
      try:
         data = self.current_data()
      except AttributeError:
         raise AttributeError("every Model subclass should have a class attribute _inform_about, which is a tuple of field names. Or it can be an instance attribute and a list of field names. Alternatively, you can override current_data")
      view.inform(data)
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
   def __init__(self):
      self._model = self._model_class()
   def model_subscribe(self, view):
      self._model.subscribe(view)
   @abstractmethod
   def dispatch_event(self, event):
      pass