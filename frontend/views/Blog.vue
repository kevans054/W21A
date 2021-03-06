<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h1 class="text-info">Welcome to BlogBook! (Blog.vue)</h1>
            </div>
        </div>
        <div>
            <div class="row">
                <div class="col">
                    <blog-post></blog-post>
                </div>
            </div>
        </div>
        <div>
            <div class="row">
                <div class="col">
                    <blog-form></blog-form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"
import cookies from 'vue-cookies'
import BlogPost from '../components/BlogPost.vue'
import BlogForm from '../components/BlogForm.vue'

    export default {
        name: "blog",
        components: {
            BlogPost,
            BlogForm
           },
        data() {
            return {
                // users:[],
                loginStatus: "",
                userid: "",
                username: cookies.get('username'),
                password: cookies.get('password'),
            }
        },

        mounted: function() {
            this.getUser()
        },
        methods: {
            getUser: function(){
                axios.request({
                    method: "GET",
                    url: "http://localhost:5000/blog",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    data: {
                        username: this.username,
                        password: this.password,
                    }
                }).then((response) => {
                    console.log("The data returned: " + response.data)
                   this.userid = response.data.userid
                }).catch((error) => {
                    console.log(error)
                    this.loginStatus = "Error"
                })
            },
        }
    }
</script>

<style scoped>
   .container {
        padding: 20px;
        margin-top: auto;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: auto;
    }
</style>
