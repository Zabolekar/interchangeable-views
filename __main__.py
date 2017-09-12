from sys import argv
from threading import Thread

from .views.console import ConsoleView

# you should generally avoid importing other views at the top of the file:
# for example, importing kivy writes stuff to console even if you set log_level='critical'
# and importing matplotlib takes some time

# TODO: place all the models into a separate models folder, and maybe untie model and controller classes, because currently we have two controllers whose code is identical
# TODO: if Flask is being launched in a separate thread,
# it still somehow manages to block the program
# TODO: for reasons I don't quite understand,
# Qt doesn't work well when launched in a separate thread
# but it also doesn't update without being clicked, which I also don't understand
# TODO: for whatever reason Tk and Kivy run fine together, Tk and Matplotlib do too, but all three together don't
# TODO: for whatever reason matplotlib is unresponsive when called with qt-matplotlib
# changind the backend to Qt4Agg doesn't fix it ("A QApplication instance already exists")
# TODO: tk-matplotlib backends behaves really ugly if one of the windows has been closed
# Solution: every view should send a "quit" message on being closed, controller should be able to handle it. So every view should
# additionally have a .close() method? And who should call it, model or controller? And where should we really place the views list, in the model or in the controller? Think about it
# the controller should probably also be able to unsubscribe a view when the view requests it. How would I implement it?

from .my_controller import MyController

if __name__ == '__main__':
   try:
      model_name = argv[1]
      if model_name == "my-model":
         from .models.my_model import MyModel as model_class
      elif model_name == "my-r-model":
         from .models.my_r_model import MyRModel as model_class
      else:
         print(f"Unknown model: {model_name}")
         quit()
   except IndexError:
      print("You haven't selected any model")
      print("Default is my-model. Others are: my-r-model")
      from .models.my_model import MyModel as model_class

   controller = MyController(model_class)

   try:
      view_name = argv[2]
   except IndexError:
      print("You haven't selected any view")
      print("Default is console. Others are: tk, kivy, matplotlib, curses, qt, flask, tk-kivy, tk-matplotlib, qt-matplotlib (experimental)")
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
      from .views.kv import KivyView as MainView
   elif view_name == "flask":
      from .views.fl.fl import FlaskView as MainView
   elif view_name == "matplotlib":
      from .views.mpl import MatplotlibView as MainView
   elif view_name == "tk-kivy":
      from .views.tk import TkView as MainView
      def kv():
         from .views.kv import KivyView
         kivy_view = KivyView(controller.dispatch_event)
         controller.model_subscribe(kivy_view)
         kivy_view.mainloop()
      Thread(target=kv, args=()).start()
   elif view_name == "tk-matplotlib":
      from .views.tk import TkView as MainView
      from .views.mpl import MatplotlibView
      mpl_view = MatplotlibView(controller.dispatch_event)
      controller.model_subscribe(mpl_view)
   elif view_name == "qt-matplotlib":
      from .views.qt import QtView as MainView
      from .views.mpl import MatplotlibView
      mpl_view = MatplotlibView(controller.dispatch_event)
      controller.model_subscribe(mpl_view)
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
