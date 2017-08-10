import colorama as cr
from ..helpers.mvc import View

def bright(s):
   return cr.Style.BRIGHT + s + cr.Style.RESET_ALL

def bright_green(s):
   return cr.Fore.GREEN + cr.Style.BRIGHT + s + cr.Style.RESET_ALL

def red(s):
   return cr.Fore.RED + s + cr.Style.RESET_ALL

class ConsoleView(View):
   def __init__(self, dispatch_event):
      cr.init()
      print(bright("initializing ConsoleView"))
      self._n = None
      self.dispatch_event = dispatch_event
      print(self)
   def __repr__(self):
      return bright_green(f"n = {self._n}")
   def inform(self, model_data):
      self._n = model_data["n"]
      print(self)
   def mainloop(self):
      print(bright("Use 'i' to increment the counter, 'q' to quit:"))
      while True:
         try:
            command = input("counter> ")
         except (KeyboardInterrupt, EOFError):
            break
         if command == "i":
            self.dispatch_event("increment")
         elif command == "q":
            break
         elif command == "":
            continue
         else:
            print(red("Unknown command"))
