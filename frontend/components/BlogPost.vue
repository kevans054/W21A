<template>
    <div class="container border border-dark rounded">
        <div class="row">
            <div class="col">
                <div v-for="blog in blogs" :key="blog.blogid">
                    <textarea id="blogbox" class="col" v-model="blog.blog_content"></textarea>
                    <blog-delete :blogid="blog.blogid"></blog-delete>
                    <button class="btn btn-outline-light" type="button" @click="editBlog()">Update</button>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col"><br>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import cookies from 'vue-cookies'
import BlogDelete from './BlogDelete.vue'
// import BlogEdit from './BlogEdit.vue'

    export default {
        name: 'blog-post',
            components: {
                BlogDelete,
                // BlogEdit
            },
            
        data(){
            return {
                blogs: [],
                userid: cookies.get("userid"),
                blogid: cookies.get("blogid")
            }
        },
        
        mounted: function() {
            this.getBlogs()
        },

        methods: {
            getBlogs: function() {
                axios.request({
                    method: "GET",
                    url: "http://localhost:5000/blog",
                   
                }).then((response) => {
                    this.blogs = response.data
                    console.log(response)
                    cookies.set('blogid', response.data.blogid)
 
                }).catch((error) => {
                    console.log(error)
                    this.loginStatus = "Error"
                })
            },
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
        }
    }
</script>

<style scoped>
     p {
         font-size: 12px;
    }
    .container {
        background-color: rgb(20, 131, 223);
    }
</style>