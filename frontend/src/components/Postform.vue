<template>
  <form @submit.prevent>
    <h1 v-if="post.succes === true">Пост успешно создан</h1>
    <h4>Создание поста</h4>
    <my-input
        v-focus
        v-model="post.title"
        type="text"
        placeholder="Заголовок"
    />
    <my-input
        v-model="post.body"
        type="text"
        placeholder="Описание"
    />
    <my-button
        style="align-self: flex-end; margin-top: 15px"
        @click="createPost"
    >
      Создать
    </my-button>
  </form>
</template>

<script>
import axios from "axios";
import store from "@/store";

export default {
  data() {
    return {
      post: {
        title: '',
        body: '',
        succes: false
      }
    }
  },
  methods: {
    createPost() {
      try {
        const response = axios.post('http://127.0.0.1:8000/api/',{
          author: store.state.user,
          title: this.post.title,
          description: this.post.body
        } ,{headers: {Authorization: store.state.token}})
        console.log(response)
        this.post.succes = true
      } catch (e) {
        console.log(e)

      }
      finally {
        this.post.title = ''
        this.post.body = ''
      }
    }
  },
}
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}

</style>