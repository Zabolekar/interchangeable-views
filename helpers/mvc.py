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
      for view in self.observers:
         view.inform(self)
      return result
   return wrapper

class Model(metaclass=SingleInheritance):
   def __init__(self):
      self.observers = []
   def subscribe(self, view):
      print(f"subscribing {view.__class__.__name__} to the model")
      self.observers.append(view)
      view.inform(self)

class View(ABC):
   @abstractmethod
   def inform(self, model):
      pass
   @abstractmethod
   def mainloop(self):
      pass

class Controller(metaclass=SingleInheritance):
   def __init__(self):
      self._model = self._model_class()
   def model_subscribe(self, view):
      self._model.subscribe(view)