<template>
  <div class="diarypage">
        <main-header/>
        <div class="mydiarycal" >
            <v-calendar 
                :is-expanded=true
                @dayclick="clickday"
                :attributes="attributes"
            />
        </div>
        <modal-food></modal-food>
    <main-footer/>
  </div>
</template>

<script>
import axios from 'axios'
import MainHeader from '@/components/Header.vue'
import MainFooter from '@/components/Footer.vue'
import ModalFood from '@/components/page/ModalFood.vue'

export default {
    components : {
        MainHeader,
        MainFooter,
        ModalFood,
    },
    methods:{
        clickday(day){
            this.$store.state.clickdate = day.id
            if(day.id == (new Date().toISOString().substring(0,10))){
                this.$store.state.isToday = true
                // console.log('오늘임')
            }else this.$store.state.isToday = false
            axios.get('http://127.0.0.1:8000/foods/date/',{ 
                params:{
                    date : day.id,
                    pk : localStorage.getItem('userpk') 
                    }
                },
            )
            .then( res => {
                // console.log(res.data)

                this.$store.state.Eatstate = [false,false,false,false]
                this.$store.state.Eatimg = ['','','','']
                this.$store.state.EatKcal = [0,0,0,0]

                // 메모
                if(res.data.memo.length>0){
                    this.$store.commit('getMemo',res.data.memo[0].memo)
                    // console.log('today memo : '+this.$store.state.memoInput)
                }
                else this.$store.commit('getMemo','')

                // 식단  
                for(var i=0;i<res.data.EatImg.length;i++){
                    var num = res.data.EatImg[i].whenEat
                    this.$store.state.Eatstate[num] = true
                    this.$store.state.Eatimg[num] = 'http://127.0.0.1:8000'+res.data.EatImg[i].eatImg
                }
                // console.log(this.$store.state.Eatimg)

                // 칼로리 
                this.$store.state.EatKcal = [res.data.morning,res.data.lunch,res.data.dinner,res.data.snack]

            })
            .catch( err => {
                err
            })     
        }// clickday
    },
    created(){
        this.clickday({ id : new Date().toISOString().substring(0,10)})
        var today = new Date().toISOString().substring(0,7)
        var dietdate = ''
        var bodyfatdate = ''
        var memodate = []

        axios.get('http://127.0.0.1:8000/foods/month/',{ 
            params:{
                month : today,
                pk : localStorage.getItem('userpk') 
                }
            },
        )
        .then( res => {
            // console.log(res.data)
            for(var i=0;i<res.data.all_body_data.length;i++){
                var monthOnday = res.data.all_body_data[i].bodyDate
                bodyfatdate += monthOnday +','
            }    
            if(bodyfatdate == ''){
                bodyfatdate = null
            }
            for(i=0;i<res.data.all_food_data.length;i++){
                monthOnday = res.data.all_food_data[i].date
                dietdate += monthOnday +','
            }
            if(dietdate == ''){
                dietdate = null
            }
            for(i=0;i<res.data.all_memo_data.length;i++){
                monthOnday = res.data.all_memo_data[i].diaryDate
                memodate[i] = monthOnday 
            }
            if(memodate == ''){
                memodate = null
            }
            // console.log('메모 확인')
            // console.log(memodate)
            
            // console.log('date?? ' +bodyfatdate)
            // console.log(dietdate)
            // console.log((memodate))
            this.attributes.push({
                dot:{
                    color:'red',
                    class:'눈바디',
                },
                popover:{
                    label:'눈바디'
                },
                dates : 
                   bodyfatdate
                
                },{
                dot:{
                    color:'green',
                    class:'식단',
                },
                popover:{
                    label:'식단'
                },
                dates : dietdate
                },{
                dot:{
                    color:'yellow',
                    class:'메모',
                },
                popover:{
                    label:'메모'
                },
                dates : memodate
                })

            // console.log(this.attributes)
        })
        .catch( err => {
            err
        })
    },
    data(){
        return{
        attributes: [],
        }
    },//data
}
</script>

<style scoped>

.mydiarycal {
    margin:0 auto;
    width:60%;
}
.vc-container {
  --day-content-height : 80px;
  --day-content-width : 80px;
}
</style>