<template>
  <form @submit.prevent>
    <h1 v-if="user.succes">Успешный Вход</h1>
    <h3>Вход</h3>
    <my-input
        v-focus
        v-model="user.login"
        type="text"
        placeholder="Логин"
    />
    <my-input
        v-model="user.password"
        type="password"
        placeholder="Пароль"
    />
    <my-button
        @click="loginUser"
        style="align-self: center"
    >Вход</my-button>
  </form>
</template>

<script>

import MyInput from "@/components/UI/MyInput.vue";
import axios from "axios";
import store from "@/store";
import {usePosts} from "@/hooks/usePosts";

export default {
  components: {MyInput},

  data () {
    return {
      user: {
        login: '',
        password: '',
        succes: false
      }
    }
  },
  methods: {
    loginUser() {
      try {
        const response = axios.post('http://127.0.0.1:8000/api/auth/token/login',
            {
              "username": this.user.login,
              "password": this.user.password
            }).then(response => {
              store.state.token ='token ' + response.data.auth_token
        })
        this.user.succes = true

        console.log(response)
      } catch (e) {
        console.log(e)

      }
      finally {
        store.state.user = this.user.login
        this.user.login = ''
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