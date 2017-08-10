from ..helpers.mvc import View

import sys
from PySide.QtGui import QApplication, QPushButton, QTextDocument, QPixmap, QPainter, QColor

def button_set_HTML(button, html):
   doc = QTextDocument()
   doc.setHtml(html)
   doc.setTextWidth(doc.size().width())
   pixmap = QPixmap(doc.size().width(), doc.size().height())
   pixmap.fill(QColor(0,0,0,0))
   painter = QPainter(pixmap)
   doc.drawContents(painter)
   painter.end()
   button.setIconSize(pixmap.size())
   button.setIcon(pixmap)

class QtView(View):
   def __init__(self, dispatch_event):
      print("initializing QtView")
      self.app = QApplication(sys.argv)
      self.but = QPushButton()
      self.but.clicked.connect(lambda: dispatch_event("increment"))
      self.but.show()
   def inform(self, model):
      m, n = model.n//5, model.n % 5
      html = " ".join(["<s>||||</s>"]*m)+" "+"|"*n
      button_set_HTML(self.but, html)
   def mainloop(self):
      self.app.exec_()