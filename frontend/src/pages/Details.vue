<template>
  <div>
    <h1 @click="$router.push(`/`)">Детали Поста {{ $route.params.id }}</h1>
    <my-button @click.stop="showDialog" v-if="$store.state.isAuth === 'True'">
      Создать Комментарий
    </my-button>
    <my-dialog v-model:show="dialogVisible">
      <commentform>
        @create="createComment"
      </commentform>
    </my-dialog>
    <my-button @click.stop="UpdatePage">
      Подгрузить комментарии
    </my-button>
    <post-details
        :post="posts[$route.params.id-1]"
        v-if="!isPostLoading"
    ></post-details>
    <commentlist
        :comments="comments"
        v-if="!isCommentLoading"
    ></commentlist>
    <div v-else>Идет загрузка...</div>

  </div>
</template>

<script>
import Postform from "@/components/Postform.vue";
import Postlist from "@/components/Postlist.vue";
import MyDialog from "@/components/UI/MyDialog.vue";
import MyButton from "@/components/UI/MyButton.vue";
import {usePosts} from "@/hooks/usePosts";
import PostDetails from "@/components/PostDetails.vue";
import Commentlist from "@/components/Commentlist.vue";
import {useComments} from "@/hooks/useComments";
import axios from "axios";
import store from "@/store";
import Commentform from "@/components/Commentform.vue";
export default {
  components: {
    Commentlist,
    PostDetails,
    MyButton,
    MyDialog,
    Postlist, Postform,
    Commentform
  },
  data() {
    return {
      dialogVisible: false,
    }
  },
  methods: {
    UpdatePage() {
      const response = axios.get('http://127.0.0.1:8000/api/comment/', {
        headers: {
          Authorization: store.state.token
        },
        params: {
          post: document.URL.slice(-1)
        }
      }).then(response => {
        store.state.isAuth = response.headers.get('auth')
        store.state.isStaf = response.headers.get('staff')
        this.comments = response.data
      });
      console.log(response)
    },
    showDialog() {
      this.dialogVisible = true;
    }
  },
  setup(props) {
    const {posts, isPostLoading, isStaf, isAuth} = usePosts();
    const {comments, isCommentLoading} = useComments(document.URL.slice(-1));

    return {
      posts,
      isPostLoading,
      isStaf,
      isAuth,
      comments,
      isCommentLoading
    }
  }
}
</script>

<style>

</style>