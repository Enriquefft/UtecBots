<template>
    <div class="bots-principal">
        <!--
        <h1>Own Bots - {{ getContOwnBots( owner ) }}</h1>
        <div class="bots"> 
        
  
            <div v-for="bot in dataBots" :key="bot.bot_id" class="bot-list">
                
                <div v-if="bot.owner ==owner" class="bot-list-one">
                    <div class="bot-list-one-perfil">
                        <img :src=bot.icon>
                        <b><p>{{ bot.bot_username }}</p></b>
                    </div>
    
                    <div class="bot-list-one-description">
                        <p>{{bot.description}}</p>
                        <p><u>Created by {{bot.owner}}</u></p>
                    </div>
                    
                </div>          
    
            </div>  
        </div>
        <---->


        <h1>Community Bots - {{ getContCommunityBots() }}</h1>
        <div class="bots">
  
        
  
            <div v-for="bot in dataBots" :key="bot.bot_id" class="bot-list">
                
                <div class="bot-list-one">
                    <div class="bot-list-one-perfil">
                        <img :src=bot.icon>
                        <b><p>{{ bot.bot_username }}</p></b>
                    </div>
    
                    <div class="bot-list-one-description">
                        <p>{{bot.description}}</p>
                        <p><u>Created by {{bot.owner}}</u></p>
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

        

        
    },
  
  }
  </script>
  
  <style>
  
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