<script>
	import { form, field } from 'svelte-forms';
	import { matchField, required } from 'svelte-forms/validators';

	const name = field('name', '', [required()], {
		validateOnChange: false,
	});
	const password = field('password', '', [required()], {
		validateOnChange: false,
	});
	const email = field('email', '', [required()], {
		validateOnChange: false,
	});
	const passwordConfirmation = field('passwordConfirmation', '', [
		matchField(password),
	]);
	const myForm = form(name, password, email, passwordConfirmation);
	function validate() {
		name.validate();
		password.validate();
		passwordConfirmation.validate();
		email.validate();
		let user = {
			username: $name.value,
			password: $password.value,
      passwordConfirm: $passwordConfirmation.value,
			email: $email.value,
		};
		console.log(user);
		// fetch('https://alivewrathfulwireframe.danielyatali0.repl.co/rand', {
		// 	mode: 'no-cors',
		// })
		// 	.then((results) => results.json())
		// 	.then(console.log);
	}
</script>

<div class="card">
	<h3 class="font-semibold text-3xl">Sign Up</h3>
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
	<input
		class="input"
		type="password"
		bind:value={$passwordConfirmation.value}
		placeholder="Repeat Passoword"
	/>
	{#if $myForm.hasError('passwordConfirmation.match_field')}
		<div class="error">Password does not match</div>
	{/if}
	<input
		class="input"
		type="email"
		bind:value={$email.value}
		placeholder="Email"
	/>
	{#if $myForm.hasError('email.required')}
		<div class="error">Email is required</div>
	{/if}

	<button
		class="action-btn"
		on:click={validate}>Sign Up</button
	>
</div>

<style>
</style>
