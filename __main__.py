from sys import argv
from threading import Thread

from .helpers.my_controller import MyController
from .views.console import ConsoleView

if __name__ == '__main__':
   c = MyController()

   try:
      view = argv[1]
   except IndexError:
      print("You haven't selected any view")
      print("Default is console. Others are: tk, kivy, tk-kivy, curses, qt, flask")
      view = "console"
      
   if view == "console":
      MainView = ConsoleView
   elif view == "curses":
      from .views.curses import CursesView as MainView
   elif view == "tk":
      from .views.tk import TkView as MainView
   elif view == "qt":
      from .views.qt import QtView as MainView
   elif view == "kivy":
      from .views.kv import KivyView as MainView
   elif view == "flask":
      from .views.fl.fl import FlaskView as MainView
   elif view == "tk-kivy":
      from .views.tk import TkView as MainView
      def kv():
         from .views.kv import KivyView as View
         v = View(command=c.push_button)
         c.model_subscribe(v)
         v.mainloop()
      Thread(target=kv, args=()).start()
      # TODO: if Flask is being launched in a separate thread it still somehow manages to block the program
      # but most importantly, A BUG: the number on the website does not get updated until we push the button on the website
      # TODO: for reasons I don't quite understand, Qt doesn't work well when launched in a separate thread
      # but it also doesn't update without being clicked, which I also don't understand
   else:
      print(f"Unknown view: {view}")
      quit()
   
   if view not in ["console", "curses"]:
      c.model_subscribe(ConsoleView(c.push_button))
   
   v = MainView(command=c.push_button)
   c.model_subscribe(v)
   v.mainloop()