<script>
	import { goto } from '$app/navigation';

	import { onMount } from 'svelte';

	import { get } from 'svelte/store';
	import currentUser from '../stores/userDataStore';

	let User = {};
	onMount(() => {
		User = get(currentUser);
		//enable this after testing
		// if (!User.loggedIn) {
		// 	goto('/');
		// }
	});
	const Rooms = ['Room-1', 'Room-2', 'Room-3', 'Room-4'];
	let selected = 'Room-1';
	const handleSelect = () => {
		goto(`/chat/${selected}`);
	};
</script>

<h1>Welcome {User.username}</h1>
<h2>Tell us about yourself {User.username}</h2>
<select bind:value={selected} on:change={handleSelect}>
	{#each Rooms as room}
		<!-- content here -->
		<option value={room}>
			{room}
		</option>
	{/each}
</select>
<br />
<br />
<h1>Selected room is : {selected}</h1>
