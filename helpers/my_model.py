from .mvc import Model, informs

class MyModel(Model):
   _inform_about = ("n",)
   def __init__(self):
      super().__init__()
      self.n = 0
   @informs
   def inc(self):
      self.n += 1
