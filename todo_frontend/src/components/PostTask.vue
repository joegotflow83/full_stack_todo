<template>
  <div class="col-md-6">
    <div class="panel panel-default">
      <div class="panel-body">
        <form id="addTaskForm">
          <legend>Add New Task</legend><br />
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" class="form-control" v-model="name" id="taskName" placeholder="Enter Name" />
          </div>
          <br />
          <div class="form-group">
            <label for="date">Due Date</label>
            <input type="text" class="form-control" v-model="dueDate" id="dueDate" placeholder="Enter Due Date" />
          </div>
          <br />
          <button v-on:click="addTask()" type="submit" class="btn btn-primary">Save</button>
        <form>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import Vue from 'vue'
import VueResource from 'vue-resource'

import Task from './Task.vue'
import {apiDomain, getHeaders} from './config'

Vue.use(VueResource)

export default {
  data: function () {
    return {
      name: '',
      dueDate: ''
    }
  },
  events: {

  },
  methods: {
    addTask: function () {
      let authUser = window.localStorage.getItem('authUser')
      authUser = JSON.parse(authUser)
      let newTask = {
        name: this.name,
        due_date: this.dueDate
      }
      this.$http.post(apiDomain + '/users/' + authUser.id + '/tasks/', newTask, {headers: getHeaders()}).then(function (response) {
        console.log(response)
      })
    }
  },
}
</script>

<style>
  .completed {
    text-decoration: line-through;
  }
</style>
