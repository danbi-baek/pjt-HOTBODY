<template>
  <div class="mainchart">
    <div class="avgBox avgBmi">
        <div class="avgInner myBmi">
          <p class="bmitxt">키(cm)</p>
          <p class="bminum" style="color:#7a8d99;">{{$store.state.height}}</p>

        </div>
        <div class="avgInner otherBmi">
          <p class="bmitxt">체중(kg)</p>
          <p class="bminum" style="color:rgb(255, 88, 102);">{{$store.state.weight}}</p>
        </div>
      <div class="avgText">
        <p>
          *<b>{{nickname}}</b>님은 <b style="color:rgb(255, 88, 102)">{{bmitext}}범위</b>의 BMI를 가지고 있네요<br>
        </p>  
          저희 사이트와 함께 관리하러 가볼까요?
        
      </div>
    </div>
    <div class="mainbackimg">
    <div class="welcomemsg">
      <h4 v-if="len==1">{{msg[this.num]}}</h4>
    </div>
    <div >
    <line-chart/>
    </div>
    </div>
  </div>
</template>

<script>
import LineChart from  '@/components/page/LineChart.vue'
// import axios from 'axios';

export default {
    components : {
        LineChart,
    },
    created(){
      this.todaybmi = this.$store.state.mainbmi
      this.nickname = this.$store.state.Usernickname

      this.len = this.$store.state.chartdatas.length

      if(this.todaybmi<18.5) this.bmitext = '저체중'
      else if(this.todaybmi<23) this.bmitext = '정상체중'
      else if(this.todaybmi<25) this.bmitext = '과체중'
      else if(this.todaybmi<30) this.bmitext = '경도비만'
      else if(this.todaybmi<35) this.bmitext ='중정도'
      else this.bmitext ='고도비만'
    },
    mounted(){
      this.changeMsg()
    },
    computed:{
       changes : {
            get(){
                // //console.log("changes-get:"+this.num)
                return this.num;
            },
            set(v){
                // //console.log("changes-set:"+v)
                this.num=  v;
            }
        }
    },
    methods:{
      changeMsg(){
          this.intervalid = setInterval(()=>{
          this.num = (this.num+1)% 2;
          },3000);

      }
    },
    data(){
      return {
          nickname: '',
          list:[],
          todaybmi:0,
          avgbmi:0,
          bmitext:'정상체중',
          len:0,
          num:0,
          msg: [
            '✨WELCOME HOTBODY✨',
            '더 많은 정보를 추가하고 당신의 BMI 변화를 그래프로 확인해 보세요😉'
          ]

      }
    },
}
</script>

<style scoped>
.mainbackimg{
  padding-top:20px;
  padding-bottom:40px;
  /* background: #f0f0f0; */
  /* background-image: url('../../assets/backIMG.png'); */
}
.avgBox{
  margin:30px auto;
  width:400px;
  height:230px;
  /* background: white; */
  text-align: center;
  border-radius: 30px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  border:1px solid white;
  background:white;
  
}
.avgInner{
  width:48%;
  margin-top:30px;
  padding:4px; 
  font-weight: bold;
}
.bmitxt{
  font-size:14px;
}
.bminum{
  font-size:35px;
}
.myBmi{
  float:left;
  /* border-right:1px solid darkgray; */
}
.otherBmi{
  float:right;
}
.avgText{
  margin-top:140px;
  color:#969696;
  font-size:12px;
}
.welcomemsg{
  text-align:center;
  height:120px;
}
h4 {
  /* font-weight:bold; */
  font-family: 'NanumBarunGothic'; 
  font-style: normal;
  font-weight: bold ; 
}
</style>