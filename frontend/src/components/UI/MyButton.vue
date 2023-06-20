<template>
  <button class="btn">
  <slot></slot>
  </button>
</template>

<script>
export default {
  name: "my-button"
}
</script>

<style scoped>
.btn {
  margin: 10px;
  padding: 10px 15px;
  background-color: white;
  color: teal;
  border: 1px solid teal;
}
</style>