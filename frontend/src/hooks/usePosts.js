import axios from "axios";
import {onMounted, ref} from 'vue';
import store from "@/store";

export function usePosts(token) {
    const posts = ref([])
    const isAuth = ref(false)
    const isStaf = ref(false)
    const isPostLoading = ref(true)
    const fetching = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/', {
                params: {
                    Authorization: token
                }
            });
            posts.value = response.data
            isAuth.value = response.headers.get('auth')
            isStaf.value = response.headers['staff']
            store.state.isAuth = response.headers.get('auth')
            store.state.isStaf = response.headers.get('staff')
            console.log(response)
        } catch (e) {
            console.log(e)
        } finally {
            isPostLoading.value = false;
        }
    }

    onMounted(fetching)
    return {
        posts, isAuth, isStaf, isPostLoading
    }

}