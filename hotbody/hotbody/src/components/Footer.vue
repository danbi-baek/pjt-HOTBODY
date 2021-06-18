<template>
  <div class="footer">
    <div class="center">
        <div class="sns">
            <i class="fab fa-instagram-square fa-2x" @click="goSNS(1)"></i>
            <i class="fab fa-facebook-square fa-2x" @click="goSNS(2)"></i>
            <i class="fas fa-envelope-square fa-2x" @click="goSNS(3)"></i>
        </div>
        <div class="teaminfo">
          <p>양진엽 진승화 백단비 김홍준 김은송</p>
          <p>Copyright © HOTBODY Rights Reserved.</p>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    methods: {
        goSNS(num){
            if(num==1)window.open('https://www.instagram.com/hellossafy/?hl=ko','_blank')
            else if(num==2) window.open('https://www.facebook.com/hellossafy','_blank')
            else if(num==3) location.href="mailto:SSAFY@ssafy.com"
        }
    }
}
</script>

<style scoped>
.footer{
    height:20vh;
    width:100%;
    background-color:rgb(59, 59, 59);
    color:white;
    text-align: center;
    padding-top:25px;
    overflow:hidden;
}
.center{
    display: inline-block;
    width:50%;
}
.teaminfo p {
    font-size:12px;
    margin-top:5px;
}
.sns i {
    color:rgb(202, 200, 200);
    margin:4px 5px;
    margin-bottom:15px;
    cursor: pointer;
}
</style>