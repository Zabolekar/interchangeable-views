from ..helpers.mvc import View

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config

kivy.require('1.9.1')
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class MyApp(App):
   def build(self):
      self.title = "Counter"
      return self.but

class KivyView(View):
   def __init__(self, dispatch_event):
      print("Initializing KivyView")
      self.app = MyApp()
      self.app.but = Button()
      self.app.but.bind(on_press=lambda _: dispatch_event("increment"))
      self.app.but.bind(on_release=lambda _: dispatch_event("increment"))
   def inform(self, model_data):
      n = model_data["n"]
      self.app.but.text = str(n)
      self.app.but.font_size = n+5
   def mainloop(self):
      self.app.run()