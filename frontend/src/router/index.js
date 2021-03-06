import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Blog from '../views/Blog.vue'
import Account from '../views/Account.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/Account',
    name: 'Account',
    component: Account
  },
  {
    path: '/Blog',
    name: 'Blog',
    component: Blog
  },
]

const router = new VueRouter({
  routes
})

export default router
