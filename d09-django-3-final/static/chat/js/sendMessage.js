function sendMessage(event) {
	try {
		event.preventDefault();

		const $form = $(event.target);
		const text = $form.find('[name="text"]').val();
		$form[0].reset();

		gWebSocket.send(JSON.stringify({ 'text': text }));

		return 0;
	} catch (err) { console.error(err); return 1; }
}
