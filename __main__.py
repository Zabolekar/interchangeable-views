from sys import argv

from helpers.my_controller import MyController
from views.console import ConsoleView

if __name__ == '__main__':
   c = MyController()

   try:
      view = argv[1]
   except IndexError:
      print("You haven't selected any view")
      print("Default is console. Others are: curses, tk, qt, kivy, flask")
      view = "console"
      
   if view == "console":
      MainView = ConsoleView
   elif view == "curses":
      from views.curses import CursesView as MainView
   elif view == "tk":
      from views.tk import TkView as MainView
   elif view == "qt":
      from views.qt import QtView as MainView
   elif view == "kivy":
      from views.kv import KivyView as MainView
   elif view == "flask":
      from views.fl.fl import FlaskView as MainView
   else:
      print(f"Unknown view: {view}")
      quit()
   
   if view not in ["console", "curses"]:
      c.model_subscribe(ConsoleView(c.push_button))
   
   v = MainView(command=c.push_button)
   c.model_subscribe(v)
   v.mainloop()