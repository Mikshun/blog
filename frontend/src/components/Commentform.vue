<template>
  <form @submit.prevent>
    <h1 v-if="comment.succes === true">Комментарий успешно создан</h1>
    <h4>Создание Комментария</h4>
    <my-input
        v-model="comment.body"
        type="text"
        placeholder="Текст"
    />
    <my-button
        style="align-self: flex-end; margin-top: 15px"
        @click="createComment"
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
      comment: {
        body: '',
        succes: false
      }
    }
  },
  methods: {
    createComment() {
      try {
        const response = axios.post('http://127.0.0.1:8000/api/comment/',{
          author: store.state.user,
          text: this.comment.body,
          post: document.URL.slice(-1)
        } ,{headers: {Authorization: store.state.token}})
        console.log(response)
        this.comment.succes = true
      } catch (e) {
        console.log(e)

      }
      finally {
        this.comment.body = ''
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