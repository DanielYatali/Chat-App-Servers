<script>
	import { io } from 'socket.io-client';
	import { onMount } from 'svelte';

	const socket = io('https://hpoffice-paper-chat-app-server.herokuapp.com/');
	socket.on('connection', () => {
		console.log(socket.id);
	});
	socket.on('connect', () => {
		console.log(socket.connected);
		console.log(socket.id);
		socket.on('receive-message', (msg) => {
			messages = [...messages, msg];
			console.log(msg);
		});
	});
	let messages = [];
	let message;

	const handleSubmit = () => {
		socket.emit('send-message', message);
	};
</script>

{#each messages as message}
	<p>{message}</p>
	<!-- content here -->
{/each}

<input type="text" bind:value={message} placeholder="enter text" />
<button on:click={handleSubmit}>Submit</button>
