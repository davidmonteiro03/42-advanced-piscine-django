const ws = new WebSocket('ws://' + window.location.host + '/ws/');

ws.onopen = function (e) {
	console.log(e);
	console.log('<username> has joined the chat');
};
