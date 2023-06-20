import axios from "axios";
import {onMounted, ref} from 'vue';

export function useComments(id) {
    const comments = ref([])
    const isCommentLoading = ref(true)
    const fetching = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/comment', {
                params: {
                    post: id
                }
            });
            comments.value = response.data
        } catch (e) {
            console.log(e)
        } finally {
            isCommentLoading.value = false;
        }
    }

    onMounted(fetching)
    return {
        comments, isCommentLoading
    }

}