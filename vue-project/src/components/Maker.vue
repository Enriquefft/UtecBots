<template>
    <div class="maker">
      <h1>Maker</h1>     
      
      <div class="create-bot">
        <div class="create-bot-form">
          <div class="register-box-information">
            <label><b>Bot Username</b></label>
            <input v-model="bot_username" type="text">
          </div>
  
          <div class="register-box-information">
            <label><b>URL Icon</b></label>
            <input v-model="icon" type="text">
          </div>
  
          <div class="register-box-information">
            <label><b>Description</b></label>
            <input v-model="description" type="text">
          </div>
  
          <div class="register-box-button">
            <button @click="isCreateBot(bot_username, icon, description, getUsername())">
              <label><b>Create</b></label>
            </button>
          </div>
  
          <h3 v-if="boolCreateBot === false" style="color:red; transition: opacity 0.5s cubic-bezier(0.4, 2, 0.2, 1); opacity: 1;">
            {{ msg }}
          </h3>
          <h3 v-if="msg === 'Se ha creado exitosamente'" style="color:rergb(9, 255, 0)transition: opacity 0.5s cubic-bezier(0.4, 2, 0.2, 1); opacity: 1;">
            {{ msg }}
          </h3>
        </div>
  
        <div class="preview-bot">
          <div class="bot-list">           
            <div class="bot-list-one">
              <div class="bot-list-one-perfil">
                <img :src="icon">
                <b><p>{{ bot_username }}</p></b>
              </div>
  
              <div class="bot-list-one-description">
                <p>{{ description }}</p>
                <p><u>Created by {{ getUsername() }}</u></p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {    
    data() {
      return {
        bot_username: "",
        icon: "https://www.softzone.es/app/uploads/2018/04/guest.png",
        owner: "",
        description: "",
        boolCreateBot: true,
        msg : "",
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
      isCreateBot(bot_username, icon, description,owner) {
        const url = "https://m2zak1cxah.execute-api.us-east-1.amazonaws.com/prod/bot/create";
        const data = {
            owner: owner,
            bot_username: bot_username,
            icon: icon,
            description : description,
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
                this.msg = result.message;
                this.boolCreateBot = false;
                console.log("Hay error")
            }

            //Refidrecciona al menu
            else{
                this.msg = "Se ha creado exitosamente";
            }
            })
            .catch(error => {
            // Manejar cualquier error de la solicitud aquí
            console.error(error);
            });
        }
    
        }
    
  }
  </script>
  
  <style>
  .maker {
    color: white;
    margin: 20px;
  }
  
  .create-bot {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }
  </style>
  