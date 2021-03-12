import axios from 'axios'
import router from "@/router";

const state = {
    username : null,
    authToken : sessionStorage.getItem('auth-token'),
    API_URL : 'http://j3c202.p.ssafy.io:8000/api/',
    links: [
        'Home',
        'Course',
        'Community',
        'Login',
        'MyPage',
        'Logout'
      ]

}
const mutations = {
    SET_TOKEN(state,token){
        state.authToken = token
        sessionStorage.setItem("auth-token",token)
    },
    SET_USERNAME(state,username){
        state.username = username
        sessionStorage.setItem('username',username)
    },
    RESET_TOKEN(){
        sessionStorage.removeItem("auth-token")
    },
    RESET_USERNAME(){
        sessionStorage.removeItem("username")
    }


}
const actions ={
    async login({state,commit},payload){
        console.log('안녕하세요')
        console.log(payload)
        const response = await axios.post(state.API_URL+'rest-auth/login/',payload)
        .catch((err)=>{alert('아이디와 비밀번호를 확인해주세요.')})
        commit('SET_TOKEN',response.data.key)
        const headers = {
            Authorization : `Token ${state.authToken}`
        }
        const userdata = await axios.get(state.API_URL+'account/',{headers : headers})
        // console.log(userdata)
        commit('SET_USERNAME',userdata.data.nickname)
        alert('로그인이 완료되었습니다.')
        router.push({ name: 'Home' })
    },

    logout({state, commit},){
        const headers = {
            headers : {
                'Authorization' : `Token ${state.authToken}`
            }
        }
        axios.post(state.API_URL+'rest-auth/logout/', null, headers)
        .then((res)=>{
            console.log(res)
            commit('RESET_TOKEN')
            commit('RESET_USERNAME')  
        })
        .catch((err)=>
        {console.log(err.response)})
    }

}
const getters = {
    isLogined : (state) => !!state.authToken,
    navlinks : (state,getters) => {
        if (getters.isLogined){
            var temp = [ 'Home', 'Course','Community','MyPage','Logout']
            return temp
        } else{
            var temp = [ 'Home', 'Course','Community','Login']
            return temp
        }
    }

}

export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions,
  };