$(function () {
   $("button").bind("click", function () {
      $.get($SCRIPT_ROOT + '/on_click', {}, function (data) {
         $("button").text(data);
      });
   });
});

var stream = new EventSource('/stream');

stream.onmessage = function (event) {
   $("button").text(event.data);
};