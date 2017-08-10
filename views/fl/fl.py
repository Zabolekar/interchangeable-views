from time import strftime
from flask import Flask, render_template, Response
from ...helpers.mvc import View

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
         return Response(f"retry: 1000\ndata:{self.text}", mimetype="text/event-stream")

      self.app, self.index, self.on_click, self.stream = app, index, on_click, stream

   def inform(self, model_data):
      self.text = f"--- {model_data['n']} ---"
      # TODO:
      # do you see the bug here? We only change the text variable, not the page
      # The whole construction only works because the page changes itself on every button press
      # And also because there is a stream that the page reads every second
      # And also because we have set the initial button value manually in the template
      # We can see the bug if we refresh the page:
      # the value becomes 0, but the server stores the correct value
      # also, if we use multiple views (e.g. by launching flask in a separate thread),
      # the number on the website does not get updated until we push the button on the website

   def mainloop(self):
      self.app.run(threaded=True)
