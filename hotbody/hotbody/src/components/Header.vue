<template>
  <div class="headerDiv">
    <div class="headerLogo" @click="goPage(0)">
      <p class="title">HOT BODY</p>
    </div>
    <div class="headerUser">
      <b class="name" @click="$router.push('./profile')">{{ nickname }}님</b>
      <br />
      <b
        class="name"
        v-if="nickname != '비회원'"
        id="btnlogout"
        @click="btnlogout()"
        >로그아웃</b
      >
    </div>
    <ul :class="{ headerMenu: !this.menuflag, headerFix: this.menuflag }">
      <li class="menuitem">
        <a
          :class="{
            clickmenu: this.$store.state.menuClick == 1,
            menulink: this.$store.state.menuClick != 1,
          }"
          @click="goPage(1)"
          >바디측정</a
        >
      </li>
      <li class="menuitem">
        <a
          :class="{
            clickmenu: this.$store.state.menuClick == 2,
            menulink: this.$store.state.menuClick != 2,
          }"
          @click="goPage(2)"
          >다이어리</a
        >
      </li>
      <li class="menuitem">
        <a
          :class="{
            clickmenu: this.$store.state.menuClick == 3,
            menulink: this.$store.state.menuClick != 3,
          }"
          @click="goPage(3)"
          >꿀팁</a
        >
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import { saveNicknameToCookie } from "@/utils/cookies";
import { Logout } from "@/utils/kakao.js";

export default {
  created() {
    // console.log('header CREATED '+localStorage.getItem('userpk'))
    axios
      .get(
        `http://127.0.0.1:8000/accounts/userinfo/${localStorage.getItem(
          "userpk"
        )}`
      )
      .then((res) => {
        // console.log(res.data);
        saveNicknameToCookie(res.data.user.nickname);
        this.nickname = res.data.user.nickname;
        this.$store.commit("Savenickname", this.nickname);
         this.$store.state.gender = res.data.user.gender
            // console.log( this.$store.state.gender)
      })
      .catch((res) => {
        console.log(res);
      });
  },
  data() {
    return {
      nickname: "",
      scrollPosition: null,
      menuflag: false,
    };
  },

    methods: {
      Logout,
      btnlogout() {
        alert("로그아웃....");
        this.Logout();
        this.$store.state.menuClick = 0;
        this.$router.push("/");
      },
      updateScroll() {
        this.scrollPosition = window.scrollY;
        if (this.scrollPosition >= 130) this.menuflag = true;
        else this.menuflag = false;
      },
    goPage(num) {
      window.scrollTo(0, 0);
      if (num == 0) {
        this.$store.state.menuClick = 0;
        this.$router.push("../../main").catch(() => {});
      } else if (num == 1) {
        this.$store.state.menuClick = 1;
        this.$router.push("../../body").catch(() => {});
      } else if (num == 2) {
        this.$store.state.menuClick = 2;
        this.$router.push("../../diary").catch(() => {});
      } else if (num == 3) {
        this.$store.state.menuClick = 3;
        this.$router.push("../../list").catch(() => {});
      }
    },
  },
  mounted() {
    window.addEventListener("scroll", this.updateScroll);
  },
  destroy() {
    window.removeEventListener("scroll", this.updateScroll);
  },
};
</script>
<style scoped>
@font-face {
  font-family: "NanumBarunGothic";
  font-style: normal;
  font-weight: 400;
  src: url("//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.eot");
  src: url("//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.eot?#iefix")
      format("embedded-opentype"),
    url("//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.woff")
      format("woff"),
    url("//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWeb.ttf")
      format("truetype");
}

.title {
  /* 1. 널디느낌 */
  font-family: Impact, sans-serif;
  /* font-weight: bold; */
  font-style: italic;

  /* 2. */
  /* font-weight: bold;
 font-style: italic; */

  /* font-style:  Romana, Rubik, Roboto Mono; */
}
.name {
  cursor: pointer;
  font-family: "NanumBarunGothic";
  font-style: normal;
  font-weight: 300 bold;
}
.headerDiv {
  text-align: center;
  height: 120px;
  position: relative;
  margin-bottom: 110px;
  /* background:white; */
}
.headerLogo {
  padding-top: 20px;
  font-size: 28px;
  cursor: pointer;
  background: linear-gradient(to right, crimson, pink, springgreen);
  background-size: 200% 200%;
  animation: rainbow 2s ease-in-out infinite;
  background-clip: text;
  -webkit-background-clip: text;
  color: rgba(0, 0, 0, 1);
  display: block;
  text-align: center;
  transition: color 0.2s ease-in-out;
  text-transform: uppercase;
  font-weight: 900;
}
.headerLogo:hover {
  color: rgba(0, 0, 0, 0);
}
@keyframes rainbow {
  0% {
    background-position: left;
  }
  50% {
    background-position: right;
  }
  100% {
    background-position: left;
  }
}
.headerUser {
  float: right;
  width: 20%;
  font-size: 14px;
}
#btnlogout {
  transition: all 0.8s;
  font-size: 11px;
}
#btnlogout:hover {
  font-weight: bold;
  color: red;
  cursor: pointer;
}
ul {
  margin-top: 50px;
  position: relative;
}
ul li {
  display: inline;
  font: bold 16px Dotum;
  padding: 0 40px;
  position: relative;
  cursor: pointer;
}
.headerMenu {
  /* transform: translate3d(0, 0, 0);
    transition: 0.2s all ease-out; */
  width: 100%;
  height: 60px;
  margin: 0 auto;
  margin-top: 60px;
  line-height: 60px;
  z-index: 201;
}
.headerFix {
  transform: translate3d(0, 0, 0);
  transition: 0.2s all ease-out;
  width: 100%;
  height: 70px;
  line-height: 70px;
  top: -60px;
  left: 0;
  position: fixed;
  z-index: 201;
  background: white;
}

.menulink:hover:after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: -14px;
  display: block;
  width: 38px;
  height: 2px;
  margin-left: -19px;
  background-color: rgb(255, 88, 102);
}

.clickmenu:after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: -14px;
  display: block;
  width: 38px;
  height: 2px;
  margin-left: -19px;
  background-color: rgb(255, 88, 102);
}

.headerMenu {
  opacity: 1;
  transform: matrix(1, 0, 0, 1, 0, 0);
}

.menulink,
.clickmenu {
  cursor: pointer;
  text-decoration: none;
  font-size: 16px;
  font-family: "NanumBarunGothic";
  font-style: normal;
  font-weight: 300 bold;
}
</style>
