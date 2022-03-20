<script context="module">
	import { get } from 'svelte/store';
	import currentUser from '../../stores/userDataStore.js';
	export async function load({ url, params }) {
		const Receiver = params.to;
		const Sender = get(currentUser);
		return {
			props: {
				Receiver,
				Sender
			}
		};
	}
</script>

<script>
	import ChatBox from '../../components/chatbox.svelte';
	export let Receiver;
	export let Sender;
</script>

<h1>Welcome {Sender.username}</h1>
<div>
	<ChatBox receiver={Receiver} sender={Sender} />
</div>
