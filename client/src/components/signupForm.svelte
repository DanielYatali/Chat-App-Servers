<script>
	import { form, field } from 'svelte-forms';
	import { matchField, required } from 'svelte-forms/validators';
	import { goto } from '$app/navigation';

	const name = field('name', '', [required()], {
		validateOnChange: false
	});
	const password = field('password', '', [required()], {
		validateOnChange: false
	});
	const email = field('email', '', [required()], {
		validateOnChange: false
	});
	const passwordConfirmation = field('passwordConfirmation', '', [matchField(password)]);
	const myForm = form(name, email, password, passwordConfirmation);

	let signupResponse = '';
	const validate = () => {
		myForm.validate();
		const noError =
			$myForm.hasError('name.required') ||
			$myForm.hasError('password.required') ||
			$myForm.hasError('email.required') ||
			$myForm.hasError('passwordConfirmation.match_field');
		if (!noError) {
			const user = {
				username: $name.value,
				password: $password.value,
				email: $email.value
			};
			(async () => {
				const rawResponse = await fetch(
					'https://hpofficepaper-database-chatapp.herokuapp.com/signup',
					{
						method: 'POST',
						headers: {
							Accept: 'application/json',
							'Content-Type': 'application/json'
						},
						body: JSON.stringify(user)
					}
				);
				const content = await rawResponse.json();
				console.log(content);
				signupResponse = content;
				if (signupResponse == 'user created') {
					goto('/login');
				}
			})();
		}
	};
</script>

<div class="card">
	<h3 class="font-semibold text-3xl">Sign Up</h3>
	<input class="input" type="text" bind:value={$name.value} placeholder="Enter Name" />
	{#if $myForm.hasError('name.required')}
		<div class="error">Name is required</div>
	{/if}
	<input class="input" type="email" bind:value={$email.value} placeholder="Email" />
	{#if $myForm.hasError('email.required')}
		<div class="error">Email is required</div>
	{/if}
	<input class="input" type="password" bind:value={$password.value} placeholder="Password" />
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

	{#if signupResponse === 'username or email already exists'}
		<p>{signupResponse}</p>
	{/if}
	<button class="action-btn" on:click={validate}>Sign Up</button>
</div>

<style>
</style>
