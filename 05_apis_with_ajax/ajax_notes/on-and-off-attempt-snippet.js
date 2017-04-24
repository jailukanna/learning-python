function displayTitleForm(event) {
	$(this).html("<input type='text'>");
	var id = $(this).parent().attr("id"); 
	var placeholder = $(this).parent().attr("value");
	$(this).children().attr({
	  value: placeholder,
	  name: 'updateTitle' + id
	});
	  $(this).children().focus();
}

$(document).ready(function(){
    $('.title').children().on('click', displayTitleForm);
}); // end .ready