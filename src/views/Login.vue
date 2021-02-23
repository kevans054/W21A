<template>
    <div id="account">
        <div id="title"><br>
            <h1 class="text-info">Welcome to The BlogBook!</h1>
            <br>
        </div>
        <div class="container border border-dark rounded"><br>
            <form class="form-signin" @submit.prevent="loginUser">
                <h2 class="form-signin-heading">Please sign in</h2><br>
                <input type="username" id="userName" class="form-control" v-model="username" placeholder="username"><br>
                <input type="password" id="inputPassword" class="form-control" v-model="password" placeholder="password">
                <div><br>
                    <button  class="btn btn-outline-light btn-sm" type="submit">Sign in</button>
                    <br><br>
                </div>
                <div>
                    <button class="btn btn-outline-light btn-sm" @click="show = !show">I don't have a User account</button>
                    <div v-if="show">
                        <accountform></accountform>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import cookies from 'vue-cookies'
    import accountform from '../components/Account.vue'
    export default {
        name: "Login",
    
        components: {
        accountform
        },
        data() {
            return {
                username: "",
                password: "",
                loginStatus: "",
                show: false
            }
        },
        methods: {
            loginUser: function() {
                this.loginStatus = "Loading",
                
                axios.request({
                    method: "POST",
                    url: "http://localhost:5000/login",
                    headers: {
                        "Content-Type":"application/json",
                    },
                    data: {
                        username: this.username,
                        password: this.password,
                        loginStatus: this.loginStatus
                    }
                }).then((response) => {
                    console.log(response)
                    this.loginStatus = "Success"
                    cookies.set('userId', response.data.userId)
                    cookies.set('password', "password"),
                    this.$router.push("/Blog")
                }).catch((error) => {
                    console.log(error)
                    this.loginStatus = "Error"
                    // alert("No account with that email or password found. Please create your account.")
                    // this.$router.push({ name: 'SignupForm' })
                })
            },
            // signup: function(){
            // this.$router.push({ name: 'Account' })
            // }
        }
    }
    
</script>

<style scoped>
    .container {
        background-color: rgb(20, 131, 223);
    }
</style>