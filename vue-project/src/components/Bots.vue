<template>
    <div class="bots-principal">
        <div v-if="activate_recrrent_bot">
            <h1>Recurrent Bots - {{ getContOwnBots( owner ) }}</h1>
          <div class="bots"> 
            
          
    
              <div class="bot-list">
                  
                  <div class="bot-list-one">
                      <div class="bot-list-one-perfil">
                          <img :src=bot_icon_activate>
                          <b><p>{{ bot_username_activate }}</p></b>
                      </div>
      
                      <div class="bot-list-one-description">
                          <p>{{bot_description_activate}}</p>   
                          <div class="login-box-button">
                            <button @click="desactivateBot()"><label><b>Desactivate</b></label></button>                      
                          </div>                     
                      </div>
                      
                      
                      

                      
                      
                  </div>          
      
              </div>  
          </div>
          
        </div>
        
        
        


        <h1>Community Bots - {{ getContCommunityBots() }}</h1>
        <div class="bots">
  
        
  
            <div v-for="bot in dataBots" :key="bot.bot_id" class="bot-list">
                
                <div class="bot-list-one">
                    <div class="bot-list-one-perfil">
                        <img :src=bot.icon>
                        <b><p>{{ bot.bot_username }}</p></b>

                        <div class="bot-list-one-description">
                          <p>{{bot.description}}</p>                          
                        </div>

                        <div class="login-box-button">
                          <button @click="activateBot(bot.bot_username,bot.icon,bot.description)"><label><b>Activate</b></label></button>                      
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
            dataBots : fetch('https://m2zak1cxah.execute-api.us-east-1.amazonaws.com/prod/bot/list')
      .then(response => response.json())
      .then(data => {
        // Maneja los datos recibidos de la API
        this.dataBots = data.bots; 
      }),
        owner : this.getUsername() ,
        bot_username_activate : "",
        bot_icon_activate : "",
        bot_description_activate : "",
        activate_recrrent_bot : false
        
        }        
    },

 

    methods: {
        getUsername() {
            // Obtiene la URL actual
            var url = window.location.href;
            //console.log(url);

            // Obtiene el nombre de la URL
            var nameParam = new URL(url).searchParams.get("username");
            var username = nameParam ? nameParam.split('=')[1] : '';
            

            return username;
        },

        getContOwnBots(owner){

            let cont = 0;

            //console.log(this.dataBots)
            for(let i = 0; i < this.dataBots.length;i++){
                if(this.dataBots[i].owner == owner){
                    cont = cont + 1;
                }
            }

            return cont;
        },
        getContCommunityBots(){

            let cont = 0;

            //console.log(this.dataBots)
            for(let i = 0; i < this.dataBots.length;i++){
                cont = cont + 1;
            }

            return cont;
        },

        activateBot(bot_username,bot_icon,bot_description){
          this.bot_username_activate = bot_username;
          this.bot_icon_activate = bot_icon;
          this.bot_description_activate = bot_description;
          this.activate_recrrent_bot = true;
        },

        desactivateBot(){
          this.bot_username_activate = "";
          this.bot_icon_activate = "";
          this.bot_description_activate = "";
          this.activate_recrrent_bot = false;
        }


        

        
    },
  
  }
  </script>
  
  <style>

  .activate-button{
    display: flex;
    align-content: center;
  }
  
  .bots-principal{
    margin: 20px;
    color:white
  }
  
  
  .bots{  
    
    
    display:inline-flex;
    flex-direction: row;
    flex-wrap: wrap;
    
  }
  
  .bots-list{
    display:inline-flex;
    flex-direction: row;
    
    
  }
  
  .bot-list-one{
    display: inline-flex;
    flex-direction: column;
    background-color: #2f3030;
    border-radius: 10px;
    padding: 40px;
    margin: 10px;    
        
  }
  
  .bot-list-one-perfil{
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    
  }
  
  .bot-list-one-perfil img{
    width: 200px;
    height: 200px;
    border-radius: 10px;
    
  }
  
  .bot-list-one-description{
    text-align: center;
  }
  
  
  
  
  </style>