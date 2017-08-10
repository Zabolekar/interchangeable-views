from ...helpers.mvc import View

from typing import NamedTuple, Callable

from flask import Flask, render_template, Response
app = Flask(__name__)

# module scope variables
_command: Callable[[], None]
_text: str

class FlaskView(View):
   def __init__(self, dispatch_event):
      print("initializing FlaskView")
      global _dispatch_event
      _dispatch_event = dispatch_event
   def inform(self, model_data):
      global _text
      _text = f"--- {model_data['n']} ---"
      # DO YOU SEE THE BUG HERE? We only change the text variable, not the page
      # The whole construction only works because the page changes itself on every button press
      # And also because there is a stream that the page reads every second
      # And also because we have set the initial button value manually in the template
      # We can see the bug if we refresh the page: the value becomes 0, but the server stores the correct value
   def mainloop(self):
      app.run(threaded=True)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/on_click")
def on_click():
   _dispatch_event("increment")
   return _text

@app.route('/stream')
def stream():
   return Response(f"retry: 1000\ndata:{_text}", mimetype="text/event-stream")