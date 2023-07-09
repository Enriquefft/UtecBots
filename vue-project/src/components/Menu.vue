<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './HelloWorld.vue'

</script>

<template>
  <div class="menu">
    <div class="menu-bar">
      <div class="menu-bar-sections">
        <img src="https://cdn-icons-png.flaticon.com/512/1239/1239343.png?w=740&t=st=1687377653~exp=1687378253~hmac=6623b1c389d347e9e10a2394dfc6a7d8efa2f7c7c02649ad1a7ba6ca4b80c0e7">
        <a @click="loadPage('/menu/menu-info')">Home</a>
      </div>

      <div class="menu-bar-sections">
        <img src="https://cdn-icons-png.flaticon.com/512/1201/1201419.png?w=740&t=st=1687378044~exp=1687378644~hmac=8bd531de52ea112c1acc0dc7cf50e8cf99d6ec4bd454c0c8976dee98783cd689">
        <a @click="loadPage('/menu/bots')">Bots</a>
      </div>

      <div class="menu-bar-sections">
        <img src="https://cdn-icons-png.flaticon.com/512/929/929358.png?w=740&t=st=1687378205~exp=1687378805~hmac=8f84fec28fc95562bd024771c0d5f6740fdde1cde1bed5654a2cbdcddeb8b700">
        <a @click="loadPage('/menu/maker')">Maker</a>
      </div>

      <div class="menu-bar-sections">
        <img src="https://cdn-icons-png.flaticon.com/512/15/15659.png?w=740&t=st=1687378321~exp=1687378921~hmac=a1706a2db3f9a90ae3e7056309ae36c8af969d1248e84ad2fe09995a6dd48485">
        <a @click="loadPage('/aboutUs')">About Us</a>
      </div>

      <div class="menu-bar-sections">
        <img src="https://cdn-icons-png.flaticon.com/512/929/929358.png?w=740&t=st=1687378205~exp=1687378805~hmac=8f84fec28fc95562bd024771c0d5f6740fdde1cde1bed5654a2cbdcddeb8b700">
        <router-link to="/">LogOut</router-link>
      </div>
    </div>

    <div class="menu-container">
      <iframe :src="`${pageUrl}?username=${username}`" frameborder="0" width="100%" height="100%"></iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuComponent',
  props: {
    username: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      pageUrl: '/menu/menu-info', // Página inicial a cargar
      username : this.$route.query.username,
      phone_number: this.$route.query.phone_number,
      password: this.$route.query.password,
    };
  },
  methods: {
    loadPage(url) {
      
      this.pageUrl = url + '?username=' + this.username;


    },
  },
};
</script>


<style>
.menu {
  display: flex;
}

.menu-bar {
  flex: 1;
  display: inline-flex;
  height: 100vh;
  flex-direction: column;
  align-items: center;
  font-size: 20px;
}

.menu-bar-sections {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  margin: 0;
  margin: 10px;
}

.menu-bar-sections a {
  list-style-type: none;
  text-decoration: none;
  color: black;
}

.menu-bar-sections img {
  height: 30px;
  width: 30px;
}

.menu-container {
  flex: 9;
  background-color: #242525;
  color: white;
}

.menu-container iframe {
  overflow-y: scroll;
  border: none;
  /* Elimina los bordes del contenedor */
  height: 100vh;
  /* Ajusta la altura según tus necesidades */
  width: 100%;
}
</style>
