<template>
  <div class="container">
    <h3>Select a user to follow</h3>
    <br />
    <div v-for="user in users">
      <span><p v-if="user.username !== userStore.authUser.username">{{ user.username }}&nbsp;&nbsp;<button v-on:click="addFriend(user.id)" class="btn btn-primary">Add Friend</button></p></span>
    </div>
  </div>
</template>

<script>
import {apiDomain, getHeaders} from './config'
import {mapState} from 'vuex'

export default {
  data: function() {
    return {
      users: this.$http.get(apiDomain + '/users/', {headers: getHeaders()}).then((response) => {
        this.users = response.data
      })
    }
  },
  methods: {
    addFriend: function (pk) {
      this.$http.post(apiDomain + '/users/' + pk + '/add/', {headers: getHeaders()}).then((response) => {
        console.log(response)
      })
    }
  },
  computed: mapState({
    userStore: state => state.userStore
  })
}
</script>
