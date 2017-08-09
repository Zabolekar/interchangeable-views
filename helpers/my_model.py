from .mvc import Model, informs

class MyModel(Model):
   def __init__(self):
      super().__init__()
      self.n = 0
   @informs
   def inc(self):
      self.n += 1