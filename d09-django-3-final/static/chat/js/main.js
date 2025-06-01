let gHost = undefined;
let gRoomPathname = undefined;
let gWebSocketURL = undefined;
let gWebSocket = undefined;

function joinOrLeave(jsonData, action, fontColor) {
	let username = jsonData.data.username;

	let $messagesDiv = $('#messages');

	let $newMessageNode = $('<div></div>');
	let $usernameNode = $('<span></span>');

	$newMessageNode.addClass(`d-flex justify-content-center align-items-center w-100 text-${fontColor}`);

	$newMessageNode.css('font-size', '18px');

	$usernameNode.html(`<b>${username}</b> has ${action} the chat`);

	$newMessageNode.append($usernameNode);
	$messagesDiv.append($newMessageNode);
}

function main() {
	try {
		gHost = window.location.host;
		gRoomPathname = window.location.pathname;
		gWebSocketURL = `ws://${gHost}${gRoomPathname}`;

		gWebSocket = new WebSocket(gWebSocketURL);

		gWebSocket.onmessage = function (e) {
			let jsonData = JSON.parse(e.data);

			if (jsonData.cmd === 'join') { joinOrLeave(jsonData, 'joined', 'success'); }
			else if (jsonData.cmd === 'leave') { joinOrLeave(jsonData, 'left', 'danger'); }
			else if (jsonData.cmd === 'message') {
				let text = jsonData.data.text;
				let username = jsonData.data.username;

				let $messagesDiv = $('#messages');

				let $newMessageNode = $('<div></div>');
				let $textNode = $('<span></span>');
				let $usernameNode = $('<span></span>');

				$newMessageNode.addClass('d-flex flex-column justify-content-center align-items-center w-100 my-1');
				$usernameNode.addClass('d-flex flex-column justify-content-center align-items-start fw-bold w-100');
				$textNode.addClass('d-flex flex-column justify-content-center align-items-start w-100');

				$usernameNode.css('font-size', '22px');
				$textNode.css('font-size', '16px');

				$usernameNode.text(username);
				$textNode.text(text);

				$newMessageNode.append($usernameNode);
				$newMessageNode.append($textNode);
				$messagesDiv.append($newMessageNode);
			}
		};

		return 0;
	} catch (err) { console.error(err); return 1; }
}

$(document).ready(main);
