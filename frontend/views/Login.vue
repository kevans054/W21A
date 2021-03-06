<template>
    <div>
        <div id="title"><br>
            <h1 class="text-info">Welcome to The BlogBook!</h1>
            <br>
        </div>
        <div class="container border border-dark rounded"><br>
            <!-- <form class="form-signin" @submit.prevent="loginUser"> -->
                <h2 class="form-signin-heading">Please sign in</h2><br>
                <input type="text" id="Username" v-model="Username" class="standard-input" placeholder="username"><br>
                <input type="password" id="Password" v-model="Password" class="standard-input" placeholder="password">
                <div><br>
                    <button  class="btn btn-outline-light btn-sm" @click="loginUser()">Sign in</button>
                    <br><br>
                </div>
                <div>
                    <button class="btn btn-outline-light btn-sm" @click="signup()">I don't have a User account</button>
                   
                </div>

        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import cookies from 'vue-cookies'

    export default {
        name: "Login",

        data() {
            return {
                username: "",
                password: "",
                loginStatus: "",
            }
        },

        methods: {
            
            loginUser: function() {
                this.loginStatus = "Loading",
                axios.request({
                    method: "POST",
                    url: "http://localhost:5000/login",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    data: {
                        username: this.Username,
                        password: this.Password,
                    }
                }).then((response) => {
                    this.loginStatus = response
                    console.log("Line 60 Loginvue " + response)
                    cookies.set('username', this.Username),
                    cookies.set('password', this.Password),
                    this.$router.push("/Blog")
                }).catch((error) => {
                    console.log(error)
                    this.loginStatus = "Error"
                })
            },
            signup: function(){
            this.$router.push("/Account")
            }
        }
    }
    
</script>

<style scoped>
    .container {
        background-color: rgb(20, 131, 223);
    }
</style>