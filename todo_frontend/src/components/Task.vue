<template>
    <div id="currentTasks" class="col-md-6">
      <div class="panel panel-default">
        <div class="panel-body">
          <legend>Current Tasks</legend><br />
            <div v-if="tasks.length > 0">
              <div v-for="task in tasks" class="task conatiner">
                <h3 v-bind:class="{ completed : task.completed }">{{ task.name }}</h3>
                <h5 v-bind:class="{ completed : task.completed }">Due Date: <em>{{ task.due_date }}</em></h5>
                <span>
                  <button type="button" id="editButton" v-if="!task.completed" class="btn btn-success">Edit</button>
                  <button v-on:click="deleteTask(task.id, $index)" type="button" class="btn btn-danger">Delete</button>
                  <button v-on:click="completeTask(task)" v-if="!task.completed" type="button" class="btn btn-info">Completed</button>
                </span>
              </div>
            </div>
            <div v-else>
            <p>You do not have any tasks.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import Vue from 'vue'
import VueResource from 'vue-resource'

import {apiDomain, getHeaders} from './config'

Vue.use(VueResource)

export default {
  data: function () {
    let authUser = window.localStorage.getItem('authUser')
    authUser = JSON.parse(authUser)
    return {
      tasks: this.$http.get(apiDomain + '/users/' + authUser.id + '/tasks/', {headers: getHeaders()}).then(function (response) {
        this.tasks = response.data
      })
    }
  },
  methods: {
    completeTask: function (task) {
      task.completed = true
      let authUser = window.localStorage.getItem('authUser')
      authUser = JSON.parse(authUser)
      this.$http.put(apiDomain + '/users/' + authUser.id + '/tasks/' + task.id + '/', task, {headers: getHeaders()}).then(function (response) {
        console.log(response)
      })
    },
    deleteTask: function (id, index) {
      let authUser = window.localStorage.getItem('authUser')
      authUser = JSON.parse(authUser)
      this.$http.delete(apiDomain  + '/users/' + authUser.id + '/tasks/' + id + '/', {headers: getHeaders()}).then(function (response) {
        console.log(response)
      })
      this.tasks.splice(index, 1)
    }
  },
}
</script>
