<script context="module">
	import { get } from 'svelte/store';
	import currentUser from '../../stores/userDataStore.js';
	export async function load({ url, params }) {
		const receiver = params.to;
		const sender = get(currentUser);
		return {
			props: {
				receiver,
				sender
			}
		};
	}
</script>

<script>
	import ChatBox from '../../components/chatbox.svelte';
	export let receiver;
	console.log('int to' + receiver);
	export let sender;
</script>

<h1>Welcome {sender.username}</h1>
<div>
	<ChatBox {receiver} {sender} />
</div>
