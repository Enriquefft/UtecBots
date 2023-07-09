<template>
  <div class="register">
    <div class="image-box">            
    </div>

    <div class="register-box">
        
        
        <img height="100" margin="10" src="https://cdn-icons-png.flaticon.com/512/847/847291.png?w=740&t=st=1687372978~exp=1687373578~hmac=7d5caef5ede5a500b58eab469fa88304fe4bbe79fc91e4c4e11602809cfd1973">
        
        <div class="register-box-information">
            <label ><b>Username</b></label>
            <input v-model="username" type="text" >
        </div>

        <div class="register-box-information">
            <label ><b>Phone Number</b></label>
            <input v-model="phone_number" type="text" >
        </div>        
        
        <div class="register-box-information">
            <label ><b>Password</b></label>
            <input v-model="password" type="password" >
        </div>
        
        <div class="register-box-button">
            <button @click="isRegister(username,password,phone_number)"><label><b>Register</b></label></button>                
        </div>
            
        <h3 v-if="boolRegister === false" style="color:red; transition: opacity 0.5s cubic-bezier(0.4, 2, 0.2, 1); opacity: 1;">{{ error_msg }}</h3>                 
        
    </div>

    

    
</div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      phone_number: "",
      error_msg: "",
      boolRegister: true
    };
  },

  methods: {
    isRegister(username, password, phone_number) {
      const url = "https://b5jlsdgj5l.execute-api.us-east-1.amazonaws.com/prod/user/register";
      const data = {
        username: username,
        phone_number: phone_number,
        password: password
      };

      

      fetch(url, {
        method: "POST",
        body: JSON.stringify(data)
      })
        .then(response => response.json())
        .then(result => {
          // Procesar la respuesta de la API aquí
          console.log(result.statusCode);
        
            // Comprobar si existe el usuario o no
          if(result.statusCode === 400){
            this.error_msg = result.message;
            this.boolRegister = false;
            console.log("Hay error")
          }

          //Refidrecciona al menu
          else{
            this.$router.push({
            path: '/menu',
            query: {
                username: this.username,
                phone_number: this.phone_number,
                password: this.password
            }
            });
          }
          
        })
        .catch(error => {
          // Manejar cualquier error de la solicitud aquí
          console.error(error);
        });
    }
  },
};
</script>

<style>


.register {
  display: flex;
height: 100vh; /* Ocupa toda la altura de la pantalla */
}

.register-box {
flex: 3;    
display: inline-flex;
flex-direction: column;
padding: 100px;     
align-items: center;

}

.register-box-information{
margin: 10px;
display: inline-flex;
flex-direction: column;  
font-size:30px ; 

} 

.register-box-information input{

font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
font-size: 20px;    
outline: none; 
border: none;
background-color: #EDEDED;
border-radius: 10px;
padding:10px;
}


.register-box-button button{
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
margin: 10px;
border: none;
background-color: #00ff84;
padding: 10px;
border-radius: 10px;
}

.register-box-button a{
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
margin: 25px;
color: black;


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