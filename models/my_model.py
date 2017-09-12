from ..base_classes import Model, informs

class MyModel(Model):
   _inform_about = ("n",)
   def __init__(self):
      self.n = 0
   @informs
   def inc(self):
      self.n += 1
