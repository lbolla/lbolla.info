function init () {
	$('html').mousemove(function () { 
		$('.fade').fadeIn(); 
		$(this).unbind('mousemove');
	});
}

$(document).ready(init);
