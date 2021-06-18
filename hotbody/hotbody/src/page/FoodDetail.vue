<template>
  <div class="detailpage">
    <main-header/>
    <loading v-if="$store.state.loadingflag" />
    <div class="detailfood">
        <div class="foodinfo">
            <div class="foodimg">
                <img :src="foodTotalImg"/>
            </div>
            
            <div class="foin">
                <div class="eatinfo">
                    <div id="totalKcal">
                        <p>전체 섭취량({{$store.state.detailNut[0]}}Kcal)</p>
                        <p>{{new Date() | moment('YYYY년 MM월 DD일')}}  {{diettype}}</p>
                    </div>
                    <div id="nutriinfo">
                        <div class="info">
                            <p>{{$store.state.detailNut[1]}}g</p>
                            <p>탄수화물</p>
                        </div>
                        <div class="info">
                            <p>{{$store.state.detailNut[2]}}g</p>
                            <p>단백질</p>
                        </div>
                        <div class="info">
                            <p>{{$store.state.detailNut[3]}}g</p>
                            <p>지방</p>
                        </div>
                    </div>
                </div>
                <div class="foodinfos">
                    <div class="foinfo" v-if="getFood.length!=0">
                        <div class="foods" v-for="(food, i) in getFood " :key="i">
                            <div class="foodinfoimg"  @click="writeDetail(i)" >
                                <img class="imgh" :src="'http://127.0.0.1:8000'+food.foodImg"/>
                            </div> 
                            <p class="imgh" @click="writeDetail(i)">{{food.name}}</p>
                            <p><i class="fas fa-times" @click="delFood(i)"></i></p>
                        </div>
                        
                    </div>
                </div>
                <div class="showinfos" v-if="detailOpen">
                    <div id="findfood">
                        <p style="margin: 0;line-height: 42px;"><i class="fas fa-exclamation-triangle" style="color:orange;  "></i>{{detailFood.name}} 이/가 아닌가요?</p>
                        <button @click="foodmodify()">검색하기</button>
                    </div>
                </div>
                <div class="showinfos" v-if="!detailOpen">
                    <div id="findfood">
                        <button @click="show">음식 추가하기</button>
                    </div>
                </div>
            <!-- 여기 써치 모달 !!! -->
            <div id="addectfood" >
                
                <modal name="modal-search"
                height = "auto"
                scrollable= "true"
                >
                <div class="searchbox" >
                    <div>
                        <!-- <i class="fas fa-times fa-2x" style="float:right" @click="hide"/>
                        <input type="text" v-model="word"/> 
                        <button @click="foodsearch">검색하기</button> -->
                        <div class="wrapper" style="margin-left:18%">
                            <div class="input-data" style="width:50%;float:left">
                                <input type="text" @keyup.enter ="foodsearch" v-model="word" required>
                                <div class="underline">
                                </div>
                                <label>food name</label>
                            </div>
                            <!-- <button @click="foodsearch" style="width:60px;height:40px;">검색하기</button> -->
                            <div class="photo div_file" @click="foodsearch" style="width:60px;height:36px;">
                                등록
                            </div>
                        </div>

                    </div>
                    <div v-if="searchOpen">
                        <div v-if="searchInfo.length!=0">
                            <div v-for="(s,i) in searchInfo" :key="i" @click="addFood(i)">
                                <div style="width:120px; height:120px; margin-left:42%;margin-bottom:1%;">
                                    <img :src="'http://127.0.0.1:8000'+s.foodImg" style="cursor:pointer"/>
                                </div>
                                <div style="margin-left:42%;margin-bottom:3%">
                                    {{s.name}} || {{s.kcal}}kcal
                                </div>
                            </div> 
                        </div>
                        <div v-if="searchInfo.length==0" style="font-size:30px;text-align:center;margin-top:10%">
                            찾으시는 음식이 없어요 😂
                        </div>

                    </div>
             
                </div>
                </modal>
            </div>
            <!-- 누르면 상세입력창 .. ㅜ0ㅜ.. -->
        </div>
            <div class="foodamount" v-if="this.tab!=0">
                <div class="amountmenu" v-if="this.tab==1">
                    <div>
                        <div class="amount">
                            <p>먹은 음식 중량(g) 입력</p>
                            <div class="in-line">
                                <input style="text-align:center; width:40%" :value="detailFood.gram" v-on:input="updateInput" type="text"   :v-model="detailFood.gram" placeholder="중량(g)입력" >
                            </div>
                        </div>
                        <div class="values">
                            <p>탄수화물  :  {{Math.round(detailFood.car/100*detailFood.gram*100)/100.00}} g</p>
                            <p>단백질  :  {{Math.round(detailFood.pro/100*detailFood.gram*100)/100.00}} g</p>
                            <p>지방  :  {{Math.round(detailFood.fat/100*detailFood.gram*100)/100.00}} g</p>
                            <p>당분  :  {{Math.round(detailFood.tsg/100*detailFood.gram*100)/100.00}} g</p>
                            <p>칼로리  :  {{Math.round(detailFood.kcal/100*detailFood.gram*100)/100.00}} kcal</p>
                        </div>
                    </div>    
                </div>

                <button class="ubts" @click="gramModify">확인</button>
            </div>
     
        </div>
            <!-- 상세입력 끝 -->
    </div>
        <div class="btns" v-if="!detailOpen">
            <button @click="uploadtodayDiet">
                    등록하기
            </button>
        </div>
    <main-footer/>
</div>
</template>

<script>
import axios from 'axios'
import MainHeader from '@/components/Header.vue'
import MainFooter from '@/components/Footer.vue'
import Loading from '@/components/Loading.vue'
export default {
    components : {
        MainHeader,
        MainFooter,
        Loading
    },
    data() {
        return {
            type: this.$route.params.type,
            tab:0,
            gram:100,
            kcal:0,
            car:0,
            pro:0,
            fat:0,
            tsg:0,
            index: 0,
            getFood: [],
            detailFood : [],
            foodTotalImg : [],
            detailOpen: false,
            searchOpen:false,
            searchInfo : [],
            word:'',
            searchtype:0,
            diettype: '아침'
            
        }
    },
    created () {
        // 0 아침 1 점심 2 저녁 3 간식
            if(this.type=='1'){
               this.diettype = '점심' 
            }else if(this.type==2){
               this.diettype = '저녁' 
            }else if(this.type==3){
                this.diettype = '간식'
            }
            this.getFood = this.$store.state.addFoodList.data

            // console.log(this.getFood)
            this.foodTotalImg = 'http://127.0.0.1:8000' + this.$store.state.addFoodList.img
            this.getNut()
    },
    methods:{
        show() {
            this.$modal.show("modal-search");
        },
        hide() {
            this.searchOpen = false
            this.$modal.hide("modal-search");
        },
        tabChange(num){
            this.tab = num
        },
        updateInput: function(event){
            var updated = event.target.value;
            this.getFood[this.index].gram = updated
        },
        getNut(){
            this.$store.state.detailNut = [0,0,0,0]
            for(var i=0;i<this.getFood.length;i++){
                this.$store.state.detailNut[0] += this.getFood[i].kcal
                this.$store.state.detailNut[1] += this.getFood[i].car
                this.$store.state.detailNut[2] += this.getFood[i].pro
                this.$store.state.detailNut[3] += this.getFood[i].fat
            }

            for(i =0 ; i<4;i++){
                this.$store.state.detailNut[i] = Math.round(this.$store.state.detailNut[i] * 100 )/ 100.00 
            }
        },
        writeDetail(i){
            // 음식 영양소 수정
            // console.log('수정창 오픈')
            this.detailOpen = true
            this.tab = 1
            this.index = i
            this.detailFood = this.getFood[i]
        },
        delFood(i){
            // 음식 삭제
            this.getFood.splice(i,1)
            // console.log('음식삭제````')
            // console.log(this.getFood)
            this.getNut()
            // console.log('-------');
        },
        foodsearch(){
            if(this.word!=''){
            axios.get(`http://127.0.0.1:8000/foods/search`,{
                params: {
                    name : this.word
                }
            })
            .then(res => {
                this.searchOpen = true
                this.searchInfo = res.data
            })
            .catch(res => {
                res
            })                

            }
        }, //foodsearch()

        foodmodify(){
            // console.log("음식 수정 검색")
            this.show()
            this.searchtype = 1
        },  //foodmodify()
        
        addFood(i){
            // console.log(this.searchInfo[i].name +'추가하기')
            if(this.searchtype == 0 ) { //그냥 추가
                this.getFood.push(this.searchInfo[i])
                this.detailOpen = false
            } else if(this.searchtype == 1) { // 수정 추가
                this.getFood[this.index] = this.searchInfo[i]
                this.detailOpen = false
            }
            this.getFood.gram = 100
            this.searchtype = 0
            this.getNut()
            this.hide()
            
        } ,//addFood()

        uploadtodayDiet(){
            axios.post(`http://127.0.0.1:8000/foods/add/`,{
                params: {
                    pk : localStorage.getItem('userpk'),
                    lis : this.getFood,
                    type : this.type,
                    date : this.$store.state.clickdate
                }
            })
            .then(res => {
                res
                this.$store.state.diaryflag = true

                this.$router.push('../../diary')
            })
            .catch(res => {
                res
            })          
        },
        gramModify(){
            //고유 푸드 영양값이 와야함.. 데이터 계속 증가됨 ㅡㅡ
            var gf = this.getFood[this.index]
            var df = this.detailFood
            var dg = this.detailFood.gram

            

            // console.log(this.detailFood)
            gf.kcal = df.kcal /100*dg
            gf.car = df.car /100*dg
            gf.pro = df.pro /100*dg
            gf.fat = df.fat /100*dg
            gf.tsg = df.tsg /100*dg

            this.tab=0
            this.detailOpen = false
            // console.log('modify')
            // console.log(this.getFood.data[this.index])
            this.getNut()
        }        
    }//methods
}
</script>


<style scoped>
i{
    cursor: pointer;
}
button{
    width: 110px;
    height: 5%;
    border:none;
    background-color: pink;
    color: white;
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
.foin{
    
    height: 400px;
}
.detailfood{
   min-height:500px;
   font-weight: bold;
}
/* ------------------------------- */
.foodimg{
    width:30%;
    height:400px;
    border-radius: 40px;
    margin: 0 auto;
    margin-left: 7%;
    float: left;
}
.foinfo{
    /* display: flex; */
    justify-content: center;
    overflow-y: scroll;
    overflow-x: hidden;
}
.isize{
    /* width: 100px;
    height: 100px; */
    background: #5f6982;
    /* border-radius: 30px;
    line-height: 100px; */
}
.eatinfo{
    margin: 25px auto;
    text-align: center;
    width: 50%;
    border-top: 1px solid #f0f0f0;
    padding-top: 15px ;
    display: flex;
    justify-content: center;
    /* background: #f0f0f0; */
    border-bottom: 1px solid #f0f0f0;
}
#totalKcal, #nutriinfo{
    display: inline-block;
}
#totalKcal {
    width:40%;
    font-size:18px;
}
#nutriinfo {
    width: 40%;
}
#nutriinfo .info{
    display: inline-block;
    width: 30%;
}
/* --------------------------- */
.foodinfos{
    margin:0 auto;
    width:60%;
    height:328px;
    text-align: center;
    overflow:auto;
    display: flex;
    justify-content: center
    /* cursor: pointer; */
}

.foods{
    width:fit-content;
    height: fit-content;
    margin: 10px 30px;
    display: inline-block;
}
.foods i , .foods p{
    cursor: pointer;
}
.foodinfoimg{
    width:100px; 
    height:100px;
    border-radius:30px;
}
#addectfood{
    width:60%;
    margin: 4px auto;
    transition: all 0.7s;
}
#addectfood:hover{
    color:gray;
}
#findfood{
    width:60%;
    margin:0 auto;
    margin-top:40px;
    text-align: center;
    display: flex;
    justify-content: center;
}
#findfood>button{
    margin: 0 50px;
    background-color: pink;
    color: white;

}
/* ---------------- */
.foodamount{
    width:80%;
    margin:0 auto;
    margin-top:40px;
    text-align: center;
}
.amounttab{
    width:80%;
    margin: 0 auto;
    text-align: left;
}
.tabp {
    display: inline-block;
    margin:0 10px;
    color:black;
    border-bottom: 3px solid rgb(255, 88, 102);
}
.amountmenu{
    min-height:300px;
    display: flex;
    justify-content: center;
}
.amountmenu>div{
    background: #f0f0f0;
    width: 70%;
    height: 200px;
    padding: 25px;
    margin-top: 100px;
    margin-bottom: 20px;
}
.amount {
    width:30%;
    height:100px;
    line-height:40px;
    display: inline-block;
    margin:10px 10px;
}
.values{
    width:40%;
    float:right;
    text-align: left;
}
.btns{
    width:20%;
    margin:0 auto;
    text-align:center;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}
img {
    width:100%;
    height:100%;
    border-radius: 30px;;
}
.sum{
    background-color: #f0f0f0;
}
.searchOpen{
    height:400px;
    overflow:scroll;
}
@import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');

.wrapper{
  width: 100%;
  background: #fff;
  padding: 30px;
  /* box-shadow: 0px 0px 10px rgba(0,0,0,0.1); */
}
.wrapper .input-data{
  height: 40px;
  width: 100%;
  position: relative;
}
.wrapper .input-data input{
  height: 100%;
  width: 100%;
  border: none;
  font-size: 17px;
  border-bottom: 2px solid silver;
}
.input-data input:focus ~ label,
.input-data input:valid ~ label{
  transform: translateY(-20px);
  font-size: 15px;
  color: #4158d0;
}
.wrapper .input-data label{
  position: absolute;
  bottom: 10px;
  left: 0;
  color: grey;
  pointer-events: none;
  transition: all 0.3s ease;
}
.input-data .underline{
  position: absolute;
  height: 2px;
  width: 100%;
  bottom: 0;
}
.input-data .underline:before{
  position: absolute;
  content: "";
  height: 100%;
  width: 100%;
  background: #4158d0;
  transform: scaleX(0);
  transform-origin: center;
  transition: transform 0.3s ease;
}
.input-data input:focus ~ .underline:before,
.input-data input:valid ~ .underline:before{
  transform: scaleX(1);
}

.div_file {
  color: #5f6982;
}
.photo {
  background-color: #454cad;
    display: inline-block;
    margin: 0.5rem 1.5rem 1rem 1.5rem;
    clear: both;
    font-family: initial;
    text-align: center;
    font-weight: 700;
    font-size: 14px;
    text-decoration: none;
    text-transform: initial;
    border: none;
    border-radius: 0.2rem;
    outline: none;
    padding: 0 1rem;
    height: 36px;
    line-height: 36px;
    color: #fff;
    transition: all 0.2s ease-in-out;
    box-sizing: border-box;
    background: #454cad;
    border-color: #454cad;
    width: 30%;
    cursor: pointer;

    /* &:hover {
      cursor: pointer;
      background-color: #8387b6f1;
    } */
    }                                       

    
  .photo:hover{
       cursor: pointer;
      background-color: #8387b6f1;
  }

.imgh:hover{
  cursor:pointer;
  opacity: 0.5;
}
/* .findfood > p{
    line-height: 42px;
} */
.ubts{
    margin:0;
    margin-bottom:80px ;
}
</style>