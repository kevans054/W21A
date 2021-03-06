<template>
    <div>
        <button class="btn btn-outline-light" type="button" @click="editBlog()">Update</button>
    </div>
</template>

<script>
import axios from 'axios'
import cookies from 'vue-cookies'
    export default {
        name: 'blog-edit',
        data() {
            return {
                show: false,
            }
        },
        props: {
            blogid: {
                type: Number,
                required: true 
            },
            blog_content: {
                type: String,
                required: true
            }
        },
        methods: {
            editBlog: function() {
                axios.request({
                    url: "http://localhost:5000/blog",
                    method: "PATCH",
                    headers: {
                        "Content-Type": "application/json",
                    }, 
                    data: {
                        loginToken: cookies.get("session"),
                        blogid: this.blogid,
                        blog_content: this.blog_content
                    },
                     
                }).then((response) => {
                    console.log(response)
                }).catch((error) => {
                    console.log(error)
                })
            }
        },
    }
</script>

<style scoped>
</style>