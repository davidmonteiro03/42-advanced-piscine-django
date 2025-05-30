const host = window.location.host;
const roomPathname = window.location.pathname;
const wsURL = `ws://${host}${roomPathname}`;

const gWebSocket = new WebSocket(wsURL);

gWebSocket.onmessage = function (e) {
	let jsonData = JSON.parse(e.data);
	console.log(jsonData.message);
};
