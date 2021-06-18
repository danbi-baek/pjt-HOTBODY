<template>
  <div>
    <div class="btn_upload" @click="show">사진 업로드</div>
    <modal name="modal-upload" height="500" @before-open="beforeOpen">
      <!-- Upload  -->
      <form id="file-upload-form" class="uploader" style="margin-top:50px;">
        <div v-if="!image">
          <div class="noimg-body">
            <label for="file-upload" id="not_img" ref="dropbox">
              <div id="start" style="padding-top:90px;">
                <i class="fa fa-download" aria-hidden="true"></i>
              </div>
            </label>
          </div>
          <div class="file_info">
            <div class="div_file">사진업로드하세요</div>
            <!-- <div id="notimage" >Please select an image</div>  -->
            <!-- <div id="file-upload-btn" class="btn btn-primary" @change="onFileChange"> -->
            <div>
              <input
                type="file"
                id="photo"
                accept="image/*"
                @change="onFileChange"
              />
              <label for="photo" class="photo div_file">업로드</label>
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
              <div class="photo div_file" @click="noticeRegister">
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
export default {
  methods: {
    show() {
      this.$modal.show("modal-upload");
    },
    hide() {
      this.image = "";
      this.$modal.hide("modal-upload");
    },
    beforeOpen() {
      this.image = "";
    },
    onFileChange(e) {
      //이미지 첨부

      var files = e.target.files || e.dataTransfer.files;

      if (!files.length) return;
      // console.log(files[0])
      this.createImage(files[0]);
      this.files = e.target.files[0];
    },
    createImage(file) {
      //이미지 가져오기
      // console.log('경로'+file.name)
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
    },
    noticeRegister() {
      this.$store.state.noticeImg = this.files;
      // console.log("사진 ");
      // console.log(this.$store.state.noticeImg);
      this.image = "";
      this.hide();
    },
  },
  data() {
    return {
      image: "",
      files: "",
    };
  },
};
</script>

<style lang="scss" scoped>
$theme: #454cad;
$dark-text: #5f6982;
.btn_upload {
  width: 150px;
  // height: 5%;
  background-color: rgb(255, 88, 102);
  color: #fff;
  cursor: pointer;
  // margin: 50px 0 0 50px;
  align-self: center;
  line-height: 42px;
  backface-visibility: hidden;
  text-align: center;
  font-family: Impact, sans-serif;
  font-weight: bold;
  font-style: normal;
}
.btn_upload:hover {
  background-color: rgba(255, 146, 157, 0.884);
}

.img_upload {
  //  max-width: 50px;
  //  height: 50px;
  height: 99%;
  width: auto;
  margin: 1px 0;
}
#file-upload-btn {
  &:hover {
    background-color: #8387b6f1;
  }
}

.photo {
  background-color: $theme;
}

.uploader {
  display: block;
  clear: both;
  margin: 0 auto;
  width: 100%;
  max-width: 600px;
  #file-drag-not_img {
    float: left;
    clear: both;
    width: 100%;
    height: 100%;
    // padding: 1.5rem 1.5rem;
    text-align: center;
    background: #fff;
    border-radius: 7px;
    border: 3px solid #eee;
    transition: all 0.2s ease;
    user-select: none;

    &:hover {
      border-color: $theme;
    }
    &.hover {
      border: 3px solid $theme;
      box-shadow: inset 0 0 0 6px #eee;

      #start {
        i.fa {
          transform: scale(0.8);
          opacity: 0.3;
        }
      }
    }
  }
  #file-drag {
    float: left;
    clear: both;
    width: 100%;
    height: 280px;
    text-align: center;
    background: #fff;
    border-radius: 7px;
    border: 3px solid #eee;
    transition: all 0.2s ease;
    user-select: none;

    &:hover {
      border-color: $theme;
    }
    &.hover {
      border: 3px solid $theme;
      box-shadow: inset 0 0 0 6px #eee;

      #start {
        i.fa {
          transform: scale(0.8);
          opacity: 0.3;
        }
      }
    }
  }

  #start {
    // float: left;
    clear: both;
    width: 60%;
    height: 70%;
    margin: 0 auto;
    // border: 1px red solid;

    &.hidden {
      display: none;
    }
    i.fa {
      font-size: 50px;
      margin-bottom: 1rem;
      transition: all 0.2s ease-in-out;
    }
  }
  input[type="file"] {
    display: none;
  }

  div {
    // margin: 5px 10px 0 10px;
    // color: $dark-text;
  }
  .photo {
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
    background: $theme;
    border-color: $theme;
    width: 100%;
    cursor: pointer;

    &:hover {
      cursor: pointer;
      background-color: #8387b6f1;
    }
  }
}

.check {
  color: crimson;
  width: 100%;
  margin: 3px;
  font-size: 1.5vh;
  text-align: center;
}

.div_file {
  color: #5f6982;
}

.body_exam {
  width: auto;
  height: 80%;
  margin: 15%;
  // border: 1px solid blueviolet;
}

.file_info {
  text-align: center;
  // border: 1px red solid;
  height: 200px;
  display: inline-block;
}
.file-upload {
  width: 50px;
  height: 300px;
}
.flexs {
  display: flex;
  justify-content: center;
}
</style>
