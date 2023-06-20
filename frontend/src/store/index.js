import {createStore} from "vuex";

export default createStore({
    state: {
        isAuth: false,
        isStaff: false,
        token: null,
        user: null,
    }
})