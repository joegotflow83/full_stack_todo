<template>
  <div id="signupPage" class="container">
    <div class="panel panel-default">
      <div class="panel-body">
          <form v-on:submit.prevent="signup()" id="signupForm">
            <legend><center>Signup</center></legend><br />
            <div class="form-group">
              <label for="username">Username</label>
              <input type="text" class="form-control" v-model="username" id="username" placeholder="Enter Username" />
            </div>
              <br />
            <div class="form-group">
              <label for="date">Password</label>
              <input type="password" class="form-control" v-model="password" id="password" placeholder="Enter Password" />
            </div>
            <div class="form-group">
              <label for="date">Confirm Password</label>
              <input type="password" class="form-control" v-model="confirmPassword" id="password" placeholder="Confirm Password" />
            </div>
            <div v-if="errors" class="errors">{{ errors }}</div>
            <br />
            <button type="submit" class="btn btn-success">Sign Up</button>
          <form>
      </div>
    </div>
  </div>
</template>

<script>
import {signupUrl, getHeaders} from './config'

export default {
  data: function () {
    return {
      username: '',
      password: '',
      confirmPassword: '',
      errors: ''
    }
  },
  methods: {
    signup: function () {
      const newUser = {
        username: this.username,
        password: this.password,
        confirm_password: this.confirmPassword
      }
      this.$http.post(signupUrl, newUser).then((response) => {
        if (response.status === 200) {
          console.log(response.data)
          this.$router.push({ name: 'login' })
        }
      }, (response) => {
          if (response.data.username) {
            this.errors = response.data.username[0]
            console.log(response.data)
          } else if (response.data.non_field_errors) {
            this.errors = response.data.non_field_errors[0]
            console.log(response.data)
          } else {
            console.log(response.data)
          }
      })
    }
  }
}
</script>

<style>
  .errors {
    color: red;
  }
</style>
