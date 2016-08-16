var index = 0;
var range = 50;
var query = "1234"

function addToTable(table) {
  for(var i = 0; i < range && i < table.length; i++) {
    var text = document.createTextNode(table[i]);
    var col = $('<td>').append(text);
    var row = $('<tr>').append(col);
    $('tbody').append(row);
  }
}

$('#submit').click(function(){
  $.getJSON('/table', {query: query, index: index, range: range}, function(data) {
    var table = data.table;
    addToTable(table);
  });
});


$(window).scroll(function() {
  if($(window).scrollTop() == ($(document).height() - $(window).height())) {
	$('.results').addClass('loader');
    index = index + range;
    $.getJSON('/table', {query: query, index: index, range: range}, function(data) {
      $('#load').html
      var table = data.table;
      if (table.length == 0)
        $(window).off('scroll');
      else
        addToTable(table);
	  $('.results').removeClass('loader');
    });
  }
});
