import { writable } from 'svelte/store';

const currentUser = writable({
	username: '',
	token: '',
	loggedIn: false
});

export default currentUser;
