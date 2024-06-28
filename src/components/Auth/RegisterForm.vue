<template>
    <div class="login">
        <form @submit.prevent="login">
            <h2>注册</h2>
            <input v-model="username" placeholder="Username" required />
            <input v-model="password" type="password" placeholder="Password" required />
            <button type="submit">Login</button>
            <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
        </form>
    </div>
</template>

<script>


export default {
    data() {
        return {
            username: '',
            password: '',
            errorMessage: ''
        };
    },
    methods: {
        
    }
};
</script>

<style scoped>
.login {
    max-width: 400px;
    margin: 0 auto;
    padding: 1em;
    border: 1px solid #ccc;
    border-radius: 5px;
}

input {
    display: block;
    width: 100%;
    padding: 0.5em;
    margin: 0.5em 0;
}

button {
    width: 100%;
    padding: 0.5em;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.error {
    color: red;
    margin-top: 1em;
}
</style>