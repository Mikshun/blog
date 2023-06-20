import Main from "@/pages/Main.vue";
import {createRouter, createWebHistory} from "vue-router";
import PostPage from "@/pages/PostPage.vue";
import Details from "@/pages/Details.vue";


const routes = [
    {
        path: '/',
        component: PostPage
    },
    {
        path: '/:id',
        component: Details
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URl)
})

export default router;