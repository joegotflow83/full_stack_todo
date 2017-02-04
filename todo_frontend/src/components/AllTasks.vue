<template>
  <div class="container">
    <h2>All Tasks</h2>
    <br />
    <div v-for="task in tasks">
      <h4><router-link :to="'/tasks/' + task.id">{{ task.name }}</router-link></a></h4>
      <em>{{ task.due_date }}</em>
      <br /><br />
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import VueResource from 'vue-resource'

import {apiDomain, getHeaders} from './config'

Vue.use(VueResource)

export default {
  data: function() {
    return {
      tasks: this.$http.get(apiDomain + '/tasks/', {headers: getHeaders()}).then((response) => {
        this.tasks = response.data
      })
    }
  }
}
</script>
