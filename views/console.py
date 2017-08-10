from ..helpers.mvc import View

import colorama as cr

class ConsoleView(View):
   def __init__(self, command):
      cr.init()
      print(cr.Style.BRIGHT + "initializing ConsoleView" + cr.Style.RESET_ALL)
      self._n = None
      self.command = command
      print(self)
   def __repr__(self):
      return cr.Fore.GREEN + cr.Style.BRIGHT + f"n = {self._n}" + cr.Style.RESET_ALL
   def inform(self, model):
      self._n = model.n
      print(self)
   def mainloop(self):
      print(cr.Style.BRIGHT + "Use 'i' to increment the counter, 'q' to quit:" + cr.Style.RESET_ALL)
      while True:
         try:
            command = input("counter> ")
         except (KeyboardInterrupt, EOFError):
            break
         if command == "i":
            self.command()
         elif command == "q":
            break
         elif command == "":
            continue
         else:
            print(cr.Fore.RED + "Unknown command" + cr.Style.RESET_ALL)