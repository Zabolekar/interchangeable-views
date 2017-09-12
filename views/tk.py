from tkinter import Tk
from tkinter import Button, Scale, Label
from ..base_classes import View

ARABIC = "٠١٢٣٤٥٦٧٨٩"
DEVANAGARI = "०१२३४५६७८९"
TIBETAN = "༠༡༢༣༤༥༦༧༨༩"
BENGALI = "০১২৩৪৫৬৭৮৯"
KHMER = "០១២៣៤៥៦៧៨៩"
KANNADA = "೦೧೨೩೪೫೬೭೮೯"

def convert(n, to):
   return "".join(to[int(i)] for i in str(n))

class TkView(View):
   def __init__(self, dispatch_event):
      print("initializing TkView")
      self.dispatch_event = dispatch_event
      self.root = Tk()
      self.but = Button(self.root, command=lambda: dispatch_event("increment"))
      self.but2 = Button(self.root, command=lambda: dispatch_event("increment"))

      self.scale = Scale(self.root, from_=0, to=99, showvalue=False,
                         state="disabled", orient="horizontal",
                         length=200, sliderlength=20, relief="sunken")
      
      self.lab = Label(self.root, font=("Helvetica", 20))

      self.but.grid(row=0, column=0)
      self.scale.grid(row=0, column=1)
      self.but2.grid(row=0, column=2)
      self.lab.grid(row=1, column=0, columnspan=3)
      
      self.root.protocol("WM_DELETE_WINDOW", self.on_delete_window)
      
   def on_delete_window(self):
      self.dispatch_event("quit")
      self.close()
      
   def close(self):
      self.root.destroy()

   def inform(self, model_data):
      n = model_data["n"]

      self.root.title(str(n))

      self.but["text"] = f"{n:08b}"

      self.scale["state"] = "active"
      self.scale.set(n % 100)
      self.scale["state"] = "disabled"

      self.but2["text"] = f"{n:#04x}"

      ar = convert(n, ARABIC)
      hi = convert(n, DEVANAGARI)
      ti = convert(n, TIBETAN)
      be = convert(n, BENGALI)
      kh = convert(n, KHMER)
      ka = convert(n, KANNADA)
      
      self.lab["text"] = f"{ar}   {hi}   {ti}\n{be}   {kh}   {ka}"
   def mainloop(self):
      self.root.mainloop()
