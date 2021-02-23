<template>
    <div>
        <button class="btn btn-outline-light btn-sm" type="button" @click="show = !show">Edit Blog</button>
        <div v-if="show">
            <textarea v-model="blogContent"></textarea>
            <button class="btn btn-outline-light" type="button" @click="editBlog()">Submit</button>
        </div>
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
                blogContent: ""
            }
        },
        props: {
            blogId: {
                type: Number,
                required: true 
            },
        },
        methods: {
            editBlog: function() {
                axios.request({
                    url: "http://localhost:8080/Blog",
                    method: "PATCH",
                    headers: {
                        "Content-Type": "application/json",
                    }, 
                    data: {
                        loginToken: cookies.get("session"),
                        blogId: this.blogId,
                        content: this.blogContent
                    },
                     
                }).then((response) => {
                    console.log(response)
                    this.$emit('update-blog', this.blogContent)
                    this.show = false;
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