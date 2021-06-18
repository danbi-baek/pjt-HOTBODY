<template>
  <div class="maindaykal">
    <div class="daykalbox">
      <div class="kalprogress">
        <circle-progress 
        :r=100
        stroke-bg-color='#f0f0f0'
        stroke-color='#5765FF'
        :stroke-width=18
        :percentage="kalP" 
        >
        <p style="margin-top:55px;">잔여칼로리<br></p>
        <p style="font-size:24px;" :class="{'eatover':eatover[0]}">{{totalkal}}</p>
        <p v-if="eatover[0]" style="font-size:10px" class="eatover">일일칼로리 초과!</p>
          </circle-progress>
      </div>
      <div class="nutrientprogress">
        <div class="nutrients">
          <p>탄수화물</p>
          <progress-bar 
          :height=15
          color='#5765FF'
          bg-color='#f0f0f0'
          :show-top-tip=false
          :percentage="(eatcar/car)*100"/>
          <p style="font-size:10px;">{{eatcar}} / {{Math.round(car)}}g</p>
        </div>
        <div class="nutrients">
          <p>단백질</p>
          <progress-bar 
          :height=16
          color='#5765FF'
          bg-color='#f0f0f0'
          :show-top-tip=false
          :percentage="(eatpro/pro)*100" />
          <p style="font-size:10px;">{{eatpro}} / {{Math.round(pro)}}g</p>
        </div>
        <div class="nutrients">
          <p>지방</p>
          <progress-bar 
          :height=15
          color='#5765FF'
          bg-color='#f0f0f0'
          :show-top-tip=false
          :percentage="(eatfat/fat)*100" />
          <p style="font-size:10px;">{{eatfat}} / {{Math.round(fat)}}g</p>
        </div>
      </div>
    </div>
    <div class="btn_body" @click="goDiary">
      기록하러 가기
    </div>
  </div>
</template>

<script scoped>
// import axios from 'axios';
import 'vue-pithy-progress/dist/vue-pithy-progress.css'
export default {

  data () {
    return {
      car: 0,
      pro: 0,
      fat: 0,
      eatcar:0,
      eatpro:0,
      eatfat:0,
      kalP:0,
      totalkal:0,
      eatkal: 0,
      list: [],
      eatover: [false,false,false,false],
      
    }
  },
  created (){
    this.eatkal = this.$store.state.maineat[0]
    this.eatcar = this.$store.state.maineat[1]
    this.eatpro = this.$store.state.maineat[2]
    this.eatfat = this.$store.state.maineat[3]

    this.totalkal = Math.round(this.$store.state.maindayKcal)
    this.kalP = (this.eatkal/this.totalkal*100)

    this.totalkal = this.totalkal - this.eatkal
    if(this.totalkal<0) {
      this.eatover[0] = true
      this.totalkal = this.totalkal * -1
    }

    if(this.$store.state.usergoal == 1){ //체중 감소
        this.car = this.totalkal*0.3/4
        this.pro = this.totalkal*0.4/4
        this.fat = this.totalkal*0.3/9
    }else if (this.$store.state.usergoal == 2){ // 체중 유지
        this.car = this.totalkal*0.5/4
        this.pro = this.totalkal*0.3/4
        this.fat = this.totalkal*0.2/9
    }else { //벌크업
        this.car = this.totalkal*0.4/4
        this.pro = this.totalkal*0.4/4
        this.fat = this.totalkal*0.2/9
    }


    // console.log('CREATED MAINDAYKAL')
  },
  methods:{
    goDiary(){
        window.scrollTo(0, 0)
        this.$store.state.menuClick = 2
        this.$router.push('./diary')
    }
  }
}
</script>

<style lang="scss" scoped>
.nutrientprogress{
  width:100%;
  text-align: center;
}
.nutrients{
  display: inline-block;
  width: 28%;
  margin:10px;
  font-weight: bold;
  font-size:14px;
}
.nutrients p{
  margin-bottom:6px;
}

.kalprogress{
  width:30%;
  margin:20px auto;
  text-align: center;
  font-weight: bold;
  font-size:12px;
}
.kalprogress p {
  margin-top:20px;
}

// ------------------

.maindaykal{
  height:730px;
  margin:0 auto;
}
.daykalbox{
  margin:0 auto;
  width:550px;
  height:400px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  background: white;
  border-radius:50px;
  margin-top:140px;
  padding-top:20px;
}
.btn_body{
    width: 150px;
    height: 5%;
    background-color: rgb(255, 88, 102);
    color: #fff;
    cursor: pointer;
    margin: 50px 0 0 50px;
    align-self: center;
    line-height: 42px;
    backface-visibility: hidden;
    text-align: center;
    margin:80px auto;
    font-family: Impact, sans-serif;
    font-weight: bold;
    font-style: normal;
}
.btn_body:hover{
    background-color:  rgba(255, 146, 157, 0.884);
}
.eatover{
  color:red;
}
</style>