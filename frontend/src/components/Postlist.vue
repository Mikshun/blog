<template>
  <div v-if="posts.length > 0">
    <h2><strong>Список Постов:</strong></h2>
    <transition-group name="post-list">
      <postitem
          v-for="post in posts"
          :post="post"
      />
    </transition-group>

  </div>
  <h2 v-else style="color: red">
    Постов еще нет
  </h2>
</template>

<script>
import Postitem from "@/components/Postitem.vue";

export default {
  components: {Postitem},
  props: {
    posts: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
.post-list-item {
  display: inline-block;
  margin-right: 10px;
}
.post-list-enter-active,
.post-list-leave-active {
  transition: all 1s ease;
}
.post-list-enter-from,
.post-list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>