<template>
    <div class="container border border-dark rounded">
        <div class="row">
            <div class="col">
                <h4 class="text-white">BlogBook</h4>
            </div>
        </div>
        <div class="row">
            <textarea id="blogbox" class="col" v-model="blogContent" placeholder="Enter your blog post here"></textarea>
        </div>
        <div class="row">
            <div class="col"><br>
                <button class="btn btn-outline-light btn-sm" @click="postBlog()">Post</button>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import cookies from 'vue-cookies'
    export default {
        name: 'blog-form',
        data() {
            return {
                blogContent: "",
                blogStatus: "Post your blog here!",
                // userid: cookies.get("userid")
                }
            },

        methods: {
            postBlog: function() {
                this.blogStatus = "Sending!"
                axios.request({
                    url: "http://localhost:8080/Blog",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    method: "POST",
                    data: {
                        content: this.blogContent,
                        userid: cookies.get('userid')
                    }
                }).then((response) => {
                    console.log(response)
                    this.blogStatus = "Posted!"
                    
                }).catch((error) => {
                        console.log(error)
                        this.blogStatus = "Failed to post!"
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