import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SearchView from '@/views/SearchView.vue'
import RecipeOverview from '@/views/RecipeOverview.vue'
import RecipeView from '@/views/RecipeView.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/recipe',
        name: 'recipe',
        component: RecipeView,
        meta: { transition: 'slide-left'}
    },
    {
        path: '/search',
        name: 'search',
        component: SearchView,
        meta: { transition: 'slide-left'}
    },
    {
        path: '/recipe-overview/:id',
        name: 'recipe-overview',
        component: RecipeOverview,
        meta: { transition: 'slide-left'}
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
