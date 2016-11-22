<template>
  <div id="app">
    <navbar></navbar>
    <router-view></router-view>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import Navbar from './components/Navbar.vue'

export default {
  components: {
    Navbar
  },
  computed: mapState({
    userStore: state => state.userStore
  }),
  created () {
    console.log('I was created')
    const userObj = JSON.parse(window.localStorage.getItem('authUser'))
    this.$store.dispatch('setUserObject', userObj)
  }
}
</script>
