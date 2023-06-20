<template>
  <div class="header-div">
    <my-button @click.stop="showDialog" class="toolbar_buttons" v-if="$store.state.isAuth === 'False'">
      Вход
    </my-button>
    <my-dialog v-model:show="dialogVisible">
      <loginform
          @create="createPost"
      ></loginform>
    </my-dialog>
    <my-button @click.stop="showRegister"  class="toolbar_buttons" v-if="$store.state.isAuth === 'False'">
      Регистрация
    </my-button>
    <my-dialog v-model:show="dialogRegister">
      <register
          @create="createPost"
      ></register>
    </my-dialog>
    <my-button  @click.stop="Logout" class="toolbar_buttons" v-if="$store.state.isAuth === 'True'">
      Выход
    </my-button>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";
import Postform from "@/components/Postform.vue";
import MyDialog from "@/components/UI/MyDialog.vue";
import Register from "@/components/Register.vue";
import Loginform from "@/components/Loginform.vue";
import store from "@/store";

export default {
  components: {Loginform, Register, Postform, MyButton, MyDialog},
  data() {
    return {
      dialogVisible: false,
      dialogRegister: false
    }
  },
  methods: {
    showDialog() {
      this.dialogVisible = true;
    },
    showRegister() {
      this.dialogRegister = true;
    },
    Logout() {
      store.state.token = null
      store.state.isAuth = 'False'
      store.state.isStaf = 'False'
    }
  }
}
</script>

<style scoped>
.header-div {
  margin: 15px;
  min-height: 100px;
  display: flex;
  justify-content: flex-end;
  background-color: aqua;
}

.div-link {
  margin-top: 30px;
  margin-right: 15px;
}

.toolbar_buttons {
  margin: 15px;
  min-width: 100px;
  min-height: 50px;
}

</style>