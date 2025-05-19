async function login(event) {
	event.preventDefault();
	const formData = new FormData(event.target);
	const csrfToken = formData.get('csrfmiddlewaretoken');
	formData.delete('csrfmiddlewaretoken');
	$.ajax({
		url: '/account/login',
		method: 'POST',
		headers: { 'X-CSRFToken': csrfToken },
		data: formData,
		processData: false,
		contentType: false,
	}).done(function (data) {
		$(document.body).html(data.html);
	}).fail(function (jqXhr) {
		const responseJson = JSON.parse(jqXhr.responseText);
		if (event.target.previousElementSibling === null) {
			const newElement = document.createElement('span');
			newElement.classList.add('text-danger', 'mb-2');
			event.target.parentNode.insertBefore(newElement, event.target);
		}
		event.target.previousElementSibling.innerText = responseJson.error;
	});
}
