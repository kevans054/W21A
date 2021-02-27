<template>
    <div>
        <div class="row">
            <div class="col">
                <h1 class="text-info">Create your BlogBook Account</h1>
            </div>
        </div>
        <div class="container border border-dark rounded">
                <div class="row">
                    <div class="col"><br>
                        <input type="text" id="usernamefield" v-model="username" class="standard-input" placeholder="Username">
                    </div>
                </div>
                <div class="row">
                    <div class="col"><br>
                        <input type="password" id="passwordfield" v-model="password" class="standard-input" placeholder="Password">
                    </div>
                </div>
                <div class="row">
                    <div class="col"><br>
                        <button class="btn btn-outline-light btn-sm" @click="signupUser">Sign up</button>
                        <br><br>
                    </div>
                </div>
                
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import cookies from 'vue-cookies'
    export default {
        name: 'account',
        data() {
            return {
                userId: Number,
                username: "",
                password: "",
            }
        },
        methods: {
            signupUser: function() {
                axios.request({
                    method: "POST",
                    url: "http://localhost:5000/account",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    data: {
                        username: this.username,
                        password: this.password,
                    }
                }).then((response) => {
                    console.log(response)
                    // cookies.set('session', response.data.loginToken)
                    cookies.set('userid', response.data.userid)
                    cookies.set('username', response.data.username)
                    cookies.set('password', "password"),
                    this.$router.push("/Blog")
                }).catch((error) => {
                    console.log(error)
                })
            }
           
        }
    }
</script>

<style scoped>
.container {
        background-color: rgb(20, 131, 223);
    }
</style>
