let button = document.getElementById("button");

button.onclick = function () {
   var request = new XMLHttpRequest();

   request.open('GET', $SCRIPT_ROOT + '/on_click', true);

   request.onload = function() {
      // we don't care about this.status
      button.innerText = this.response;
   };

   // we don't care about connection errors either

   request.send();
}

let stream = new EventSource('/stream');

stream.onmessage = function (event) {
   button.innerText = event.data;
};
