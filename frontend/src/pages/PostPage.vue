<template>
  <div>
    <h1>Страница с постами</h1>
    <my-button @click.stop="showDialog" v-if="$store.state.isStaf === 'True'">
      Создать пост
    </my-button>
    <my-button @click.stop="UpdatePage">
      Подгрузить посты
    </my-button>
    <my-dialog v-model:show="dialogVisible">
      <postform
          @create="createPost"
      ></postform>
    </my-dialog>
    <postlist
        :posts="posts"
        v-if="!isPostLoading"
    ></postlist>
    <div v-else>Идет загрузка...</div>

  </div>
</template>

<script>
import Postform from "@/components/Postform.vue";
import Postlist from "@/components/Postlist.vue";
import MyDialog from "@/components/UI/MyDialog.vue";
import MyButton from "@/components/UI/MyButton.vue";
import {mapState, mapGetters, mapActions, mapMutations} from 'vuex';
import {ref} from 'vue';
import {usePosts} from "@/hooks/usePosts";
import Toolbar from "@/components/toolbar.vue";
import store from "@/store";
import axios from "axios";
export default {
  components: {
    Toolbar,
    MyButton,
    MyDialog,
    Postlist, Postform
  },
  data() {
    return {
      dialogVisible: false
    }
  },
  methods: {
    showDialog() {
      this.dialogVisible = true;
    },
    UpdatePage() {
      const response = axios.get('http://127.0.0.1:8000/api/', {
        headers: {
          Authorization: store.state.token
        }
      }).then(response => {
        store.state.isAuth = response.headers.get('auth')
        store.state.isStaf = response.headers.get('staff')
        this.posts = response.data
      });
      console.log(response)
    }
  },

  setup(props) {
    const {posts, isPostLoading, isStaf, isAuth} = usePosts(store.state.token);
    return {
      posts,
      isPostLoading,
      isStaf,
      isAuth
    }
  }
}
</script>

<style>

</style>