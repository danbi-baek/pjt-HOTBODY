<template>
<div class="Maindiv">
    <loading v-if="$store.state.loadingflag"/>
    <div v-if="!$store.state.loadingflag">
        <div class="div_img1">
            <main-header/>
            <main-chart  v-if="flag==true"/>
        </div>
        <main-daykcal  v-if="flag==true"/>
        <main-footer v-if="flag==true"/>
    </div>
</div>

</template>

<script>
import MainHeader from '@/components/Header.vue'
import MainFooter from '@/components/Footer.vue'
import MainChart from  '@/components/page/MainChart.vue'
import MainDaykcal from  '@/components/page/MainDaykcal.vue'
import {saveHeightToCookie,saveWeightToCookie} from '@/utils/cookies'
import Loading from '@/components/Loading.vue'
import axios from 'axios';

export default {
    components : {
        MainHeader,
        MainFooter,
        MainChart,
        MainDaykcal,
        Loading
    },
    
    created() {

        // console.log(this.$store.state)
        axios.get('http://127.0.0.1:8000/accounts/everybody',{
        params: {
            pk : localStorage.getItem('userpk'),
            date : this.$store.state.clickdate
        }
        })
        .then( res => {
            // console.log('datass')
            // console.log(res.data)
            this.$store.state.mainbmi = res.data.body[0].bmi
            this.$store.state.maindayKcal = res.data.body[0].dayKcal
            this.$store.state.height = res.data.body[0].height
            this.$store.state.weight = res.data.body[0].weight
            this.$store.state.maineat = [res.data.kcal,res.data.car,res.data.pro,res.data.fat]
            saveHeightToCookie(res.data.body[0].height)
            saveWeightToCookie(res.data.body[0].weight)
            
            var limit = res.data.body.length-8
            if(limit<0) limit = res.data.body.length-1
            for(var i = limit , j=0 ; i>=0;i--,j++ ){
                this.tLabel[j] = (res.data.body[i].bodyDate)
                this.tDatas[j] = (res.data.body[i].bmi)
            }

            this.$store.state.chartlabels = this.tLabel
            this.$store.state.chartdatas = this.tDatas
        

            // console.log('CREATED MAIN')
            this.flag = true

        })
        .catch( err => {
            err
        })

    },
    mounted (){
        if(this.$store.state.loadingflag){
            this.$store.state.bodyorfood = 2
            this.intervalid = setInterval(()=>{
                this.$store.state.loadingflag = false;
            }, 5000);
        }
        // console.log('MOUNTED MAIN')
        
    },
    data () {
        return{
            tLabel : [],
            tDatas : [],
            flag: false,
        }
    }

}
</script>

<style scoped>
.Maindiv{
    background: white;

}

.div_img1{
    width: 100%;
    height: auto;
    background-image: url('../assets/imgs/running.jpg');
    background-repeat: no-repeat;
    background-size: cover;
}
</style>