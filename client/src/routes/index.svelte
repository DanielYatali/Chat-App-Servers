<script>
	import { io } from 'socket.io-client';
	import { onMount } from 'svelte';
	let id
	const socket = io('https://hpoffice-paper-chat-app-server.herokuapp.com/');

	//Remember to implent this in an onLoad function
	socket.on('connection', () => {
		console.log(socket.id);
	});
	socket.on('connect', () => {
		id = socket.id
		// console.log(socket.connected);
		console.log(socket.id);
		socket.on('receive-message', (msg) => {
			messages = [...messages, msg];
			// console.log(msg);
		});
	});
	let messages = [];
	let message;

	const handleSubmit = () => {
		if(message != "")
			socket.emit('send-message', {"msg": message, "id": id});
		message = ''
	};
</script>

<div class="container flex flex-col overflow-y-auto bg-red-500 p-10">
	<div class="h-96 bg-orange-400">

		{#each messages as message}
		{#if message.id == id}
		<p class="message sent">{message.msg}</p>
		{:else}
		<p class="message received">{message.msg}</p>
		{/if}
		{/each}
	</div>
	
	<div class="relative text-gray-700">
		<input bind:value={message} class="w-full h-10 pl-3 pr-8 text-base placeholder-gray-500 border rounded-lg focus:shadow-outline" type="text" placeholder="Enter Text"/>
	
  <button on:click={handleSubmit} class="absolute inset-y-0 right-0 flex items-center px-4 font-bold text-white bg-indigo-600 rounded-r-lg hover:bg-indigo-500 focus:bg-indigo-700">Submit</button>
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
  max-width: 85%;
  word-wrap: break-word;
  /* z-index: -1; */
}

.message:after {
  position: absolute;
  content: "";
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