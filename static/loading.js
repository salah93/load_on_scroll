var index = 0;
var range = 50;
$('#submit').click(function(){
  $.getJSON('/table', {index: index, range: range}, function(data) {
    var table = data.table;
    for(var i = 0; i < range && i < table.length; i++) {
      var row = $('<tr>').append($('<td>').append(document.createTextNode(table[i])));
      $('tbody').append(row);
    }
  });
});


$(window).scroll(function() {
  if($(window).scrollTop() == ($(document).height() - $(window).height())) {
    index = index + range;
    $.getJSON('/table', {index: index, range: range}, function(data) {
      var table = data.table;
      if (table.length == 0)
        $(window).off('scroll');
      else
        for(var i = 0; i < range && i < table.length; i++) {
          var row = $('<tr>').append($('<td>').append(document.createTextNode(table[i])));
          $('tbody').append(row);
        }
    });
  }
});
