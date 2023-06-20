<template>
  <toolbar></toolbar>
  <div  class="app">
  <router-view></router-view>
  </div>
</template>

<script>
import Toolbar from "@/components/toolbar.vue";

export default {
  components: {Toolbar}

}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;

}

.app {
  padding: 20px;
}
</style>