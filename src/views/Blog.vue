<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h1 class="text-info">Welcome to BlogBook!</h1>
            </div>
        </div>
        <div class="container border border-dark rounded">
            <div class="row">
            </div>
            <div class="row">
                <div class="col"><br>
                    <h2 class="text-dark">Create a new blog post here:</h2>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <blog-form></blog-form>
                    <br>
                </div>
            </div>
        </div>
        <div class="container border border-dark rounded">
            <div class="row">
            </div>
            <div class="row">
                <div class="col"><br>
                    <h2 class="text-dark">View Blog Postings here:</h2>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <blog-post></blog-post>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"
import cookies from 'vue-cookies'
import BlogForm from '../components/BlogForm.vue'
import BlogPost from '../components/BlogPost.vue'

    export default {
        name: "blog",
        data() {
            return {
                blogs: [],
                userId: cookies.get('userId'),
                show: false
            }
        },
        components: {
            BlogForm,
            BlogPost
           },

        mounted: function() {
            this.getBlogs();
        },
        methods: {

            getBlogs: function() {
                axios.request({
                    url: "/Blog",
                    method: "GET",
                     headers: {
                        "Content-Type": "application/json",

                    },
                }).then((response) => {
                    console.log(response)
                    this.blogs = response.data
                }).catch((error) => {
                    console.log(error)
                })
            }
        },
       
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
