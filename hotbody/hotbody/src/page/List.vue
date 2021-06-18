<template>
  <div class="listpage">
    <main-header />
  <div class="feed">
      <div class="feed_header">
         <p class="font-weight-regular titleDoHyeon feedheader_top" >notice</p>
         <span class="feedheader_des">칼럼 : )</span>
         <span class="feedheader_follow" v-if="pk == 3"> 
             <div class="write_span" @click="moveWrite"> <i class="fas fa-pencil-alt"></i> </div> 
        </span>
      </div>
      <div class="feed_body" >
          <div class="feed_article" v-for="list in paginatedData" :key="list.title">
                <div class="article_info">
                    <div class="profilediv">
                        <img class="profileimg" :src="'http://127.0.0.1:8000'+list.articleImg"  />
                    </div>
                    <span>
                        by HOT BODY
                    </span>
                </div>
                <div class="article_contents" >
                    <div class="title">
                    <span @click="moveDetail(list.id)">
                       {{list.title}} 
                    </span>
                    </div>
                    <div class="content">
                    <div v-html="list.content.split('<br>')[0].substring(0,50)">
                    </div>
                    <p> ... </p>
                    </div>
                    <div class="ect">
                    <span class="date">
                        {{ list.created_at.substring(0, 10)}}
                    </span>

                    </div>
                </div>

          </div>
  
      </div>
              <div class="pagination" v-show="pageCount!==0">
      
            <button :disabled="pageNum === 0" @click="firstPage" class="page-btn"><i class="fas fa-caret-square-left"></i></button>
            <button :disabled="pageNum === 0" @click="prevPage" class="page-btn"><i class="far fa-caret-square-left"></i></button>
            <span class="page-count" style="padding-left:5px;padding-right:5px;font-size:1.2em;">{{ pageNum + 1 }} / {{ pageCount }}</span>
            <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn"><i class="far fa-caret-square-right"></i></button>
            <button :disabled="pageNum >= pageCount - 1" @click="lastPage" class="page-btn"><i class="fas fa-caret-square-right"></i></button>
        </div>
  </div>

  <main-footer />
  <!-- <main-footer /> -->

  </div>
</template>

<script>
import MainHeader from "@/components/Header.vue";
import MainFooter from "@/components/Footer.vue";
import axios from 'axios'

export default {
  components: {
    MainHeader,
    MainFooter,
  },
  data() {
    return {
        lists : [],
        pk: localStorage.getItem('userpk'),
        pageNum: 0,
    }
  },
  props: {
      pageSize:{
        type: Number,
        required: false,
        default:5
      }
    },
  methods: {
    moveWrite() {
      this.$router.push('/write')
    },
    moveDetail(e){
        // console.log('디테일로...')
        this.$router.push('/noticeDetail/'+ e)
    },
     nextPage () {
      this.pageNum += 1;
      },
      prevPage () {
        this.pageNum -= 1;
      },
      firstPage () {
        this.pageNum = 0;
      },
      lastPage () {
        this.pageNum = this.pageCount-1;
      },
  },
  created(){
      axios.get('http://127.0.0.1:8000/community/board/',
      )
      .then( res => {
          // console.log('리스트 가지고오기 성공')
          // console.log(res.data)
          this.lists = res.data
      })
      //   console.log('작성자')
      // console.log(localStorage.getItem('userpk'))
  },
  computed:{
      pageCount() {
        let listleng = this.lists.length,
        listSize = this.pageSize,
        page = Math.floor(listleng/listSize)

        if(listleng % listSize > 0) page +=1;

        return page;
      },
      paginatedData() {
        const start = this.pageNum*this.pageSize,
        end = start + this.pageSize;
        if(this.lists!=null)
            return this.lists.slice(start, end);
        return 0;
      },
      
    }
};
</script>

<style lang="scss" scoped>
.listpage{
  width: 100%;
  // height: 100%;
}
.feed{
    margin-top:100px;
    min-height: 1000px;
}
.feed_header{
    border-bottom:3px solid #7e7d7d;
    width: 60%;
    margin:0 auto;
    padding-bottom:30px;

}
.feedheader_top{
    margin-bottom:0px
}
.feedheader_des{
    font-size:18px;
  
}
.feedheader_follow{
    color : #9b9b9b;
    float:right;
    font-size: 24px;
    font-weight: 600;
}
.feedheader_follow span{
    font-size:14px;
}
/* body */
.feed_body{
  min-height: 60vh;
}
.feed_article{
    height:200px;
    border-bottom:1px solid lightgrey;
    margin:0 auto;
    width:60%;
    padding-top:25px;
    padding-bottom:25px;
}
/* body - profile */
.article_info{
    width:20%;
    height:100%;
    float:left;
    text-align: center;
}
.article_info span{
    margin: 0 auto;
    font-size:12px;
    color:#7e7d7d;
}
/* body - content */
.article_contents{
    width:70%;
    height:100%;
    float:right;
    line-height: 3;
    padding:14px;
    position: relative;

    
}
.article_contents .title{
    font-size:20px;
    font-weight: bold;
}
.article_contents .ect{
    font-size:13px;
    margin-top:20px;
    color:#7e7d7d;
}

.emptymsg{
    text-align: center;
    margin: 0 auto;
    height: 450px;
    padding:140px;
}
.msg1{
    font-size:18px;
}
.msg2{
    color:#7e7d7d;
    font-size:13px;
}
.btnhome{
    margin-top:10px;
}
.btnhome:hover, .btnhome:focus { animation-duration: 3s; animation-name: rainbowLink; animation-iteration-count: infinite; } 
@keyframes rainbowLink {     
 0% { color: #ff2a2a; }
 15% { color: #ff7a2a; }
 30% { color: #ffc52a; }
 45% { color: #43ff2a; }
 60% { color: #2a89ff; }
 75% { color: #202082; }
 90% { color: #6b2aff; } 
 100% { color: #e82aff; }
}
.content>p,
.content>div{
  display: inline;
}
.profileimg {

        height: 150px;
    width: 250px;
    // background-color: blueviolet;
    margin: 0 auto 0 0;
    }
.write_span:hover{
  color: black; 
  cursor: pointer;
}

.title{
    cursor:pointer;
}
.title:hover{ 
    color: gray;
}
.page-btn{
    font-size: 1.3em;
    color: pink;
    background-color: white;
    border: 0;
  }
  .pagination{
      display: flex;
      justify-content: center;
      margin-bottom: 50px;
  }
</style>
