import { createRouter, createWebHistory } from 'vue-router'
import Register from '../components/Register.vue'
import Login from '../components/Login.vue'
import Menu from '../components/Menu.vue'
import Bots from '../components/Bots.vue'
import MenuInfo from '../components/Menu-Info.vue'
import Maker from '../components/Maker.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },  
    {
      path: '/menu',
      name: 'Menu',
      component: Menu
    },   
    {
      path: '/menu/bots',
      name: 'Bots',
      component: Bots
    }, 
    {
      path: '/menu/menu-info',
      name: 'Menu-Info',
      component: MenuInfo
    },
    {
      path: '/menu/maker',
      name: 'Maker',
      component: Maker
    },
  ]
})

export default router
