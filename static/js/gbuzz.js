function buzzHandleResponse(response) {

	var container = document.getElementById('buzz');
	if (!container)
		return;

	var buzzes = document.createElement('ul');
	for (var i = 0; i < Math.min(3, response.data.items.length); i++) {
		var item = response.data.items[i];
		// in production code, item.title should have the HTML entities escaped.
		var buzz = document.createElement('li');
		buzz.innerHTML = '<a href="' + item.links.alternate[0].href + '">' + item.title + '</a>';
		buzzes.appendChild(buzz);
	}

	var title = document.createElement('h3');
	title.innerHTML = 'Recent buzzes';

	container.appendChild(title);
	container.appendChild(buzzes);
}
