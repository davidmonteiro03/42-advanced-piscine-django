function login(event) {
	if (event === undefined || event === null || event === '') { return 1; }
	try {
		event.preventDefault();
		const formData = new FormData(event.target);
		const csrfToken = formData.get('csrfmiddlewaretoken');
		formData.delete('csrfmiddlewaretoken');
		const xhr = new XMLHttpRequest();
		xhr.open('POST', '/account/login', true);
		xhr.setRequestHeader('X-CSRFToken', csrfToken);
		xhr.onreadystatechange = function () {
			if (xhr.readyState === 4) {
				if (xhr.status === 200) {
					try {
						const data = JSON.parse(xhr.responseText);
						document.body.innerHTML = data.html;
					}
					catch (err) { console.error(`Error: ${err}`); }
				} else {
					try {
						const responseJson = JSON.parse(xhr.responseText);
						showError(event, responseJson.error);
					}
					catch (err) { console.error(`Error: ${err}`); }
				}
			}
		};
		xhr.send(formData);
		return 0;
	}
	catch (err) {
		console.error(`Error: ${err}`);
		return 1;
	}
}

function showError(event, errorMsg) {
	if (event.target.previousElementSibling === null) {
		const newElement = document.createElement('span');
		newElement.classList.add('text-danger', 'mb-2');
		event.target.parentNode.insertBefore(newElement, event.target);
	}
	event.target.previousElementSibling.innerText = errorMsg;
}
