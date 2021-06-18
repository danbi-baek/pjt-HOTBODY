<template>
    <div class="bodypage">
        <main-header/>
        <modal-upload/>
        <loading v-if="$store.state.loadingflag"/>
        <div v-if="!$store.state.loadingflag">
        <div class="body_chart">
            <p class="write" v-if="this.type==0" style="text-align:center">💪 당신의 결과를 바디 측정을 통해 확인해보세요 🤳</p>
            <div class="container_body">
                <div style="float:left; width:30%;height:400px;" > 
                    <img v-if="$store.state.gender == 1" class="card-5" style="width:100%; height:100%;" v-bind:src="imgSrcGirl">
                    <img v-if="$store.state.gender == 2" class="card-5" style="width:100%; height:100%;" v-bind:src="imgSrcMan">
                </div>
                <div v-if="this.sex==2" style="overflow-x: auto; padding-left:5%; padding-top:4% width:50%" >
                    <p class="hwrite">체지방률({{this.ofat}}%)</p>
                    <progress-bar :height=8 color='#808080' bg-color='#f0f0f0' :show-top-tip=false :percentage="fat" />
                    <div class="progress" style="margin-top:0.3%;">
                        <div class="progress-bar progress-bar-info" role="progressbar" style="width:25%">underfat</div>
                        <div class="progress-bar progress-bar-success" role="progressbar" style="width:25%">healthy</div>
                        <div class="progress-bar progress-bar-warning" role="progressbar" style="width:12.5%">overfat</div>
                        <div class="progress-bar progress-bar-danger" role="progressbar" style="width:37.5%">obese</div>
                    </div>
                    <div class="bar">
                        <div style="width:24%">0</div>
                        <div style="width:24%">10</div>
                        <div style="width:13%">20</div>
                        <div style="width:36%">25</div>
                    </div>
                    <br>
                    <p class="hwrite">골격근량({{this.omuscle}}kg)</p>
                    <progress-bar :height=8 color='#808080'  bg-color='#f0f0f0' :show-top-tip=false :percentage="muscle"/>
                     <div class="progress" style="margin-top:0.3%;">
                        <div class="progress-bar progress-bar-danger" role="progressbar" style="width:36%">low</div>
                        <div class="progress-bar progress-bar-success" role="progressbar" style="width:17%">general</div>
                        <div class="progress-bar progress-bar-info" role="progressbar" style="width:47%">high</div>
                    </div>
                    <div class="bar">
                        <div style="width:34%">15</div>
                        <div style="width:16%">27.5</div>
                        <div>33.5</div>
                    </div>
                    <br>
                    <p class="hwrite">bmi({{this.obmi}}kg/m^2)</p>
                    <progress-bar :height=8 color='#808080' bg-color='#f0f0f0' :show-top-tip=false :percentage="bmi"/>
                     <div class="progress" style="margin-top:0.3%;">
                        <div class="progress-bar progress-bar-info" role="progressbar" style="width:34%">low</div>
                        <div class="progress-bar progress-bar-success" role="progressbar" style="width:18%">general</div>
                        <div class="progress-bar progress-bar-danger" role="progressbar" style="width:48%">high</div>
                    </div>
                     <div class="bar">
                        <div style="width:33%">10</div>
                        <div style="width:17%">18.5</div>
                        <div>23</div>
                    </div>
                    <br>
                    <p class="hwrite">기초대사량({{this.obmr}}kcal))</p>
                    <progress-bar :height=8 color='#808080' bg-color='#f0f0f0' :show-top-tip=false :percentage="bmr"/>
                     <div class="progress" style="margin-top:0.3%;">
                        <div class="progress-bar progress-bar-danger" role="progressbar" style="width:40%">low</div>
                        <div class="progress-bar progress-bar-success" role="progressbar" style="width:13%">general</div>
                        <div class="progress-bar progress-bar-info" role="progressbar" style="width:47%">high</div>
                    </div>
                    <div class="bar">
                        <div style="width:37%">1000</div>
                        <div style="width:12.5%">1600</div>
                        <div>1800</div>
                    </div>
                    <br>
                </div>
                <div v-else style="overflow-x: auto; padding-left:10%; padding-top:4%">
                    <p class="hwrite">체지방률({{this.ofat}}%)</p>
                    <progress-bar :height=8 color='#808080' bg-color='#f0f0f0' :show-top-tip=false :percentage="fat"/>
                    <div class="progress" style="margin-top:0.3%;">
                        <div class="progress-bar progress-bar-info" role="progressbar" style="width:37.5%">underfat</div>
                        <div class="progress-bar progress-bar-success" role="progressbar" style="width:25%">healthy</div>
                        <div class="progress-bar progress-bar-warning" role="progressbar" style="width:12.5%">overfat</div>
                        <div class="progress-bar progress-bar-danger" role="progressbar" style="width:25%">obese</div>
                    </div>
                    <div class="bar">
                        <div style="width:36%">0</div>
                        <div style="width:25%">15</div>
                        <div style="width:12.5%">25</div>
                        <div style="width:24%">30</div>
                    </div>
                    <br>
                    <p class="hwrite">골격근량({{this.omuscle}}kg)</p>
                    <progress-bar :height=8 color='#808080'  bg-color='#f0f0f0' :show-top-tip=false :percentage="muscle"/>
                     <div class="progress" style="margin-top:0.3%;">
                        <div class="progress-bar progress-bar-danger" role="progressbar" style="width:40%">low</div>
                        <div class="progress-bar progress-bar-success" role="progressbar" style="width:17%">general</div>
                        <div class="progress-bar progress-bar-info" role="progressbar" style="width:43%">high</div>
                    </div>
                    <div class="bar">
                        <div style="width:39%">10</div>
                        <div style="width:16%">22</div>
                        <div>27</div>
                    </div>
                    <br>
                    <p class="hwrite">bmi({{this.obmi}}kg/m^2)</p>
                    <progress-bar :height=8 color='#808080' bg-color='#f0f0f0' :show-top-tip=false :percentage="bmi"/>
                     <div class="progress" style="margin-top:0.3%;">
                        <div class="progress-bar progress-bar-info" role="progressbar" style="width:34%">low</div>
                        <div class="progress-bar progress-bar-success" role="progressbar" style="width:18%">general</div>
                        <div class="progress-bar progress-bar-danger" role="progressbar" style="width:48%">high</div>
                    </div>
                     <div class="bar">
                        <div style="width:33%">10</div>
                        <div style="width:17%">18.5</div>
                        <div>23</div>
                    </div>
                    <br>
                    <p class="hwrite">기초대사량({{this.obmr}}kcal))</p>
                    <progress-bar :height=8 color='#808080' bg-color='#f0f0f0' :show-top-tip=false :percentage="bmr"/>
                     <div class="progress" style="margin-top:0.3%;">
                        <div class="progress-bar progress-bar-danger" role="progressbar" style="width:27%">low</div>
                        <div class="progress-bar progress-bar-success" role="progressbar" style="width:27%">general</div>
                        <div class="progress-bar progress-bar-info" role="progressbar" style="width:46%">high</div>
                    </div>
                    <div class="bar">
                        <div style="width:26%">800</div>
                        <div style="width:26%">1200</div>
                        <div>1600</div>
                    </div>
                    <br>
                </div>
            </div>    
        </div>
        <!-- <div class="chart"></div> -->
        <body-date/>
        </div>
        <main-footer/>
    </div>
</template>

<script>
import ModalUpload from '@/components/page/ModalUpload.vue'
import MainHeader from '@/components/Header.vue'
import BodyDate from '@/components/page/BodyDate.vue'
import MainFooter from '@/components/Footer.vue'
import Loading from '@/components/Loading.vue' 
import axios from 'axios'

// const BackURL = 'http://127.0.0.1:8000/';
export default {
    components:{
        ModalUpload,
        MainHeader,
        BodyDate,
        MainFooter,
        Loading
        // LinearGauge
    },
    data(){
        return{
            fat: 0,
            muscle: 0,
            bmi: 0,
            bmr: 0,
            sex: 0,
            imgSrcGirl : require("../assets/imgs/girl_exam.png"),
            imgSrcMan: require("../assets/imgs/body_exam.png"),
            type: 0,
            ofat: 0,
            omuscle: 0,
            obmi: 0,
            obmr: 0,
        }
    },
    methods:{

    },
    created(){
        let config = { 'Authorization' : 'JWT' + localStorage.getItem("token")  }
        // console.log('=+++++++++++++++++++++' + this.$store.state.Userpk)
        // console.log(localStorage.getItem('userpk'))
        axios.get(`http://127.0.0.1:8000/accounts/checkbody/`
        , { params:{
            pk : localStorage.getItem('userpk')
            }
        }, config)
        .then( res => {
            // console.log(res.data)
            this.type = 1;
            this.sex = res.data.user.gender;
            this.ofat = parseInt(res.data.body.fat*100)/100;
            this.omuscle = parseInt(res.data.body.muscle*100)/100;
            this.obmi = parseInt(res.data.body.bmi*100)/100;
            this.obmr = parseInt(res.data.body.bmr*100)/100;
        if(this.sex==2){
            this.imgSrcMan = "http://127.0.0.1:8000"+res.data.body.bodyImg;
            this.fat = res.data.body.fat/40*100;
            this.muscle= parseInt((res.data.body.muscle-15)/35*10000)/100;
            this.bmi= (res.data.body.bmi-10)/25*100;
            this.bmr= (res.data.body.bmr-1000)/1500*100;
        } else {
            this.imgSrcGirl = "http://127.0.0.1:8000"+res.data.body.bodyImg;
            this.fat = res.data.body.fat/40*100;
            this.muscle= parseInt((res.data.body.muscle-10)/35*10000)/100;
            this.bmi= (res.data.body.bmi-10)/25*100;
            this.bmr= (res.data.body.bmr-800)/1500*100;
        }
        })
        .catch( err => {
            console.log(err)
            this.type = 0;
        })

    },
    mounted(){
        
    }
   
}
</script>

<style lang="scss" scoped>
.bodypage{

}
.write{
    font-size:25px;
    font-family: 'NanumBarunGothic'; 
    font-style: normal;
    font-weight: bold ; 
}
.hwrite{
    font-size:15px;
    font-family: 'NanumBarunGothic'; 
    font-style: normal;
    font-weight: bold ; 
}
.chart{
    margin-bottom: 20%;
    border: 1px solid black;
}
.body_chart{
    margin: 0 auto;
    margin-top:140px;
    overflow:auto;
    position: relative;
    height: 550px;
    width: 95%;
    border-radius: 40px;
    // background: #f5f5f5;
    // background: #edf2f4;
    // background-image: linear-gradient(to top, #fdcbf1 0%, #fdcbf1 1%, #e6dee9 100%);
    // background-image: linear-gradient(to top, #9890e3 0%, #b1f4cf 100%);
    // background-image: linear-gradient(to top, #e6e9f0 0%, #eef1f5 100%);
    // background-image: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
    padding-top: 50px;
}
.container_body{
    width: 70%;
    // height: 100%;
    margin: 3% auto 0 20%;
    
}

    // border: 1px red solid;
.bar > div{
    display: inline-block;
}

.card-5 {
  box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);
}
@import '../assets/sass/body.scss'
</style>