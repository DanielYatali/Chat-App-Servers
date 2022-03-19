<script>
	import { form, field } from 'svelte-forms';
	import { required } from 'svelte-forms/validators';


	//Creating form fields
	const name = field('name', '', [required()], {
		validateOnChange: false,
	});
	const password = field('password', '', [required()], {
		validateOnChange: false,
	});

	
	const myForm = form(name, password);
	
	//Validates the user input when button is clicked
	function validate() {
		name.validate();
		password.validate();
		let user = {
			username: $name.value,
			password: $password.value,
		};
		console.log(user);
		// fetch('https://alivewrathfulwireframe.danielyatali0.repl.co/rand', {
		// 	mode: 'no-cors',
		// })
		// 	.then((results) => results.json())
		// 	.then(console.log);
	}
</script>
<!-- conditional rendering -->
<div class="card">
	<h3 class="font-semibold text-3xl">Login</h3>
	<input
		class="input"
		type="text"
		bind:value={$name.value}
		placeholder="Enter Name"
	/>
	{#if $myForm.hasError('name.required')}
		<div class="error">Name is required</div>
	{/if}
	<input
		class="input"
		type="password"
		bind:value={$password.value}
		placeholder="Password"
	/>
	{#if $myForm.hasError('password.required')}
		<div class="error">Password is required</div>
	{/if}

	<button
		class="action-btn"
		on:click={validate}>Sign Up</button
	>
</div>

<style>
</style>