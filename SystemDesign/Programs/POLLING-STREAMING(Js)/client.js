const helpers = require('./helpers');
const messagingApi = require('./messaging_api');
const readline = require('readline');

const displayedMessages = {}
const username = process.argv[2];
const mode = process.argv[3];

const terminal = readline.createInterface({
    input: process.stdin,
});

terminal.on('line', text => {
    const id = helpers.getRandomInt(100000);
    displayedMessages[id] = true;

    const message = { id, text, username };
    messagingApi.sendMessage(message);
});

function displayMessages(message) {
    console.log(`> ${message.username}: ${message.text}`);
    displayedMessages[message.id] = true;
}

async function getAndDisplayMessages() {
    const messages = await messagingApi.getMessages();
    for (const message of messages) {
        const messageAlreadyDisplayed = message.id in displayedMessages;
        if (!messageAlreadyDisplayed) displayMessages(message);
    }
}

function pollMessages() {
    setInterval(getAndDisplayMessages, 3000);
}

function streamMessages() {
    const messagingSocket = messagingApi.createMessagingSocket();

    messagingSocket.on('message', data => {
        const message = JSON.parse(data);
        const messageAlreadyDisplayed = message.id in displayedMessages;
        if (!messageAlreadyDisplayed) displayMessages(message);
    })
}


if (mode === 'poll') {
    getAndDisplayMessages();
    pollMessages();
} else if (mode === 'stream') {
    getAndDisplayMessages();
    streamMessages();
}