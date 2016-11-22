import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import store from './store'

import Signup from './components/Signup.vue'
import Login from './components/Login.vue'
import Hello from './components/Hello.vue'
import Task from './components/Task.vue'
import PostTask from './components/PostTask.vue'
import Search from './components/Search.vue'
import App from './App.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/signup', component: Signup, name: 'signup' },
  { path: '/login', component: Login, name: 'login' },
  { path: '/home', component: Hello, name: 'home', meta: { requiresAuth: true }},
  { path: '/tasks', component: Task, name: 'tasks', meta: { requiresAuth: true }},
  { path: '/create/task', component: PostTask, name: 'createTask', meta: { requiresAuth: true }},
  { path: '/search/tasks', component: Search, name: 'searchTasks', meta: { requiresAuth: true }},
]

const router = new VueRouter({
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    const authUser = JSON.parse(window.localStorage.getItem('authUser'))
    if (authUser && authUser.token) {
      next()
    } else {
      next({ name: 'login' })
    }
  }
  next()
})

new Vue({
  router, store,
  render: h => h(App)
}).$mount("#app")
