<template>
<div id="login" class="container text-center">
   <br /><br />
  <div class="panel panel-default">
    <div class="panel-body">
      <form v-on:submit.prevent="login()" id="loginForm">
        <legend><center>Login</center></legend><br />
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" class="form-control" v-model="username" id="username" placeholder="Enter Username" />
        </div>
          <br />
          <div class="form-group">
          <label for="date">Password</label>
          <input type="password" class="form-control" v-model="password" id="password" placeholder="Enter Password" />
        </div>
        <br />
        <button type="submit" class="btn btn-success">Login</button>
        <div v-for="error in errors">
          {{ error }}
        </div>
      <form>
    </div>
  </div>
</div>
</template>

<script>
import {mapState} from 'vuex'

import {apiDomain, loginUrl, userUrl, getHeaders} from './config'

export default {
  data: function () {
    return {
      user: {
        username: '',
        password: '',
        errors: []
      }
    }
  },
  methods: {
    login: function () {
      const user = {
        username: this.username,
        password: this.password
      }
      let authUser = {}
      this.$http.post(loginUrl, user).then(function (response) {
        if (response.status === 200) {
          authUser.id = response.data.user_id
          authUser.username = response.data.username
          authUser.token = response.data.token
          window.localStorage.setItem('authUser', JSON.stringify(authUser))
          console.log(authUser)
          this.$http.get(userUrl + authUser.id + "/", {headers: getHeaders()}
          ).then(function (response) {
            console.log('user object', response.data)
          })
          this.$store.dispatch('setUserObject', authUser)
          this.$router.push({ name: 'home'})
        } else {
            this.errors = response.body
        }
      })
    }
  },
  computed: mapState({
    userStore: state => state.userStore
  })
}
</script>

<style>
</style>
