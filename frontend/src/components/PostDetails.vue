<template>
  <div class="post">
    <div><strong>Заголовок:</strong> {{post.title}}</div>
    <div><strong>Автор:</strong> {{post.author}}</div>
    <div><strong>Описание:</strong> {{ post.description }}</div>
  </div>
</template>

<script>
export default {
  props: {
    post: {
      type: Object,
      required: true,
    }
  }

}
</script>

<style  scoped>
.post {
  padding: 10px;
  border: 2px solid teal;
  margin-top: 15px;
}
</style>