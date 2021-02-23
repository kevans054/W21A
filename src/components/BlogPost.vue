<template>
    <div class="container border border-dark rounded">
        <div class="row">
            <div class="col">
                <h3 class=text-white> UserName: </h3>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <textarea id="blogbox" class="col" v-model="blogContent" placeholder="Blog Content goes here"></textarea>
            </div>
        </div>
        <div class="row">
            <div class="col"><br>
                <h6>Blog Object:</h6>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <blog-delete class="col" v-if="isOwned" :blogId="blogObject.blogId"></blog-delete>
            </div>
            <div class="col">
                <blog-edit class="col" @update-blog="updateBlog" v-if="isOwned" :blogId="blogObject.blogId"></blog-edit>
                <br>
            </div>
            <div class="col">
            </div>
            <div class="col">
            </div>
        </div>
        <div class="row">
            <div class="col"><br>
                <div>
                    <button class="btn btn-outline-light btn-sm" @click="reloadPage()">Refresh Blogs</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import BlogDelete from './BlogDelete.vue'
import BlogEdit from './BlogEdit.vue'
import cookies from 'vue-cookies'
// import axios from 'axios'
    export default {
        name: 'blog-display',
        components: {
            BlogDelete,
            BlogEdit
        },
        props: {
            BlogObject: {
                type: Object,
                required: true,
                },
            },
        data() {
            return {
                isOwned: cookies.get('userId') == this.BlogObject.userId,
                content: this.BlogObject.content,
                show: false
            }
        },
        methods: {
            reloadPage() {
                window.location.reload()
            },
            updateBlog(newContent) {
                this.content = newContent;
            },
            addComment(newComment) {
                this.comment = newComment;
            },
        },
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