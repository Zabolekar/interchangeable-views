from helpers.mvc import View

from tkinter import Tk, Button, Scale, Label

arabic = "٠١٢٣٤٥٦٧٨٩"
devanagari = "०१२३४५६७८९"
tibetan = "༠༡༢༣༤༥༦༧༨༩"

def convert(n, to):
   return "".join(to[int(i)] for i in str(n))

class TkView(View):
   def __init__(self, command):
      print("initializing TkView")
      self.root = Tk()
      self.but = Button(self.root, command=command)
      self.but2 = Button(self.root, command=command)

      self.scale = Scale(self.root, from_=0, to=99, showvalue=False,
                         state="disabled", orient="horizontal",
                         length=200, sliderlength=20, relief="sunken")
                         
      self.lab = Label(self.root, font=("Courier", 20))

      self.but.grid(row=0, column=0)
      self.scale.grid(row=0, column=1)
      self.but2.grid(row=0, column=2)
      self.lab.grid(row=1, column=0, columnspan=3)

   def inform(self, model):
      self.root.title(str(model.n))
   
      self.but["text"] = f"{model.n:08b}"
      
      self.scale["state"] = "active"
      self.scale.set(model.n % 100)
      self.scale["state"] = "disabled"
      
      self.but2["text"] = f"{model.n:#04x}"
      
      ar = convert(model.n, arabic)
      hi = convert(model.n, devanagari)
      ti = convert(model.n, tibetan)
      self.lab["text"] = f"{ar}   {hi}   {ti}"
   def mainloop(self):
      self.root.mainloop()