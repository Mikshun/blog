<template>
  <div class="comment">
    <div><strong>Автор:</strong> {{comment.author}}</div>
    <div><strong>Техт:</strong> {{comment.text}}</div>
  </div>
</template>

<script>
export default {
  props: {
    comment: {
      type: Object,
      required: true,
    }
  }

}
</script>

<style  scoped>
.comment {
  padding: 10px;
  border: 2px solid aqua;
  margin-top: 15px;
}
</style>