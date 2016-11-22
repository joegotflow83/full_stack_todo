<template>
  <div id="searchTasks" class="row">
    <div class="col-md-6">
      <div class="panel panel-default"
        <div class="panel-body">
          <div>
              <legend>Search Tasks</legend>
              <div class="form-group">
                <label>Name</label>
                <input type="text" class="form-control" v-model="name" id="nameSearch" placeholder="Enter a task name" />
              </div>
              <br />
              <div class="form-group">
                <label>Date</label>
                <input type="text" class="form-control" v-model="date" id="dateSearch" placeholder="Enter a date" />
              </div>
              <button type="button" v-on:click="searchTasks()" class="btn btn-success">Search</button>
            <br /><br />
            {{ errors }}
            <div v-for="task in tasks">
              <h3 v-bind:class="{ completed : task.completed }">{{ task.name }}</h3>
              <h5 v-bind:class="{ completed : task.completed }">Due Date: <em>{{ task.due_date }}</em></h5>
              <span>
                <button type="button" id="editButton" v-if="!task.completed" class="btn btn-success">Edit</button>
                <button v-on:click="deleteTask(task.id, $index)" type="button" class="btn btn-danger">Delete</button>
                <button v-on:click="completeTask(task)" v-if="!task.completed" type="button" class="btn btn-info">Completed</button>
              </span>
            </div>
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
    return {
      tasks: '',
      name: '',
      date: '',
      errors: ''
    }
  },
  methods: {
    searchTasks: function () {
      this.errors = ''
      if (this.date == "") {
        this.$http.get(apiDomain + '/tasks/search?name=' + this.name, {headers: getHeaders()}).then(function (response) {
          if (response.data.length == 0) {
            this.errors = "No tasks were found."
          } else {
            this.tasks = response.data
          }
        })
      } else if (this.name == "") {
          this.$http.get(apiDomain + '/tasks/search?date=' + this.date, {headers: getHeaders()}).then(function (response) {
            this.tasks = response.data
            console.log(response)
        })
      } else if (this.name && this.date) {
        this.$http.get(apiDomain + '/tasks/search?name=' + this.name + '&date=' + this.date, {headers: getHeaders()}).then(function (response) {
          this.tasks = response.data
          console.log(response)
        })
      }
    },
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
      this.$http.delete(apiDomain + '/users/' + authUser.id + '/tasks/' + id + '/', {headers: getHeaders()}).then(function (response) {
        console.log(response)
      })
      this.tasks.splice(index, 1)
    }
  }
}
</script>
