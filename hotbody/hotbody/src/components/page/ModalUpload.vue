<template>
  <div>
    <div class="btn_body" @click="show">바디측정</div>
    <modal name="modal-upload"
      height = "500"
      @before-open="beforeOpen"
    >
     
      <!-- Upload  -->
      <form id="file-upload-form" class="uploader" style="margin-top:40px;">
        <div v-if="!image">
          <div class="noimg-body">
            <label for="file-upload" id="file-drag-not_img" ref="dropbox"><br>
            <p>한글이 포함되지 않은 이미지로 올려주세요😂</p>
              <div id="start">
                <!-- <i class="fa fa-download" aria-hidden="true"></i> -->
                <img v-if="$store.state.gender == 1" class="body_exam" src="../../assets/imgs/girl_exam.png">
                <img v-if="$store.state.gender == 2" class="body_exam" src="../../assets/imgs/body_exam.png" />
                 <!-- </div> -->
              </div>
            </label>
          </div>
          <div class="file_info">
            <div class="div_file">보다 정확한 결과를 위하여 위 예시처럼 사진을 찍어주세요!📸</div>
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
              class="file-upload"
              for="file-upload"
              id="file-drag"
              ref="dropbox"
            >
              <img :src="image" class="img_upload" />
            </label>
          </div>
          <div class="file_info">
            <div>
              <input
                class="answer"
                v-model="height"
                id="height"
                type="text"
                maxlength="5"
                placeholder="키를 입력하세요"
              />
              <span class="answer_unit">cm</span>
            </div>
            <div>
              <div class="check">{{ heicheck }}</div>
            </div>
            <div>
              <input
                class="answer"
                v-model="weight"
                id="weight"
                type="text"
                maxlength="5"
                placeholder="몸무게를 입력하세요"
              />
              <span class="answer_unit">kg</span>
            </div>
            <div>
              <div class="check">{{ weicheck }}</div>
            </div>
            <div class="flexs">
              <div class="photo div_file" @click="removeImage">
                취소
              </div>
              <div class="photo div_file" @click="bodyRegister">
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
import axios from "axios";
export default {
  components : {
  },
  data() {
    return {
      image: "",
      height: "",
      weight: "",
      fileName: "",
      files: "",
      heicheck: "키는 80이상 입력해주세요",
      weicheck: "몸무게는 30이상을 입력해주세요",
    };
  },
  methods: {
    show() {
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
    heightFail: function(text) {
      var spn;
      if (text[0] == "0") {
        text = text.substring(1, 5);
        this.height = text;
      }

      var len = text.length;
      if (
        (text[len - 1] < "0" || text[len - 1] > "9") &&
        text[len - 1] != "."
      ) {
        text = text.substring(0, len - 1);
        this.age = text;
      }

      var tmp = Number(text);
      if (text.indexOf(".") == -1 && (isNaN(tmp) || tmp < 1)) {
        this.height = String("");
      }
      if (text.indexOf(".") == -1) {
        spn = text.length;
        if (spn > 3) {
          this.heicheck = "키가 3자리를 넘습니다. 다시확인해주세요.";
        } else if (spn == 3) {
          this.heicheck = "";
        } else if (spn == 2) {
          if (tmp < 80) {
            this.heicheck = "키는 80을 넘어야 합니다.";
          } else {
            this.heicheck = "";
          }
        } else {
          this.heicheck = "키는 80을 넘어야 합니다.";
        }
      } else {
        var sp = text.split(".");
        spn = sp.length - 1;

        if (sp[0].length > 3) {
          this.heicheck = "키가 3자리를 넘습니다. 다시확인해주세요.";
        } else if (sp[0].length == 3) {
          this.heicheck = "";
        } else if (sp[1].length > 1) {
          this.heicheck = "소수점은 한자리만 입력해주세요.";
        } else if (spn > 1) {
          this.heicheck = "콤마가 1개가 넘습니다!!";
        } else {
          if (tmp <= 80) {
            this.heicheck = "키가 잘못 입력된거 같습니다...";
          } else if (isNaN(tmp)) {
            this.heicheck = "키를 입력해주세요.";
          } else {
            this.heicheck = "";
          }
        }
      }
    },
    weightFail: function(text) {
      var spn;
      if (text[0] == "0") {
        text = text.substring(1, 5);
        this.weight = text;
      }
      var tmp = Number(text);
      if (isNaN(tmp) || tmp < 1) {
        this.weight = String("");
      }
      if (text.indexOf(".") == -1) {
        spn = text.length;
        if (spn > 3) {
          this.weicheck = "몸무게가 3자리를 넘습니다. 다시확인해주세요.";
        } else if (spn == 3) {
          this.weicheck = "";
        } else if (spn == 2) {
          if (tmp < 30) {
            this.weicheck = "몸무게는 30을 넘어야 합니다.";
          } else {
            this.weicheck = "";
          }
        } else {
          this.weicheck = " 몸무게는 30을 넘어야 합니다.";
        }
      } else {
        var sp = text.split(".");
        spn = sp.length - 1;

        if (sp[0].length > 3) {
          this.weicheck = "몸무게가 3자리를 넘습니다. 다시확인해주세요.";
        } else if (sp[0].length == 3) {
          this.weicheck = "";
        } else if (sp[1].length > 1) {
          this.weicheck = "소수점은 한자리만 입력해주세요.";
        } else if (spn > 1) {
          this.weicheck = "콤마가 1개가 넘습니다!!";
        } else {
          if (tmp <= 30) {
            this.weicheck = "몸무게가 잘못 입력된거 같습니다.";
          } else if (isNaN(tmp)) {
            this.weicheck = "몸무게를 입력해주세요";
          } else {
            this.weicheck = "";
          }
        }
      }
    },
        bodyRegister(){
          if(this.heicheck != "" || this.weicheck != "" ){
            alert("키와 몸무게를 입력해주세요.");
            return
          }
          // console.log(this.fileName)
          let data = new FormData();
          data.append('name', 'body-picture');
          data.append('file', this.files);
          data.append('pk', localStorage.getItem('userpk'))
          data.append('height', this.height)
          data.append('weight', this.weight)
          data.append('img', this.fileName)
          let config = {
              header : { 
                'Content-Type'   : 'multipart/form-data',
                'Authorization' : 'JWT' + localStorage.getItem("token")
           }
          }
          // console.log('데이터')
          // console.log(data)
          // for (var key of data.keys()) {
          //   console.log(key);
          // }

          // for (var value of data.values()) {
          //   console.log(value);
          // }

          axios.post('http://127.0.0.1:8000/accounts/bodyupload/',
            data  
          ,config)
          .then( res => {
            res
            this.$store.state.bodyorfood = 1
            this.intervalid = setInterval(()=>{
              this.$store.state.loadingflag = false;
              location.reload()
          }, 3000);
            // alert('결과를 확인해 보세요')
            // this.$router.push('/body')
            this.hide()
            this.$store.state.loadingflag = true;
          })
          .catch( err => {
            err
          })
        }
        
    
  },
  watch: {
    height: function() {
      this.heightFail(this.height);
    },
    weight: function() {
      this.weightFail(this.weight);
    },
  },
};
</script>

<style lang="scss" scoped>
.noimg-body {
  height: 350px;
}
.img-body {
  height: 280px;
}
.flexs {
  display: flex;
  justify-content: center;
}
.answer {
  width: 300px;
  height: 30px;
}
.file_info > div {
  margin: 2px 0;
}
.file-upload {
  width: 50px;
  height: 500px;
}
.div_file {
  color: white;
}
@import "@/assets/sass/upload.scss";
</style>
