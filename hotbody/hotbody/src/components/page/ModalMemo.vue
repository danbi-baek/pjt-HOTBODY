<template>
  <div >
    <div class="btn_memo" @click="show">📝하루일기</div>
    <modal name="modal-memo"
      height = "400"
      width = "450"
    
    >
      <div class="memobox">
        <div class="postit yellow">
            <div class="tape" ref="clickdate">{{$store.state.clickdate | moment('YYYY-MM-DD')}}</div>
            <div class="memobtns">
                <i class="fas fa-check memowrite" @click="memoWrite"></i>
                <i class="fas fa-trash-alt memotrash" @click="memoDel"></i>
            </div>
                <textarea v-model="$store.state.memoInput"></textarea>
        </div>  
      </div>
    </modal>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return{
        clickdate : '',
    }
  },
  methods: {
    show() {
      this.$modal.show("modal-memo");
    },
    hide() {
      this.$modal.hide("modal-memo");
    },
     memoWrite(){
            if(this.$store.state.memoInput!=''){
            axios.get('http://127.0.0.1:8000/foods/diary/',{ 
                params:{
                    pk : localStorage.getItem('userpk') ,
                    date : this.$refs.clickdate.innerText
                    }
                },
            )
            .then((res) => {
                //update
                res.data
                axios.put('http://127.0.0.1:8000/foods/diary/',{ 
                    params:{
                        pk : localStorage.getItem('userpk') ,
                        date : this.$refs.clickdate.innerText,
                        memo : this.$store.state.memoInput
                        }
                    },
                )
                .then((res) => {
                    alert('메모 수정')
                    this.hide()
                    res
                })
                .catch((res) => {
                    res
                });
            })
            .catch((res) => {
                //post
                res
                axios.post('http://127.0.0.1:8000/foods/diary/',{ 
                    params:{
                        pk : localStorage.getItem('userpk') ,
                        date : this.$refs.clickdate.innerText,
                        memo: this.$store.state.memoInput
                        }
                    },
                )
                .then((res) => {
                    alert('메모 등록^_<')
                    // console.log(res);
                    res
                    this.hide()
                    location.reload()
                })
                .catch((res) => {
                    console.log(res);
                });
            });

            }
                

        },
        memoDel(){
            axios.delete('http://127.0.0.1:8000/foods/diary/',{ 
                params:{
                    pk : localStorage.getItem('userpk') ,
                    date : this.$refs.clickdate.innerText,
                    }
                },
            )
            .then((res) => {
                alert('메모 삭제')
                res
                this.hide()
                location.reload()
                this.$store.commit('getMemo','')
            })
            .catch((res) => {
                res
            });
        }
  }
}
</script>

<style  scoped>
.btn_memo{
  font-family: 'NanumBarunGothic'; 
  font-style: normal;
  font-weight: bold ; 
  float:right;
  cursor: pointer;
  /* text-decoration: underline #fff06c; */
  background:#fff06c97;
}
.memobtns{
    float:right;
}
.memobtns i {
    margin-right:15px;
    cursor:pointer;
    transition: all 0.4s;
}
.memowrite:hover{
    color:green;
}
.memotrash:hover{
    color:red;
}
.postit {
  background: #fff;
  height:100vh;
  /* margin: 60px auto; */
  padding: 10px;
  box-shadow: 0px 10px 10px rgba(0, 0, 0, 0.2);
  color: #424242;
}
textarea{
    width:100%;
    height:40%;
    resize:none;
}
textarea,.yellow{
    background: #FFF9C4;
    border:1px solid #FFF9C4;   
}
.tape {
  margin: 0 auto 10px;
  width: 200px;
  height: 40px;
  background: rgba(251, 251, 225, 0.707);
  -webkit-box-shadow: 0px 1px 3px rgba(0,0,0,0.4);
  -moz-box-shadow: 0px 1px 3px rgba(0,0,0,0.4);
  box-shadow: 0px 1px 3px rgba(0,0,0,0.4);
  text-align: center;
  line-height: 40px;
  font-weight: bold;
  color: #424242;
}
</style>
