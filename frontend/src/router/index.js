import Vue from "vue";
// import Router from "vue-router";
import VueRouter from "vue-router";
import Intro from "../views/Intro.vue";
import Home from "../components/Core/Index.vue";

// 노현석
import Community from "../components/Community/Community.vue";
import CommunityHome from "../components/Community/CommunityHome.vue";
import CourseEvaluation from "../components/Community/CourseEvaluation.vue";
import CourseEvaluationCreate from "../components/Community/CourseEvaluationCreate.vue";
import CourseRecommend from "../components/Community/CourseRecommend.vue";
import CourseRecommendCreate from "../components/Community/CourseRecommendCreate.vue";
import LoveCounseling from "../components/Community/LoveCounseling.vue";
import LoveCounselingCreate from "../components/Community/LoveCounselingCreate.vue";
import Meeting from "../components/Community/Meeting.vue";
import MeetingCreate from "../components/Community/MeetingCreate.vue";
import DetailPage from "../components/Community/DetailPage.vue";
import CourseDetailPage from "../components/Community/CourseDetailPage.vue";
import Login from "../components/Login/Login.vue";
import MyPage from "../components/MyPage/MyPage.vue";
import MyCourse from "../components/MyPage/MyCourse.vue";
import AccountUpdate from "../components/MyPage/AccountUpdate.vue";
// import PasswordChange from "../components/MyPage/PasswordChange.vue";
import Signout from "../components/MyPage/Signout.vue";
import CourseMap from "../components/Course/CourseMap.vue";

import store from "../store/index.js";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Intro",
    component: Intro,
  },
  {
    path: "/home",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/logout",
    name: "Logout",
    beforeEnter: (to, from, next) => {
      store.dispatch("accounts/logout", null, { root: true });
      alert("로그아웃이 완료되었습니다.");
      next("/login");
    },
  },

  {
    path: "/community",
    name: "Community",
    component: Community,
    redirect: CommunityHome,
    children: [
      {
        path: "/communityhome",
        name: "CommunityHome",
        component: CommunityHome,
      },
      {
        path: "/courseevaluation",
        name: "CourseEvaluation",
        component: CourseEvaluation,
      },
      {
        path: "/courseevaluationcreate",
        name: "CourseEvaluationCreate",
        component: CourseEvaluationCreate,
      },
      {
        path: "/courserecommend",
        name: "CourseRecommend",
        component: CourseRecommend,
      },
      {
        // path: "/:community_id/detailpage/:id",
        path: "/courserecommendcreate",
        name: "CourseRecommendCreate",
        component: CourseRecommendCreate,
      },
      {
        path: "/lovecounseling",
        name: "LoveCounseling",
        component: LoveCounseling,
      },
      {
        path: "/lovecounselingcreate",
        name: "LoveCounselingCreate",
        component: LoveCounselingCreate,
      },
      {
        path: "/meeting",
        name: "Meeting",
        component: Meeting,
      },
      {
        path: "/meetingcreate",
        name: "MeetingCreate",
        component: MeetingCreate,
      },
      {
        path: "/:community_id/detailpage/:id",
        name: "DetailPage",
        component: DetailPage,
      },
      {
        path: "/coursedetail/:id",
        name: "CourseDetailPage",
        component: CourseDetailPage,
      },
    ],
  },
  {
    path: "/mypage",
    name: "MyPage",
    component: MyPage,
    redirect: MyCourse,
    children: [
      {
        path: "/mycourse",
        name: "MyCourse",
        component: MyCourse,
      },
      {
        path: "/accountupdate",
        name: "AccountUpdate",
        component: AccountUpdate,
      },
      // {
      //   path: "/passwordchange",
      //   name: "PasswordChange",
      //   component: PasswordChange,
      // },
      {
        path: "/signout",
        name: "Signout",
        component: Signout,
      },
    ],
  },
  {
    path: "/course",
    name: "Course",
    component: CourseMap,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

// Routes
// import paths from "./paths";

// function route(path, view, name) {
//   return {
//     name: name || view,
//     path,
//     component: resolve => import(`@/views/${view}.vue`).then(resolve)
//   };
// }

// Vue.use(Router);

// Create a new router
// const router = new Router({
//   mode: "history",
//   routes: paths
//     .map(path => route(path.path, path.view, path.name))
//     .concat([{ path: "*", redirect: "/" }]),
//   scrollBehavior(to, from, savedPosition) {
//     if (savedPosition) {
//       return savedPosition;
//     }
//     if (to.hash) {
//       return { selector: to.hash };
//     }
//     return { x: 0, y: 0 };
//   }
// });

// export default router;
