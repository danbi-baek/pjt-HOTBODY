<template>
  <div class="loading_container">
      <!-- 음식 -->
    <div class="load_img" > 
      <i v-if="num==0" class="one fas fa-utensils fa-7x"></i>
      <i v-if="num==1" class="two fas fa-fish fa-7x"></i>
      <i v-if="num==2" class="three fas fa-weight fa-7x"></i>
      <i v-if="num==3" class="four fas fa-pizza-slice fa-7x"></i>
      <i  v-if="num==4" class="five fas fa-running fa-7x"></i>
      <i  v-if="num==5" class="six fas fa-apple-alt fa-7x"></i>
      <h5 v-if="$store.state.bodyorfood==0">음식 분석 중..</h5>
      <h5 v-if="$store.state.bodyorfood==1">바디 분석 중..</h5>
      <h5 v-if="$store.state.bodyorfood==2">BMI 분석 중..</h5>
     </div>
  </div>
</template>

<script>
export default {
  mounted(){
      this.changeLoading()
    },
computed:{
       changes : {
            get(){
               
                return this.num;
            },
            set(v){
                this.num=  v;
            }
        }
    },
    methods:{
      changeLoading(){
          this.intervalid = setInterval(()=>{
          this.num = (this.num+1)% 6;
          }, 200);

      }
    },
data(){
    return{
        num: 0,

    }
}
}
</script>

<style scoped>
.loading_container{
    min-height:1600px;
}
.load_img{
    width:fit-content;
    height:fit-content;
    margin:400px auto;
}
.one {
    color: red;
}
.two {
    color : orange;
}
.three {
    color: yellow;
}
.four{
    color:greenyellow;
}
.five{
    color:blue;
}
.six{
    color:purple;
}
</style>