from time import strftime
from flask import Flask, render_template, Response
from ...base_classes import View

class FlaskView(View):
   def __init__(self, dispatch_event):
      print("initializing FlaskView")
      
      self.dispatch_event = dispatch_event
      self.text = None

      app = Flask(__name__)

      @app.route("/")
      def index():
         now = strftime("%d.%m.%Y %H:%M:%S")
         return render_template("index.html", time=now)

      @app.route("/on_click")
      def on_click():
         self.dispatch_event("increment")
         return self.text

      @app.route('/stream')
      def stream():
         return Response(f"\nretry: 1000\ndata:{self.text}\n\n", mimetype="text/event-stream")

      self.app, self.index, self.on_click, self.stream = app, index, on_click, stream

   def inform(self, model_data):
      self.text = f"--- {model_data['n']} ---"

   def mainloop(self):
      self.app.run(threaded=True)
