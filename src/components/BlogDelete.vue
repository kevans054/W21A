<template>
    <div>
        <!-- add alert to confirm delete before -->
        <button class="btn btn-outline-light btn-sm" @click="deleteBlog()">Delete Blog</button>
    </div>
</template>

<script>
import axios from "axios"
import cookies from "vue-cookies"
    export default {
        name: "blog-delete",
        
        props: {
            blogId: {
                type: Number,
                required: true
            }
        },
        methods: {
            deleteBlog: function() {
                axios.request({
                    url: "http://localhost:8080/blog",
                    method: "DELETE",
                    headers: {
                        "Content-Type": "application/json",
                        "X-Api-Key": "p3JJq3WhdMwT98hN9PTaYDE1lr2p0qKOaLfIdjyDxiorc"
                    }, 
                    data: {
                        loginToken: cookies.get("session"),
                        blogId: this.blogId
                    },
                }).then((response) => {
                    console.log(response)
                    window.location.reload()
                }).catch((error) => {
                    console.log(error)
                })
            }
        },
    }
</script>

<style scoped>
</style>