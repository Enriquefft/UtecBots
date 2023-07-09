
<template>
    <div class="menu-info">
        <h1>Hola {{ username }}</h1>        
    </div>
    
    

    
</template>

<script>
export default {
  props: ['name'], // Prop para recibir el valor de name

  data() {
    return {
        username : this.getUsername()
    }
  },

  methods: {
      getUsername() {
            // Obtiene la URL actual
            var url = window.location.href;
            console.log(url);

            // Obtiene el nombre de la URL
            var nameParam = new URL(url).searchParams.get("username");
            var username = nameParam ? nameParam.split('=')[1] : '';
            console.log(username);

            return username;
        },
    }
};
</script>

<style>

.menu-info{
    color: white;
}
</style>