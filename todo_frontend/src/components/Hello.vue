<template>
  <div class="container">
    <h1>Hello {{ name }}</h1>
  </div>
</template>

<script>
export default {
  data () {
    let authUser = window.localStorage.getItem('authUser')
    authUser = JSON.parse(authUser)
    return {
      name: authUser.username
    }
  }
}
</script>
