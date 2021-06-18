<template>
  <div class="welcome_div">
    <!-- Slider -->
    <div id="slider">
      <div class="slides">
        <div class="slider">
          <div class="content">
            <div class="content-txt">
              <h1>HOTBODY</h1>
              <h2>다이어트 시작이 어려운 당신,</h2>
              <h2>HOTBODY와 함께 변화하는 몸과 마음을 느껴보세요.</h2>
            </div>
          </div>
          <div class="image">
            <img src="../assets/imgs/welcome1.jpg" />
          </div>
        </div>
        <div class="slider">
          <div class="content">
            <div class="content-txt">
              <h1>HOTBODY</h1>
              <h2>건강한 식단 관리</h2>
              <h2>사진 한장으로 간단하게 식단을 등록하고 성분을 체크하세요!</h2>
            </div>
          </div>
          <div class="image">
            <img src="../assets/imgs/welcome2.png" />
          </div>
        </div>
        <div class="slider">
          <div class="content">
            <div class="content-txt">
              <h1>HOTBODY</h1>
              <h2>사진을 통해 간단하게 인바디를 확인해보세요!</h2>
              <h2>HOTBODY가 당신의 기록을 그래프로 나타내 줄겁니다.</h2>
            </div>
          </div>
          <div class="image">
            <img src="../assets/imgs/welcome1.jpg" />
          </div>
        </div>
        <div class="slider">
          <div class="content">
            <div class="content-txt">
              <h1>HOTBODY</h1>
              <h2>사진을 통해 간단하게 인바디를 확인해보세요!</h2>
              <h2>HOTBODY가 당신의 기록을 그래프로 나타내 줄겁니다.</h2>
            </div>
          </div>
          <div class="image">
            <img src="../assets/imgs/welcome1.jpg" />
          </div>
        </div>
      </div>

      <div class="switch">
        <div class="legend"></div>
        <div class="btnLogin" @click="moveLogin">로그인</div>
      </div>
    </div>
    <main-footer />
  </div>
</template>

<script>
import MainFooter from "@/components/Footer.vue";

export default {
  components: {
    MainFooter,
  },
  data() {
    return {};
  },
  methods: {
    moveLogin() {
      this.$router.push("/login");
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/sass/slider.scss";
</style>