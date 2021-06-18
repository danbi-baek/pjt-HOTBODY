import Vue from 'vue'
import VueRouter from 'vue-router'
import Welcome from '@/page/Welcome.vue'
import Login from '@/page/login/Login.vue'
import Join from '@/page/join/Join.vue'
import Body from '@/page/Body.vue'
import Main from "@/page/Main.vue";
import Diary from "@/page/Diary.vue";
import List from "@/page/List.vue";
import Profile from "@/page/Profile.vue";
import FoodDetail from "@/page/FoodDetail.vue";
import FoodRedetail from "@/page/FoodRedetail.vue";
import PageNotFound from "@/page/PageNotFound.vue";
import Write from '@/page/Write.vue';
import NoticeDetail from '@/page/NoticeDetail.vue';
Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'welcome',
    component: Welcome
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/join',
    name: 'join',
    component: Join
  },
  {
    path: '/body',
    name: 'body',
    component: Body
  },
  {
    path: "/main",
    name: "main",
    component: Main,
  },
  {
    path: '/diary',
    name: 'diary',
    component: Diary
  },
  {
    path: "/list",
    name: "list",
    component: List,
  },
  {
    path: "/profile",
    name: "profile",
    component: Profile,
  },
  {
    path: "/detail/:type",
    name: "detail",
    component: FoodDetail,
  },
  {
    path: "/redetail/:type",
    name: "redetail",
    component: FoodRedetail,
  },
  {
    path: '*',
    component : PageNotFound,
  },
  {
    path: '/write',
    name: 'write',
    component : Write,
  },
  {
    path: '/noticeDetail/:type',
    name: 'noticeDetail',
    component : NoticeDetail,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
