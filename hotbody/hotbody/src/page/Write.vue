<template>
  <div class="writeContainer">
    <main-header />
    <div class="write_div">
      <div class="write_header">
        <span class="input">
          제목
          <input
            v-model="title"
            type="text"
            id="title"
            class="title"
            placeholder="제목을 입력하세요"
          />
          <span></span>
        </span>

        <modal-notice></modal-notice>
      </div>
      <editor
        ref="toastuiEditor"
        initialEditType="wysiwyg"
        previewStyle="vertical"
        height="70vh"
        width="100%"
      />
      <div class="btn_write" @click="wirteNotice">등록</div>
    </div>
    <main-footer />
  </div>
</template>

<script>
import { Editor } from "@toast-ui/vue-editor";
import "@toast-ui/editor/dist/toastui-editor.css";

import axios from "axios";
import MainFooter from "@/components/Footer.vue";
import MainHeader from "@/components/Header.vue";
import ModalNotice from "@/components/page/ModalNotice.vue";

export default {
  data() {
    return {
      editorOption: {},
      title: "",
      contents: {},
    };
  },
  components: {
    MainHeader,
    MainFooter,
    Editor,
    ModalNotice,
  },
  methods: {
    wirteNotice() {
      // console.log(this.$refs.toastuiEditor.invoke("getMarkdown"));
      let data = new FormData();
      data.append("pk", localStorage.getItem("userpk"));
      data.append("content", this.$refs.toastuiEditor.invoke("getMarkdown"));
      data.append("title", this.title);
      data.append("file", this.$store.state.noticeImg);
      // console.log(localStorage.getItem("userpk"));
      // console.log("content: " + this.$refs.toastuiEditor.invoke("getMarkdown"));
      // console.log("title: " + this.title);
      // console.log(this.$store.state.noticeImg);
      // console.log("공지글 등록 ");
      // console.log(data);
      let config = {
        header: {
          "Content-Type": "multipart/form-data",
          Authorization: "JWT" + localStorage.getItem("token"),
        },
      };

      axios
        .post("http://127.0.0.1:8000/community/board/", data, config)
        .then((res) => {
          // console.log("등록 성공");
          res
          alert("칼럼 등록 성공");
          this.$router.push("/list");
        })
        .catch((err) => {
          alert("칼럼 등록 중 에러 발생" + err);
          // console.log(err);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
// .title {
//   display: inline-block;
// }
.writeContainer {
  width: 100%;
  // height: 3000px;
}
.write_header {
  padding: 10px;
  width: 100%;
  justify-content: space-between;
  display: flex;
}
.write_div {
  width: 60%;
  // border: 1px red solid;
  height: 80vh;
  text-align: center;
  margin: 10% auto;
}
.btn_write {
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
  margin: 3% 70%;
  font-family: Impact, sans-serif;
  font-weight: bold;
  font-style: normal;
}
.btn_write:hover {
  background-color: rgba(255, 146, 157, 0.884);
}
.input {
  // needs to be relative so the :focus span is positioned correctly
  position: relative;

  // bigger font size for demo purposes
  font-size: 1.5em;

  // the border gradient
  background: #eeeeee;
  // background: linear-gradient(21deg, #10abff, #1beabd);

  // the width of the input border
  padding: 4px;
  margin: 0px 10px;
  // we want inline fields by default
  display: inline-block;

  // we want rounded corners no matter the size of the field
  // border-radius: 0.8em;

  // style of the actual input field
  // *:not(span) {
  //   position: relative;
  //   display: inherit;
  //   border-radius: inherit;
  //   margin: 0;
  //   border: none;
  //   outline: none;
  //   padding: 0 0.6em;
  //   z-index: 1; // needs to be above the :focus span

  //   // summon fancy shadow styles when focussed
  //   &:focus + span {
  //     opacity: 1;
  //     transform: scale(1);
  //   }
  // }

  // // we don't animate box-shadow directly as that can't be done on the GPU, only animate opacity and transform for high performance animations.
  // span {
  //   transform: scale(0.99, 0.94); // scale it down just a little bit

  //   transition: transform 0.1s, opacity 0.1s;
  //   opacity: 0; // is hidden by default

  //   position: absolute;
  //   z-index: 0; // needs to be below the field (would block input otherwise)
  //   margin: 4px; // a bit bigger than .input padding, this prevents background color pixels shining through
  //   left: 0;
  //   top: 0;
  //   right: 0;
  //   bottom: 0;
  //   border-radius: inherit;
  //   pointer-events: none; // this allows the user to click through this element, as the shadow is rather wide it might overlap with other fields and we don't want to block those.

  //   // fancy shadow styles
  //   box-shadow: inset 0 0 0 3px #fff, 0 0 0 4px #fff, 3px -3px 10px #1beabd,
  //     -3px 3px 10px #10abff;
  // }
}

// html {
//   font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica,
//     Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
//   line-height: 1.5;
//   font-size: 1em;
// }

// body {
//   text-align: center;
//   display: flex;
//   align-items: center;
//   justify-content: center;
// }

// html,
// body {
//   height: 100%;
// }

input {
  font-family: inherit;
  line-height: inherit;
  color: #eee;
  min-width: 12em;
}

::placeholder {
  color: #cbd0d5;
}
// input {
//   color: red;
// }
// html::after {
//   // content: "";
//   // background: linear-gradient(21deg, #10abff, #1beabd);
//   height: 3px;
//   width: 100%;
//   position: absolute;
//   left: 0;
//   top: 0;
// }
</style>
