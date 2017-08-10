from sys import argv
from threading import Thread

from .helpers.my_controller import MyController
from .views.console import ConsoleView

if __name__ == '__main__':
   controller = MyController()

   try:
      view_name = argv[1]
   except IndexError:
      print("You haven't selected any view")
      print("Default is console. Others are: tk, kivy, tk-kivy, curses, qt, flask")
      view_name = "console"

   if view_name == "console":
      MainView = ConsoleView
   elif view_name == "curses":
      from .views.curses import CursesView as MainView
   elif view_name == "tk":
      from .views.tk import TkView as MainView
   elif view_name == "qt":
      from .views.qt import QtView as MainView
   elif view_name == "kivy":
      # don't move it to the top of the file:
      # importing kivyl writes stuff to console even if you set log_level='critical'
      # so only import it if you need it
      from .views.kv import KivyView as MainView
   elif view_name == "flask":
      from .views.fl.fl import FlaskView as MainView
   elif view_name == "tk-kivy":
      from .views.tk import TkView as MainView
      def kv():
         from .views.kv import KivyView
         kivy_view = KivyView(controller.dispatch_event)
         controller.model_subscribe(kivy_view)
         kivy_view.mainloop()
      Thread(target=kv, args=()).start()
      # TODO: if Flask is being launched in a separate thread,
      # it still somehow manages to block the program
      # TODO: for reasons I don't quite understand,
      # Qt doesn't work well when launched in a separate thread
      # but it also doesn't update without being clicked, which I also don't understand
   else:
      print(f"Unknown view: {view_name}")
      quit()

   if view_name not in ["console", "curses"]:
      # a console view without mainloop won't start a repl,
      # but still will print nicely colored values on change
      controller.model_subscribe(ConsoleView(controller.dispatch_event))

   view = MainView(controller.dispatch_event)
   controller.model_subscribe(view)
   view.mainloop()
