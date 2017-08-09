from helpers.mvc import View

import curses

class CursesView(View):
   def __init__(self, command):
      self.command = command
      self.win = None
      self.screen = None
   def inform(self, model):
      if self.win:
         label = f"n = {model.n}"
         self.win.addstr(1, 16-len(label)//2, label)
      if self.screen:
         arr = [' ']*5
         arr[(-model.n+1)%5] = '<'
         arr[(-model.n)%5] = '~'
         arr[(-model.n-1)%5] = '>'
         pattern = "".join(arr)
         self.screen.addstr(0, 0, pattern*(self.width//len(pattern)))
   def mainloop(self):
      curses.wrapper(self)
   def __call__(self, screen):
      screen.clear()
      curses.curs_set(False)      
      height, width = screen.getmaxyx()
      
      self.screen = screen
      self.width = width
      
      screen.addstr(height//2-1, width//2-16, "Press i to increment, q to quit:")
      screen.refresh()

      self.win = curses.newwin(3, 32, height//2, width//2-16)
      self.win.box()
      # we need to create a label, but we can't call inform directly here, so what can we do?
      self.win.addstr(1, 16-2, "n = 0")
      # TODO: it is ugly, what if we change the initial n value but forget to change it here?
      
      while True:
         self.win.refresh()
         event = screen.getch()
         if event == ord('q'):
            break
         elif event == ord('i'):
            self.command()