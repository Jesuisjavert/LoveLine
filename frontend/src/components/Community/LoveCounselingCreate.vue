<template>
    <v-app>
        <v-parallax
            height="200"
            src="../../assets/images/히어로1.jpg"
        >
            <v-row
                align="center"
                justify="center"
            >
                <v-col class="text-center" cols="12">
                    <h2 class="display-1 font-weight-thin mb-4">연애상담</h2>
                    <h4 class="subheading">당신의 연애를 도와드립니다</h4>
                </v-col>
            </v-row>
        </v-parallax>
        <v-container>
            <v-row>
                <v-col cols="8" class="mr-5">
                    <span>제목</span>
                    <v-text-field
                        required
                        placeholder="제목을 입력해주세요."
                        v-model="title"
                    ></v-text-field>
                    <!-- <input 
                        type="text"
                        required
                        placeholder="제목을 입력해주세요."
                        v-model="title"
                    > -->
                </v-col>
                <v-col cols="2">
                    <span>카테고리</span>
                    <v-select
                        :items="['연애', '고백', '이별']"
                        label="카테고리"
                        required
                        v-model="category"
                        ></v-select>
                </v-col>
            </v-row>
            <p>내용</p>
            <textarea 
                name="" 
                id="" 
                cols="100"
                rows="20"
                placeholder="내용을 입력해주세요."
                v-model="content"
                class="content-box"
            ></textarea>
            <v-spacer></v-spacer>
            <button @click="submit()">작성완료</button>
        </v-container>
    </v-app>
</template>

<script>
import axios from "axios"
import {mapGetters, mapState} from 'vuex'

export default {
    data() {
        return {
            id : 3,
            // title: [
            //     value => !!value || 'Required.',
            //     value => (value && value.length >= 3) || 'Min 3 characters',
            // ],
            title: "",
            content: "",
            category: "",
        }
    },
    computed: {
        ...mapGetters('accounts',['isLogined']),
        ...mapState('accounts',['authToken']),
    },
    mounted(){
        console.log(this.isLogined,this.authToken)
    },
    methods: {
        submit() {
            const data = {
                title: this.title,
                content: this.content,
                category: this.category,
            }
            const headers ={headers :{
                Authorization : `Token ${sessionStorage.getItem('auth-token')}`
            }}
            axios.post("http://j3c202.p.ssafy.io:8000/api/community/3/post/", data, headers)
            .then(res => {
                console.log(res)
                alert('게시물 작성이 완료되었습니다.')
                this.$router.push({ name: 'DetailPage', params: {
                    community_id: 3,
                    id: res.data.id,
                    } 
                })
            })
            .catch(err => {
                console.log(err.response)
            })
        },
    },
}
</script>

<style scoped>
    .content-box {
        border: solid;
    }
</style>