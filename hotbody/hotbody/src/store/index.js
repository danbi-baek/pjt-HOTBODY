import Vue from "vue";
import Vuex from "vuex";
import router from "../router";
import {getEmailFromCookie,getNicknameFromCookie,getTokenToCookie,getUserpkToCookie,getHeightToCookie,getWeightToCookie} from '@/utils/cookies'
Vue.use(Vuex);

export default new Vuex.Store({
  // data의 집합(중앙 관리할 모든 데이터===상태)
  state: {
    base_url: "http://localhost:8080",
    Userid:  getEmailFromCookie() || '',
    Usernickname: getNicknameFromCookie() || '비회원',
    Usertoken: getTokenToCookie()||'',
    Userpk: getUserpkToCookie()|| 0,
    chartlabels:[],
    chartdatas:[],
    height: getHeightToCookie() || 0,
    weight: getWeightToCookie() || 0,
    mainbmi:0,
    maindayKcal:0,
    usergoal:2,
    clickdate: new Date(),
    isToday : false,
    memoInput: '',
    bodylabels: [],
    chartWeight: [],
    chartFat: [],
    chartDate: [],
    loadingflag: false,
    bodyorfood:0,
    menuClick:0,
    type : 0,
    addFoodList : [],
    maineat: [0,0,0,0],
    Eatstate : [false,false,false,false],
    Eatimg : ['','','',''],
    EatKcal : [0,0,0,0],
    Eatfood :[
      {state:false,img:''},
      {state:false,img:''},
      {state:false,img:''},
      {state:false,img:''},
    ],
    detailNut : [0,0,0,0],
    noticeImg: '',
    gender: ''

  },

  // state 를 (가공해서)가져올 함수들. ===computed
  getters: {},

  // state를 변경하는 함수들
  // mutation에 작성되지 않은 state 변경 코드는 모두 동작하지 않음
  // 모든 mutation 함수들은 동기적으로 동작하는 코드
  // commit 함수 통해 실행함.
  // this.$store.commit('')
  mutations: {
    loginCheck: function (state, check) {
      if (check == 0) {
        router.push("../main");
      }else if(check ==1){
        router.push("../join")
      }
    },
    clearLogin(state){
      state.Userid = '';
      state.Usertoken = '';
    },
    Savenickname(state,nickname){
      // console.log('--nick save--')
      state.Usernickname = nickname
    },
    Savepk(state, pk){
      // console.log('--pk save--')
      state.Userpk = pk
      localStorage.setItem('userpk',pk)
    },
    Savetoken(state,token){
      // console.log('--token save--')
      state.Usertoken = token
    },
    getMemo(state,memo){
      state.memoInput = memo
    },

  },

  // 범용적인 함수들. mutations에 정의한 함수를 actions에서 실행 가능.
  // 비동기 로직은 actions에서 정의.
  // dispatch 를 통해 실행함.
  actions: {},
  modules: {},
});
