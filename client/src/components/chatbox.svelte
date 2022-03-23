<script>
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte/internal';
	import { io } from 'socket.io-client';
	export let receiver;
	export let sender;
	let messages = [];
	let message;
	onMount(() => {
		let data = {};
		data['conversation_name'] = receiver;
		(async () => {
			const rawResponse = await fetch('http://localhost:8080/conversation/messages', {
				method: 'POST',
				headers: {
					Accept: 'application/json',
					Authorization: 'JWT ' + sender.token,
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(data)
			});
			messages = await rawResponse.json();
			console.log(messages);
		})();
	});
	// const socket = io('https://hpoffice-paper-chat-app-server.herokuapp.com/');
	const socket = io('http://localhost:5000/');
	let id;
	let chat_box;
	//Remember to implent this in an onLoad function
	socket.on('connection', () => {
		console.log(socket.id);
	});
	socket.on('connect', () => {
		id = socket.id;
		console.log(socket.id);
		console.log(receiver);
		socket.emit('join-room', receiver);
		socket.on('receive-message', (msg) => {
			messages = [...messages, msg];
		});
	});

	const handleSubmit = () => {
		let today = new Date();
		// let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
		let time = today.getHours() + ':' + today.getMinutes() + ':' + today.getSeconds();
		// let dateTime = date+' '+time;
		if (message != '')
			socket.emit('send-message', {
				conversation_name: receiver,
				sender_name: sender.username,
				content: message,
				datetime: time,
				token: sender.token
			});
		message = '';
	};
</script>

<h1>Sender : {sender.username} Receiver: {receiver}</h1>
<div class="container flex flex-col bg-red-500 p-10">
	<div bind:this={chat_box} class="h-96 bg-orange-400 overflow-y-scroll">
		{#each messages as message}
			{#if message.sender_name == sender.username}
				<div class="flex flex-col message sent">
					<p class="flex text-gray-500">{message.sender_name}</p>
					<p>{message.content}</p>
					<p class="float-right">{message.datetime}</p>
				</div>
			{:else}
				<div class="flex flex-col message received">
					<p class="flex text-gray-500">{message.sender_name}</p>
					<p>{message.content}</p>
					<p class="float-right">{message.content}</p>
				</div>
			{/if}
		{/each}
	</div>

	<div class="relative text-gray-700">
		<input
			bind:value={message}
			class="w-full h-10 pl-3 pr-8 text-base placeholder-gray-500 border rounded-lg focus:shadow-outline"
			type="text"
			placeholder="Enter Text"
		/>

		<button
			on:click={handleSubmit}
			class="absolute inset-y-0 right-0 flex items-center px-4 font-bold text-white bg-indigo-600 rounded-r-lg hover:bg-indigo-500 focus:bg-indigo-700"
			>Submit</button
		>
	</div>
</div>

<style>
	.message {
		color: #000;
		clear: both;
		line-height: 18px;
		font-size: 15px;
		padding: 8px;
		position: relative;
		margin: 8px 0;
		width: 25%;
		max-width: 85%;
		word-wrap: break-word;
		/* z-index: -1; */
	}

	.message:after {
		position: absolute;
		content: '';
		width: 0;
		height: 0;
		border-style: solid;
	}

	.message.received {
		background: #fff;
		border-radius: 0px 5px 5px 5px;
		float: left;
	}

	.message.received .metadata {
		padding: 0 0 0 16px;
	}

	.message.received:after {
		border-width: 0px 10px 10px 0;
		border-color: transparent #fff transparent transparent;
		top: 0;
		left: -10px;
	}

	.message.sent {
		background: #e1ffc7;
		border-radius: 5px 0px 5px 5px;
		float: right;
	}

	.message.sent:after {
		border-width: 0px 0 10px 10px;
		border-color: transparent transparent transparent #e1ffc7;
		top: 0;
		right: -10px;
	}
</style>
