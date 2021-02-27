<template>
    <div>
        <!-- add alert to confirm delete before -->
        <button class="btn btn-outline-light btn-sm" @click="deleteBlog()">Delete Blog</button>
    </div>
</template>

<script>
import axios from "axios"
// import cookies from "vue-cookies"
    export default {
        name: "blog-delete",

        props: {
            blogid: {
                type: Number,
                required: true
            }
        },
        methods: {
            deleteBlog: function() {
                axios.request({
                    url: "http://localhost:5000/blog",
                    method: "DELETE",
                    headers: {
                        "Content-Type": "application/json",
                    }, 
                    data: {
                        blogid: this.blogid
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