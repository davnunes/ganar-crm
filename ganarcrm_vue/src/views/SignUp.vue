<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign Up</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" name="email" id="id_email" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password" id="id_password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="field">
                        <label>Confirm Password</label>
                        <div class="control">
                            <input type="password" name="confirm_password" id="id_confirm_password" class="input"
                                v-model="confirm_password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';

export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            confirm_password: '',
            errors: []
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (!this.username) {
                this.errors.push('The username is missing!')
            }

            if (!this.password) {
                this.errors.push('The password is too short!')
            }

            if (this.password !== this.confirm_password) {
                this.errors.push('The password are not matching!')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password,
                }

                axios
                    .post('/api/v1/users/', formData)
                    .then(response => {
                        toast({
                            message: 'Account was created.',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 200,
                            position: 'bottom-right'
                        })

                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        console.log(error)
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again! ')
                        }
                    })
            }
        }
    }
}
</script>