<template>
  <form @submit.prevent>
    <h1 v-if="user.succes">Успешно Зарегестрирован</h1>
    <h3>Регистрация</h3>
    <my-input
        v-focus
        v-model="user.username"
        type="text"
        placeholder="Логин"
    />
    <my-input
        v-model="user.password"
        type="password"
        placeholder="Пароль"
    />
    <my-button
        @click="createUser"
        style="align-self: center"
    >Регистрация</my-button>
  </form>
</template>

<script>

import MyInput from "@/components/UI/MyInput.vue";
import axios from "axios";

export default {
  components: {MyInput},

  data() {
    return {
      user: {
        username: '',
        password: '',
        succes: false,
      }
    }
  },
  methods: {
    createUser() {
      try {
        const response = axios.post('http://127.0.0.1:8000/api/auth/users/',
            {
              "username": this.user.username,
              "password": this.user.password
            })
        console.log(response)
        this.user.succes = true
      } catch (e) {
        console.log(e)

      }
      finally {
        this.user.username = ''
        this.user.password = ''
      }
    }
  }
}
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}


</style>