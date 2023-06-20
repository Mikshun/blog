<template>
  <div v-if="comments.length > 0">
    <h2><strong>Список Комментариев:</strong></h2>
    <transition-group name="comment-list">
      <commentitem
          v-for="comment in comments"
          :comment="comment"
      />
    </transition-group>

  </div>
  <h2 v-else style="color: red">
    Комментариев еще нет
  </h2>
</template>

<script>
import Commentitem from "@/components/Commentitem.vue";

export default {
  components: {Commentitem},
  props: {
    comments: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
.comment-list-item {
  display: inline-block;
  margin-right: 10px;
}
.comment-list-enter-active,
.comment-list-leave-active {
  transition: all 1s ease;
}
.comment-list-enter-from,
.comment-list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>