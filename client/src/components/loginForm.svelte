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
			(async () => {
  const rawResponse = await fetch('https://8080-danielyatali-flaskmvc-3cd8pezq48y.ws-us38.gitpod.io/auth', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(user)
  });
  const content = await rawResponse.json();

  console.log(content);
})();
		// console.log(user);
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