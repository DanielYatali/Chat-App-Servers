<script context="module">
	import { get } from 'svelte/store';
	import currentUser from '../../stores/userDataStore.js';
	export async function load({ url, params }) {
		const receiver = params.to;
		const sender = get(currentUser);
		if (!sender.loggedIn) {
			goto('/');
		}
		let oldMessages = null;
		(async () => {
			const rawResponse = await fetch(
				'https://hpofficepaper-database-chatapp.herokuapp.com/conversation/messages',
				{
					method: 'POST',
					headers: {
						Accept: 'application/json',
						Authorization: 'JWT ' + sender.token,
						'Content-Type': 'application/json'
					},
					body: JSON.stringify(receiver)
				}
			);
			oldMessages = await rawResponse.json();
			console.log(oldMessages);
		})();

		return {
			props: {
				receiver,
				sender,
				oldMessages
			}
		};
	}
</script>

<script>
	import ChatBox from '../../components/chatbox.svelte';
	import { goto } from '$app/navigation';
	export let receiver;
	export let sender;
	export let oldMessages;

	// if(!messages)
</script>

<h1>Welcome {sender.username}</h1>
<div>
	<ChatBox {receiver} {sender} {oldMessages} />
</div>
