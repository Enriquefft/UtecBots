<template>
  <div class="login">

    <div class="login-box">
        
        <img height="100" margin="10" src="https://cdn-icons-png.flaticon.com/512/847/847291.png?w=740&t=st=1687372978~exp=1687373578~hmac=7d5caef5ede5a500b58eab469fa88304fe4bbe79fc91e4c4e11602809cfd1973">
        
        <div class="login-box-information">
            <label><b>Username</b></label>
            <input v-model="username" type="text">
        </div>
        
        <div class="login-box-information">
            <label ><b>Password</b></label>
            <input v-model="password" type="password" >
        </div>
        
        <div class="login-box-button">
            <button @click="isLogin(username,password)"><label><b>Login </b></label></button>
            <router-link to="/register">Register an account</router-link>
        </div>
        
        
        <h3 v-if="boolLogin === false" style="color:red; transition: opacity 0.5s cubic-bezier(0.4, 2, 0.2, 1); opacity: 1;">El usuario o contraseña no es válido</h3>           
                      
        
    </div>

    <div class="image-box">            
    </div>

    
</div>



</template>

<script>





export default {
  data() {
    return {
      username : "",
      password : "",
      dataUserList : "",
      boolLogin : true,
      
    }
  },


  methods: {
  isLogin(username, password) {
    fetch('https://b5jlsdgj5l.execute-api.us-east-1.amazonaws.com/prod/user/list')
      .then(response => response.json())
      .then(data => {
        // Maneja los datos recibidos de la API
        this.dataUserList = data;

        

        for(let i = 0; i< this.dataUserList.pendientes.length;i++){
          if(this.dataUserList.pendientes[i].username== username &&this.dataUserList.pendientes[i].password == password ){
            console.log("True")
            this.$router.push({
            path: '/menu',
            query: {
              username: this.username,
              phone_number:this.dataUserList.pendientes[i].phone_number,
              password: this.password
            }
          });
          }
        }

        this.boolLogin = false;
        console.log("False")

        


        
      })
    }
  },


}
</script>

<style>
body{
  margin: 0;
  padding: 0; 
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.login {
  display: flex;
height: 100vh; /* Ocupa toda la altura de la pantalla */
}

.login-box {
  flex: 3;    
  display: inline-flex;
  flex-direction: column;
  padding: 100px;     
  align-items: center;
  
}

.login-box-information{
  margin: 10px;
  display: inline-flex;
  flex-direction: column;  
  font-size:30px ; 
  
} 

.login-box-information input{
  
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 20px;    
  outline: none; 
  border: none;
  background-color: #EDEDED;
  border-radius: 10px;
  padding:10px;
}


.login-box-button button {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 10px;
  border: none;
  background-color: #00ff84;
  padding: 10px;
  border-radius: 10px;
  transition: background-color 0.3s ease;
}

.login-box-button button:hover {
  background-color: #3fffa2;
}

.image-box{

  flex: 7;
background-image: url("https://posgrado.utec.edu.pe/wp-content/uploads/2020/04/nosotros_01.jpg");
background-repeat: no-repeat;
background-size: cover ;
background-position: right ; /* Mueve la imagen a la izquierda */
  
  
}

/* Resto del código CSS... */


</style>