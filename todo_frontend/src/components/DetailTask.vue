<template>
  <div class="container">
    <h3>{{ task.name }}</h3>
    <em>{{ task.due_date}}</h3>
    <p>Created By: {{ task.user.username }}</p>
  </div>
</template>

<script>
import {apiDomain, getHeaders} from './config'

export default {
  data: function() {
    return {
      task: this.$http.get(apiDomain + '/tasks/' + this.$route.params.id + '/', {headers: getHeaders()}).then((response) => {
        this.task = response.data
      })
    }
  }
}
</script>
