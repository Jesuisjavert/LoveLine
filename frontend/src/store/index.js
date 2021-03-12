import Vue from "vue";
import Vuex from "vuex";
import data from "./modules/data";
import app from "./modules/app";
import accounts from './modules/accounts'
import VueAgile from 'vue-agile'

Vue.use(Vuex);
Vue.use(VueAgile);

export default new Vuex.Store({
  modules: {
    data,
    app,
    accounts,
  },
  state: {
    drawer: false,
    links: [
      'Home',
      'Course',
      'Community',
      'Login',
    ],
  mutations: {
    SET_DRAWER (state, payload) {
      state.drawer = payload
    },
  },
  getters : {
    navlinks : state => {state.links}
    }
},
});
