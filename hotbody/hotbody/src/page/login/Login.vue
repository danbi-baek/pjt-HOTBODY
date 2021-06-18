<template>
  <div class="pageLogin">
    <div class="loginBox">
      <div class="loginSiteinfo">
        <div id="loginlogo">
          <!-- &#x1F525; -->
        </div>
        <p>HOT BODY</p>
      </div>

        <div class="loginBtns">
          <KakaoLogin
          api-key="013fdf0e943af162af7cb50ab3e5627a"
          image="kakao_account_login_btn_medium_wide"
          :on-success=onSuccess
          :on-failure=onFailure
          style="cursor:pointer;"
          />
          <!-- <p style="font-size:10px; color:darkgray; text-decoration:underline; cursor:pointer; margin-top:10px;">계정을 잊으셨나요?</p> -->
      </div>

      <div></div>

    </div>
    <div class="runningGirl">
      <running-girl/>
    </div>
  </div>
</template>

<script>
import KakaoLogin from 'vue-kakao-login'
import runningGirl from '@/components/RunningGirl.vue'
import {onSuccess, onFailure} from "@/utils/kakao.js";

export default {
  components : {
    KakaoLogin,
    runningGirl
  },
  methods:{
   onSuccess,
   onFailure ,
  }
}
</script>

<style scoped>
.pageLogin{
    width: 100%;
    min-height: 600px;
  }
  .loginBox{
    z-index:201;
    position:absolute;
    margin-top:80px;
    margin-left: 120px;
    width:400px;
    height:500px;
    text-align: center;
    float:left;
    /* background:	#efff97; */    
    opacity: 0.95;
    box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
background-image: linear-gradient(-20deg, #f3e7e9 0%, #e3eeff 100%);

  }
  .loginSiteinfo{
    margin-top:24px;
    font-size: 30px;
  }
  #loginlogo{ 
    margin:0 auto;
    width:52px;
    height:52px;
    border-radius: 400px;
  }
  .loginSiteinfo p {
    font-family: 'yg-jalnan';
    font-weight: bold;
    font-style: normal;
    /* font-family: Impact, sans-serif;
    font-style: normal;
    font-weight: bold; */
    margin-top:25;
    font-size:40px;
  }
  .loginBtns{
    margin-top:100px;
    width:70%;
    margin:90px auto;
  }
  

  /* RUNNING GIRL */
  .runningGirl{
    width:60%;
    float: right;
    z-index:101;
  }

  
</style>