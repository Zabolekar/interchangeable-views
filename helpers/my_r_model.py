from rpy2.robjects import r
from .mvc import Model, informs

R_CODE = """
n <- 0
inc <- function() {
   print("Hello from R")
   n <<- n+1
}
"""

class MyRModel(Model):
   _inform_about = ("n",)
   def __init__(self):
      super().__init__()
      r(R_CODE)

   @property
   def n(self):
      return int(r.n[0])

   @informs
   def inc(self):
      r.inc()
