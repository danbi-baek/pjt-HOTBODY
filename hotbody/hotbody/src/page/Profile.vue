<template>
  <div class="profilepage">
        <main-header/>
        <div class="userprofile">
            <div class="userinfo">
                <div style="width:100px;height:100px;">
                    <img :src="imgsrc"/>
                </div>
                <h3><b>{{nickname}}</b>님</h3>
            </div>
            
            <div class="infosbox" :class="{'clickedit':edit}" >
                <div class="editbtn">
                    <button v-if="!edit" @click="edit = true">수정</button>
                    <button v-if="edit" @click="profileEdit" >완료</button>
                </div>
                <div>
                    <div class="this.weights" style="width:50%; float:left;">
                        <div class="infos">
                            <div >
                                <label class="element-label" for="nick" style="width:20%">닉네임</label>
                                <output v-if="!edit" id="nick" style="width:50%">{{nickname}}</output>
                                <input v-if="edit" id="nick" placeholder="닉네임을 입력해주세요"  v-model="changeNickname" >
                                <p v-if="err[0]==1 && edit" ref="err0" class="err"></p>
                            </div>
                        </div>
                        <div class="infos">
                            <label class="element-label" for="height" style="width:20%">키</label>
                            <output v-if="!edit" id="height" style="width:50%">{{height}}</output>
                            <input v-if="edit" id="height" placeholder="키를 입력해주세요"  v-model="height" > cm
                            <p v-if="err[1]==1 && edit" ref="err1" class="err"></p>
                        </div>

                        <div class="infos">
                            <label class="element-label" for="weight" style="width:20%">몸무게</label>
                            <output v-if="!edit" id="weight" style="width:50%">{{weight}}</output>
                            <input v-if="edit" id="weight" placeholder="몸무게를 입력해주세요"  v-model="weight" > kg
                            <p v-if="err[2]==1 && edit" ref="err2" class="err"></p>

                        </div>
                    </div>
                    <div class="this.weights" style="width:50%; float:right;">
                        <div class="infos" >
                            <div >
                                <label class="element-label" for="nick" style="width:20%">나이</label>
                                <output style="width:50%">{{age}}</output>
                            </div>
                        </div>
                        <div class="infos" >
                            <div >
                                <label class="element-label" for="nick" style="width:20%">성별</label>
                                <output style="width:50%">{{gender}}</output>
                            </div>
                        </div>
                    </div>
                </div>
                <hr>
                <div  class="activity radios" style="margin-top:25%">
                    <p>활동 상태</p>
                    <div class="innerradios">
                    <div class="radio" :class="{'selected':this.activityVal==1}" >
                    <input v-if="edit" type="radio" v-model="activityVal" id="act1" value="1">
                    <label for="act1">매우 활동적</label>  
                    </div>

                    <div class="radio"  :class="{'selected':this.activityVal==2}">
                    <input v-if="edit" type="radio" v-model="activityVal" id="act2" value="2">
                    <label for="act2">활동적</label>  
                    </div>

                    <div class="radio" :class="{'selected':this.activityVal==3}">
                    <input v-if="edit" type="radio" v-model="activityVal" id="act3" value="3">
                    <label  for="act3">저 활동적</label>  
                    </div>

                    <div class="radio" :class="{'selected':this.activityVal==4}">
                    <input v-if="edit" type="radio" v-model="activityVal" id="act4" value="4">
                    <label  for="act4">비 활동적</label>  
                    </div>
                    </div>
                </div>

                <div class="goals radios">
                    <p>체중 목표</p>
                    <div class="innerradios">
                    <div class="radio" :class="{'selected':this.goalVal==1}">
                    <input v-if="edit" type="radio" v-model="goalVal" id="goal1" value=1>
                    <label  for="goal1">체중 감소</label>  
                    </div>

                    <div class="radio"  :class="{'selected':this.goalVal==2}">
                    <input v-if="edit" type="radio" v-model="goalVal" id="goal2" value=2>
                    <label for="goal2">체중 유지</label>  
                    </div>

                    <div class="radio" :class="{'selected':this.goalVal==3}">
                    <input v-if="edit" type="radio" v-model="goalVal" id="goal3" value=3>
                    <label  for="goal3">체중 증가</label>                      
                    </div>
                    </div>
                </div>
            </div>
        </div>
        <main-footer/>
  </div>
</template>

<script>
import axios from 'axios'
import MainHeader from '@/components/Header.vue'
import MainFooter from '@/components/Footer.vue'
// import ModalEdit from '@/components/page/ModalEdit.vue'

export default {
    components : {
        MainHeader,
        MainFooter,
        // ModalEdit
    },
    data() {
        return {
          nickname: '',
          changeNickname: '',
          edit: false,
          activityVal : 1,
          goalVal : 1,
          age : 0,
          gender : '',
          height: 0,
          weight : 0,
          err : [0,0,0],
          sendState : [true,true,true],
          imgsrc: localStorage.getItem('userImg')
        }
    },
    watch:{
        changeNickname(){
            // console.log(this.changeNickname.length)
            if(this.changeNickname.length-1<1){
                this.err[0] = 1
                this.sendState[0] = false
                this.$refs.err0.innerText = '닉네임을 입력해 주세요'
            }else {
                this.err[0] =0
                this.sendState[0] = true
            }
        },
        height() {
            this.checkHeight()
        },
        weight () {
            this.checkWeight()
        }
    },
    methods:{
        profileEdit(){
            if(this.sendState[0]==false) alert('닉네임을 확인하세요')
            else if(this.sendState[1]==false) alert('키를 확인하세요')
            else if(this.sendState[2]==false) alert('몸무게를 확인하세요')
            else {
                // console.log(this.nickname+','+this.height+','+this.weight+','+this.goalVal+this.activityVal)
                axios.put('http://127.0.0.1:8000/accounts/updated/',{ 
                    params:{
                        pk : localStorage.getItem('userpk'),
                        nickname : this.nickname,
                        height : this.height,
                        weight : this.weight,
                        goal : this.goalVal,
                        activity : this.activityVal
                        }
                    },
                )
                .then(res => {
                    this.activityVal = res.data.user.activity
                    this.goalVal = res.data.user.goal
                    this.nickname = res.data.user.nickname
                    this.changeNickname = res.data.user.nickname
                    this.age = res.data.user.age
                    this.height = res.data.body.height
                    this.weight = res.data.body.weight
                    if(res.data.user.gender==1) this.gender = '여성'
                    else if(res.data.user.gender==2) this.gender = '남성'
                    // console.log(res.data)
                })
                .catch(res => {
                    res
                })                
                alert('프로필 수정 완료')
                this.edit = false
            }
        },
        checkHeight(){
        var spn;
        var tempp = this.$refs.err1;
        if (this.height[0] == "0") {
            this.height = this.height.substring(1, 5);
        }
        var tmp = Number(this.height);
        if (isNaN(tmp) || tmp < 1) {
            this.height = String("");
        }
        if (this.height.indexOf(".") == -1) {
            spn = this.height.length;
            if (spn > 3) {
                this.err[1] = 1
                this.sendState[1] = false
                tempp.innerHTML = "키가 3자리를 넘습니다. 다시확인해주세요.";
            } else if (spn == 3) {
                this.err[1] = 0
                this.sendState[1] = true
                
            } else if (spn == 2) {
            if (tmp < 80) {
                this.err[1] = 1
                this.sendState[1] = false
                tempp.innerHTML = "키는 80을 넘어야 합니다.";
            } else {            
                this.err[1] = 0
                this.sendState[1] = true
            }
            } else {
                this.err[1] = 1
                this.sendState[1] = false
                tempp.innerHTML = " 키는 80을 넘어야 합니다.";
            }
        } else {
            var sp = this.height.split(".");
            spn = sp.length - 1;

            if (sp[0].length > 3) {
                this.err[1] = 1
                this.sendState[1] = false
                tempp.innerHTML = "키 3자리를 넘습니다. 다시확인해주세요.";
            } else if (sp[0].length == 3) {
                this.err[1] = 0
                this.sendState[1] = true
            } else if (sp[1].length > 1) {
                this.err[1] = 1
                this.sendState[1] = false          
                tempp.innerHTML = "소수점은 한자리만 입력해주세요.";
            } else if (spn > 1) {
                this.err[1] = 1
                this.sendState[1] = false
                tempp.innerHTML = "콤마가 1개가 넘습니다!!";
            } else {
            if (tmp <= 30) {
                this.err[1] = 1
                this.sendState[1] = false
                tempp.innerHTML = "키를 잘못 입력된거 같습니다.";
            } else if (isNaN(tmp)) {
                this.err[1] = 1
                this.sendState[1] = false
                tempp.innerHTML = "키를 입력해주세요";
            } else {
                this.err[1] = 0
                this.sendState[1] = true
            }
            }
            }
        },// checkHeight
        checkWeight(){
        var spn;
        var tempp = this.$refs.err2;
        if (this.weight[0] == "0") {
            this.weight = this.weight.substring(1, 5);
        }
        var tmp = Number(this.weight);
        if (isNaN(tmp) || tmp < 1) {
            this.weight = String("");
        }
        if (this.weight.indexOf(".") == -1) {
            spn = this.weight.length;
            if (spn > 3) {
                this.err[2] = 1
                this.sendState[2] = false
                tempp.innerHTML = "몸무게가 3자리를 넘습니다. 다시확인해주세요.";
            } else if (spn == 3) {
                this.err[2] = 0
                this.sendState[2] = true
                
            } else if (spn == 2) {
            if (tmp < 30) {
                this.err[2] = 1
                this.sendState[2] = false
                tempp.innerHTML = "몸무게는 30을 넘어야 합니다.";
            } else {            
                this.err[2] = 0
                this.sendState[2] = true
            }
            } else {
                this.err[2] = 1
                this.sendState[2] = false
                tempp.innerHTML = " 몸무게는 30을 넘어야 합니다.";
            }
        } else {
            var sp = this.weight.split(".");
            spn = sp.length - 1;

            if (sp[0].length > 3) {
                this.err[2] = 1
                this.sendState[2] = false
                tempp.innerHTML = "몸무게가 3자리를 넘습니다. 다시확인해주세요.";
            } else if (sp[0].length == 3) {
                this.err[2] = 0
                this.sendState[2] = true
            } else if (sp[1].length > 1) {
                this.err[2] = 1
                this.sendState[2] = false          
                tempp.innerHTML = "소수점은 한자리만 입력해주세요.";
            } else if (spn > 1) {
                this.err[2] = 1
                this.sendState[2] = false
                tempp.innerHTML = "콤마가 1개가 넘습니다!!";
            } else {
            if (tmp <= 30) {
                this.err[2] = 1
                this.sendState[2] = false
                tempp.innerHTML = "몸무게가 잘못 입력된거 같습니다.";
            } else if (isNaN(tmp)) {
                this.err[2] = 1
                this.sendState[2] = false
                tempp.innerHTML = "몸무게를 입력해주세요";
            } else {
                this.err[2] = 0
                this.sendState[2] = true
            }
            }
        }
        }//checkWeight
    },
    created(){
        // console.log(this.$store.state)
        axios.get(`http://127.0.0.1:8000/accounts/userinfo/${localStorage.getItem('userpk')}`)
        .then(res => {
            // console.log(res.data)
            this.activityVal = res.data.user.activity
            this.goalVal = res.data.user.goal
            this.nickname = res.data.user.nickname
            this.changeNickname = res.data.user.nickname
            this.age = res.data.user.age
            this.height = res.data.body.height
            this.weight = res.data.body.weight
            if(res.data.user.gender==1) this.gender = '여성'
            else if(res.data.user.gender==2) this.gender = '남성'
        })
        .catch(res => {
            res
        })
    }
}
</script>

<style scoped>

@font-face { 
    font-family: 'TmoneyRoundWindExtraBold'; 
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/TmoneyRoundWindExtraBold.woff') format('woff'); 
    font-weight: normal;
    font-style: normal; 
}
@font-face { 
    font-family: 'TmoneyRoundWindRegular'; 
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/TmoneyRoundWindRegular.woff') format('woff');
    font-weight: normal;
    font-style: normal; 
  }
*{
    font-family: 'TmoneyRoundWindRegular'; 
    font-weight: normal;
    font-style: normal; 
}

.userprofile{
    min-height: 600px;
    width:50%;
    margin:0 auto;
    margin-bottom:250px;
}
.userinfo{
    margin-bottom:30px;
}
img{
    width:100%;
    height:100%;
    border-radius: 100px;
}
/* .infosbox *{
    border:1px solid black;
} */
.editbtn{
    width:100%;
    height:40px;
    font-weight:bold;
}
.editbtn button{
    height: 30px;
    width:50px;
    float:right;
    border-radius:20px;
    color:black;
    transition:all 0.6s;
    border:none;
}
.editbtn button:hover{
    opacity:0.8;
}
.this.weights{
    margin-bottom:10px;
}
.infos{
    margin-bottom:15px;
}
.infos label{
    width:10%;
}
.infos output,.infos input{
    height:40px;
    width: 20%;
    font-size:18px;
    text-align:center;
    display:inline-block;
    border:none;
}
input:checked+label{
  color: rgb(255, 88, 102);
  font-weight: bolder;
  background:none;
}
label,p {
    font-size:18px;
    font-weight:bold;
    padding-left:10px;
    /* font-family: "AlternateGotNo2D", "Helvetica Neue", "Helvetica", sans-serif; */
}
.innerradios{
    height:60px;
    text-align:center;
    /* border:1px solid red; */
}
.radios{
    /* border:1px solid green; */
    margin-bottom:30px;
    height:200px;
}
.radios p {
    border-bottom:1px solid #f0f0f0;
    padding-bottom:10px;
    margin-top:30px;
    margin-bottom:30px;
}
.radio label{
    height:30px;
    line-height:30px;
}
.activity .radio{
    width:25%;
    display:inline-block;
    text-align:center;
    margin:0 auto;
}
.goals .radio{
    width:30%;
    display:inline-block;
    text-align:center;
    margin:0 auto;

}
.radio label{
    font-size: 14px;
    padding-left:0px;
}
/* error */
.err{
    font-size:9px;
    color:red;
    width:50%;
    margin:0 auto;
    margin-top:6px;
    padding-left:80px;
    
}
/* BIND CSS */
.selected {
    background:rgb(255, 88, 102);
    height:40px;
    line-height:40px;   
    border-radius: 20px;
    color:white;
}
.clickedit  .selected{ 
    background: white;
}
.clickedit input{
    /* border-radius: 10px;  */
    border-bottom:1px solid #dddbdb;
}
.clickedit .editbtn button{
    height: 30px;
    width:50px;
    float:right;
    border-radius:20px;
    background:rgb(255, 88, 102);
    color:white;
    transition:all 0.6s;
    border:none;
}
/* radio... */
input[type='radio'] {
-webkit-appearance:none;
width:16px;
height:16px;
border:0.5px solid darkgray;
border-radius:50%;
outline:none;
position: absolute;
top:4px;
}
input[type='radio']:before {
content:'';
display:block;
width:60%;
height:60%;
margin: 20% auto;  
border-radius:50%;  

}
input[type='radio']:checked{
border:none;
background:rgb(255, 88, 102);
}
input[type='radio']:checked:before {
content: '✔';
position: absolute;
left:3px;
bottom:7px;
color:whitesmoke;
}
/* .lf{
    width:30%;
    float:left;
}
.rg{
    width:30%;
    float:right;
} */
</style>