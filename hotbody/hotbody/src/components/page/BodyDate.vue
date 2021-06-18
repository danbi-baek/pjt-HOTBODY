<template>
  <div class="date_container">
      <div class="dv_date">
        <template v-if="items.length != 0">
            <body-chart></body-chart>
        </template>
        <br>
        <p class="title_date">날짜를 선택해 지난 날과 오늘을 비교 해보세요!</p>
        <div class="div_date">
            <div style="display: inline-block;">📅</div>
            <div class="date_picker">
                <v-date-picker
                    mode="range"
                    color="red"
                    v-model="dateRange"
                    :input-props='{
                        placeholder: "Select Date",
                        readonly: true
                    }'
                />
            </div>
            <div class="btn_date" @click="getBody">비교</div>
        </div>
            <hr>

        <div v-if="openbody == false">
            <h4 class="hwrite" style="margin-top:200px;">비교 버튼을 눌러 결과를 확인하세요</h4>
        </div>
        <div v-else-if="items.length==0" style="margin-top:200px;"> 
           <h4 class="hwrite">
            기록된 몸이 없습니다😯 <br> 사진을 업로드 해 주세요📷
           </h4>
        </div>
        <div v-else>
        
        <div class="bodyImgs" v-if="dateRange && openbody == true" >
            <div class="body_slide">
                <p>사진을 클릭하면 상세정보가 나와요📋</p>
                <hooper :settings="hooperSettings" style="">
                    <slide v-for="(item, i) in items" :key="i">
                        <img :src="'http://127.0.0.1:8000'+item.bodyImg"  class="extend_body" 
                        sytle="width:auto; height:80%; top:20%;" @click="getInfo(item)">
                    </slide>
                    <hooper-navigation slot="hooper-addons"></hooper-navigation>
                    <hooper-pagination slot="hooper-addons"></hooper-pagination>
                </hooper>
            <template v-if="bodyInfo.length != 0">
                <div  class="info_div">
                    <div class="card">
                    <div class="card__image card__image--fence" :style="{'background-image' : 'url(http://127.0.0.1:8000'+bodyInfo.bodyImg}">
                        <!-- <img :src="'http://127.0.0.1:8000'+bodyInfo.bodyImg"> -->
                    </div>
                    <div class="card__content">
                        <div class="card__title">바디 정보</div>
                        <p class="card__text">키 : {{bodyInfo.height}}</p>
                        <p class="card__text">몸무게 : {{bodyInfo.weight}}</p>
                        <p class="card__text">bmi : {{bodyInfo.bmi}}</p>
                        <p class="card__text">근육량 : {{bodyInfo.muscle}}</p>
                        <p class="card__text">체지방률 : {{bodyInfo.fat}}</p>

                        <span class="card-meta">{{bodyInfo.bodyDate}}</span>
                    </div>
                    </div>
                </div>
            </template>
            </div>
        </div>
        </div>

      </div>
  </div>
</template>

<script>
import { Hooper, Slide,Navigation as HooperNavigation } from 'hooper';
import BodyChart from './BodyChart.vue'
import 'hooper/dist/hooper.css';
import axios from 'axios';

export default {
    components:{
        Hooper,
        Slide,
        HooperNavigation,
        BodyChart
    },
    data(){
        return{
            openbody: false,
            dateRange: null,
            items: [ ],
            isChecked: false,
            bodyInfo: [],
            hooperSettings: {
                itemsToShow:3,
                trimWhiteSpace:true,
                itesToSlide:0,
            },
            chartDate: [],
            chartWeight: [],
            chartFat: []
           
        }
    },
    methods:{
        getInfo(e){
            this.bodyInfo = e;
            // console.log('클릭한 바디 정보')
            // console.log(this.bodyInfo)
        },
        getBody(){
            if(this.dateRange == null){
                alert('날짜를 선택해 주세요')
                this.openbody = false
                return
            }
            this.openbody = true
            // console.log('날짜 ㅜㅜ '+ this.dateRange)
            this.dateRange.start.setHours(12)
            let dateStart = this.dateRange.start.toISOString().substring(0, 10)

            this.dateRange.end.setHours(12)
            let dateEnd = this.dateRange.end.toISOString().substring(0, 10)
            
            let config = {
                header: {
                   'Authorization' : 'JWT' + localStorage.getItem("token") 
                }
            }
            // console.log(dateStart+','+dateEnd)
            axios.get('http://127.0.0.1:8000/accounts/bodylist/',
                { params:{
                    pk: localStorage.getItem('userpk') ,start : dateStart , end : dateEnd }
                },
                config
            )
            .then( res => {
                // console.log(res.data)
                this.items = res.data

                for(var i=0 ; i < res.data.length ; i++){
                    this.chartWeight[i] = res.data[i].weight
                    this.chartFat[i] = res.data[i].fat
                    this.chartDate[i] = res.data[i].bodyDate
                }
                this.$store.state.chartWeight = this.chartWeight
                this.$store.state.chartFat = this.chartFat
                this.$store.state.chartDate = this.chartDate
                    // console.log('체지방률 '+ this.$store.state.chartFat)
                    // console.log('몸무게 '+ this.$store.state.chartWeight)
                    // console.log('날짜'+ this.$store.state.chartDate)
            })
            .catch( err => {
                console.log(err)
            })
        },
         

    },
    created(){

    },
    mounted(){
    },
    watch: {
       
    }
}

</script>

<style lang="scss" scoped>

@import '@/assets/sass/datePicker.sass'; 
@import '@/assets/sass/date.scss'
</style>