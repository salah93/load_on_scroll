var range = 50;

function addToTable(table) {
  for(var i = 0; i < range && i < table.length; i++) {
    var text = document.createTextNode(table[i]);
    var col = $('<td>').append(text);
    var row = $('<tr>').append(col);
    $('tbody').append(row);
  }
}

$('#submit').click(function(){
  range = $('#range').val() || range;
  $.getJSON('/table', {range: range}, function(data) {
    var table = data.table;
    addToTable(table);
  });
});


$(window).scroll(function() {
  if(parseInt($(window).scrollTop()) == ($(document).height() - $(window).height())) {
	$('.results').addClass('loader');
    $.getJSON('/table', {range: range}, function(data) {
      addToTable(data.table);
	  $('.results').removeClass('loader');
    });
  }
});
