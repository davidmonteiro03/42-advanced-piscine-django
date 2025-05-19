async function logout(event) {
	event.preventDefault();
	const formData = new FormData(event.target);
	const csrfToken = formData.get('csrfmiddlewaretoken');
	formData.delete('csrfmiddlewaretoken');
	$.ajax({
		url: '/account/logout',
		method: 'POST',
		headers: { 'X-CSRFToken': csrfToken },
	}).done(function (data) {
		$(document.body).html(data.html);
	});
}
