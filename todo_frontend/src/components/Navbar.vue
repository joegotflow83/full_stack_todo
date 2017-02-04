<template>
  <ul class="nav nav-tabs">
    <li v-if="userStore.authUser !== null && userStore.authUser.token" role="presentation"><router-link :to="{ name: 'tasks' }">Tasks</router-link></li>
    <li v-if="userStore.authUser !== null && userStore.authUser.token" role="presentation"><router-link :to="{ name: 'createTask' }">Create</router-link></li>
    <li v-if="userStore.authUser !== null && userStore.authUser.token" role="presentation"><router-link :to="{ name: 'home' }">Home</router-link></li>
    <li v-if="userStore.authUser !== null && userStore.authUser.token" role="presentation"><router-link :to="{ name: 'searchTasks' }">Search</router-link></li>
    <li v-if="userStore.authUser !== null && userStore.authUser.token" role="presentation"><router-link :to="{ name: 'allTasks' }">All Tasks</router-link></li>
    <li v-if="userStore.authUser !== null && userStore.authUser.token" role="presentation"><router-link :to="{ name: 'users' }">Search Users</router-link></li>
    <li v-if="userStore.authUser === null" role="presentation"><router-link :to="{ name: 'login' }">Login</router-link></li>
    <li><a v-if="userStore.authUser !== null && userStore.authUser.token" v-on:click="logout()" role="presentation">Logout</a></li>
    <li v-if="userStore.authUser === null" role="presentation"><router-link :to="{ name: 'signup' }">Signup</router-link></li>
  </ul>
</template>

<script>
import {mapState} from 'vuex'

export default {
  methods: {
    logout: function () {
      this.$store.dispatch('clearAuthUser')
      window.localStorage.removeItem('authUser')
      this.$router.push({ name: 'login' })
    }
  },
  computed: mapState({
    userStore: state => state.userStore
  })
}
</script>
