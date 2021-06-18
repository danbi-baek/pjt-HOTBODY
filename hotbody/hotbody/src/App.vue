<template>
  <div id="app">
    
    <router-view />
  </div>
</template>

<script>

export default {
  name : 'App',
  components : {

  },
  created(){
    this.url = this.$route.name;
  },
  watch: {
    $route (to,from){
        this.checkUrl(to.name,from.name);
    }
  },
  methods : {
    checkUrl(url,nowurl) { 
      console.log(url)
      console.log(nowurl)
    },
  },
  data : function () {
    return {
      url: '',
      nowurl: ''
    }
  }
}

</script>

<style>
*{
    font-family: "AlternateGotNo2D", "Helvetica Neue", "Helvetica", sans-serif;
}
#app{
}
a {
    text-decoration: none;
    color:black;
    cursor: pointer;
}
a:hover{
  color:darkgray;
}
</style>
