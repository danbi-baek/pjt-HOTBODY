<template>

  <div class="detail_container">
      <main-header />
      <div class="detail_div">
  
    <div class="cs-blog-detail">
    <div class="cs-main-post">
        <figure><img class="notice_img" alt="jobline-blog (8)" :src="'http://127.0.0.1:8000'+this.item.articleImg"></figure>
    </div>
    <hr class="hr_detail" style="background-color: black;">
    <div class="cs-post-title">
        <div class="post-option">
            <span class="post-date"><a href="#"><i class="cs-color icon-chat6"></i>{{item.created_at.substring(0,10)}}</a></span>
            <span class="post-comment"><a href="#"><i class="cs-color icon-chat6"></i>HOT BODY</a></span>
        </div>
    </div>
    <hr class="hr_detail">
    <div class="cs-post-option-panel">
        <h2>{{item.title}}</h2>
        <hr class="hr_detail">
        <div class="rich-editor-text">
            <div v-html="item.content">{{item.content}}</div>
            
        </div>
    </div>
</div>
      </div>  
      <main-footer />
  </div>
</template>

<script>
import axios from 'axios'
import MainHeader from "@/components/Header.vue";
import MainFooter from "@/components/Footer.vue";

export default {
    components: {
        MainHeader,
        MainFooter
    },
    data(){
        return{
            item: []
        }

    },
    created(){
        // console.log('ddd')
        // console.log(this.$route.params.type)
        axios.get(`http://127.0.0.1:8000/community/detail/${this.$route.params.type}`)
        .then( res => {
            // console.log('디테일 성공')
            // console.log(res.data)
            this.item = res.data
        })
        .catch( err => {
            // console.log('디테일 실패')
            err
        })
    }
}
</script>

<style lang="scss" scoped>
.detail_div{
    width: 50%;
    // border: 1px red solid;
    margin: 0 auto;
    height: 100%;
}
.notice_img{
    width: 100%;
    height: 400px;
}

.hr_detail{
    background-color: black !important;
}
@import '../assets/sass/notice.scss';
</style>