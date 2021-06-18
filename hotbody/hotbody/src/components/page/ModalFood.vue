<template>
  <div class="register-container">
    <div class="showdate">
      <p id="one">{{$store.state.clickdate | moment('YYYY년 MM월 DD일')}}</p>
      <p id="one" v-if="$store.state.isToday">오늘</p>
      <modal-memo/>
      
    </div>
    <div v-for="(item,i) in foodImgs" :key="i" class="one_fourth" >
    <!-- 식단 기록 없는 친구 -->
    
      <div class="button-container" v-if="!$store.state.Eatstate[i]">
         <div class="div_add" @click="show(item.type)" v-if="$store.state.isToday"  style="cursor: pointer;">
           <div class="food_text" >
             {{item.day}}추가
              <br>
              <i class="fas fa-plus"></i>
           </div>
         </div>
          <img :src="item.img"/>
      </div>

    <!-- 식단 기록 있는 친구 -->
      <div class="button-container" v-if="$store.state.Eatstate[i]" @click="goDetail(i)" style="cursor:pointer;">
          <img :src="$store.state.Eatimg[i]"/>
      </div>

      <div class="dayKcal"><p>{{$store.state.EatKcal[i]}}</p> Kcal</div>
    </div>
    <modal name="modal-upload"
      height = "400"
      @before-open="beforeOpen"
    >
      
      <!-- Upload  -->
      <form id="file-upload-form" class="uploader" style="margin-top:50px;">
        <div v-if="!image">
          <div class="noimg-body">
            <label for="file-upload" id="not_img" ref="dropbox"><br>
              <p>300kb이하이며 한글이 포함되지 않은 이미지로 올려주세요😂</p>
              <div id="start" style="padding-top:90px;">
                <!-- <i class="fa fa-download" aria-hidden="true"></i> -->
                 <i class="fa fa-download" aria-hidden="true"></i>
                <!-- </div> -->
              </div>
            </label>
          </div>
          <div class="file_info">
            <div class="div_file">식단을 추가해주세요</div>
            <!-- <div id="notimage" >Please select an image</div>  -->
            <!-- <div id="file-upload-btn" class="btn btn-primary" @change="onFileChange"> -->
            <div>
              <input
                type="file"
                id="photo"
                accept="image/*"
                @change="onFileChange"
              />
              <label for="photo" class="photo div_file">파일 업로드</label>
            </div>
          </div>
        </div>
        <div v-else>
          <div class="img-body">
            <label
              class="food-upload"
              for="file-upload"
              id="file-drag"
              ref="dropbox"
            >
              <img :src="image" class="img_upload" />
            </label>
          </div>
          <div class="file_info">
            <div class="flexs">
              <div class="photo div_file" @click="removeImage">
                취소
              </div>
              <div class="photo div_file" @click="foodRegister">
                등록
              </div>
            </div>
          </div>
        </div>
      </form>
    </modal>
  </div>
</template>

<script>
import ModalMemo from '@/components/page/ModalMemo.vue'
import axios from "axios";
export default {
  components : {
    ModalMemo
  },
  created () {
  },
  data() {
    return{
      image: "",
      files: "",
      foodImgs: [ { day : '아침', img : require("../../assets/imgs/breakfast.jpg"), type: 0 },
                 { day : '점심', img : require("../../assets/imgs/lunch.jpg"), type: 1},
                 { day : '저녁', img : require("../../assets/imgs/dinner.jpg"), type: 2},
                 { day : '간식', img : require("../../assets/imgs/cookie.jpg"), type: 3},  

      ],
      
    }
  },
  methods: {
    show(e) {
      this.$store.state.type = e
      // console.log('식사 타입은??'+this.$store.state.type )
      this.$modal.show("modal-upload");
    },
    hide() {
      this.image = ""
      this.$modal.hide("modal-upload");
    },
    beforeOpen(){
      this.image = ""
    },
    onFileChange(e) {
      //이미지 첨부

      var files = e.target.files || e.dataTransfer.files;

      if (!files.length) return;
      // console.log(files[0])
      if(files[0].size>300000) {
          this.image="";
          this.hide();
          alert('300kb이하 이미지로 올려주세요');
          return;
        } 
      var check = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/;
      if(check.test(files[0].name)) {
        this.imgae="";
        this.hide();
        alert('한글이 포함되지 않은 이미지로 올려주세요');
        return;
      }

      this.createImage(files[0]);
      this.files = e.target.files[0];
    },
   createImage(file) {
      //이미지 가져오기
      // console.log('경로'+file.name)
      this.fileName = file.name;
      var reader = new FileReader();
      var vm = this;

      reader.onload = (e) => {
        vm.image = e.target.result;
        // console.log('imggggg')
        // console.log(this.image)
      };
      reader.readAsDataURL(file);
    },
    removeImage: function() {
      this.image = "";
      this.fileName = "";
    },
    foodRegister(){
      this.$store.state.bodyorfood = 0
      let data = new FormData();
      // console.log('타입은!!' + this.$store.state.type)
      data.append('name', 'food-picture')
      data.append('file', this.files)
      data.append('pk', localStorage.getItem('userpk'))
      data.append('date', new Date().toISOString().substring(0,10))
      data.append('type', this.$store.state.type )
      let config = {
          header : {
              'Content-Type'   : 'multipart/form-data',
              'Authorization' : 'JWT' + localStorage.getItem("token")
           }
      }

      axios.post('http://127.0.0.1:8000/foods/upload/',
        data,
        config)
        .then( res => {
          // console.log('결과...')
          // console.log(res.data)
          window.scrollTo(0, 0)
          this.$store.state.addFoodList = res.data
          
          this.intervalid = setInterval(()=>{
            this.$store.state.loadingflag = false;

          }, 3000);

          this.hide()
            this.$router.push('../detail/'+this.$store.state.type)
          this.$store.state.loadingflag = true

        })
        .catch( err => {
          alert('음식 등록 중 에러 발생' + err)
          // console.log(err)
        })
    }, //foodregister
    goDetail(type){
      window.scrollTo(0, 0)
      localStorage.setItem('d',this.$store.state.clickdate)
      this.$router.push('../redetail/'+type)
    }

  }
}
</script>

<style lang="scss" scoped>
.register-container{
    // border: 1px solid red;
    width: 130vh;
    height: 100vh;
    margin: 10% auto;
    padding-left: 20px;
    margin-bottom:400px;
}
.showdate{
  font-weight: bold;
  height: 130px;
  padding-bottom:30px;
}
#one{
  font-family: 'NanumBarunGothic'; 
  font-style: normal;
  font-weight: bold ; 
  font-size:26px;
  text-align: center;
  margin-bottom:30px;
}
.dayKcal{
  font-family: 'NanumBarunGothic'; 
  font-style: normal;
  font-weight: bold ; 
  margin-top:10px;
  font-size:18px;
  
}
.dayKcal p{
  font-family: 'NanumBarunGothic'; 
  font-style: normal;
  font-weight: bold ; 
  display: inline-block;
}
.button-images {
  max-width: 950px;
  margin: 75px auto;
  
}

@import "@/assets/sass/register.scss";
</style>

