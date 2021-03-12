<template>
    <v-container class="pr-10">
        <h1>{{ this.community_title }}</h1>
        <v-col>
            <v-row>
                <v-col cols="auto">
                    <h2>{{ detailPost.title }}</h2>
                </v-col>
                <v-col v-if="!!this.detailPost.category" cols="auto" class="pt-4">
                    <div v-if="this.detailPost.category == '연애'" class="category-badge1 px-4 text-no-wrap rounded-pill">
                        <h3>{{ detailPost.category }}</h3>
                    </div>
                    <div v-if="this.detailPost.category == '고백'" class="category-badge2 px-4 text-no-wrap rounded-pill">
                        <h3>{{ detailPost.category }}</h3>
                    </div>
                    <div v-if="this.detailPost.category == '이별'" class="category-badge3 px-4 text-no-wrap rounded-pill">
                        <h3>{{ detailPost.category }}</h3>
                    </div>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="auto" class="mr-auto">
                    <span>******</span>
                    <span class="ml-5">{{ this.day }}</span>
                    <span class="ml-2">{{ this.time }}</span>
                </v-col>
                <v-col cols="auto">
                    <v-icon>mdi-eye-outline</v-icon>
                    {{ detailPost.views_count }}
                    <v-icon>mdi-heart-outline</v-icon>
                    {{ detailPost.like_count }}
                    <v-icon>mdi-chat-processing</v-icon>
                    {{ detailPost.comment_count }}
                </v-col>
            </v-row>
            <v-divider></v-divider>
        </v-col>
        <div v-if="!!this.detailPost.Img">
            <v-row>
                <v-col>
                    <p>ㅎㅇㅎㅇ</p>
                </v-col>
            </v-row>
        </div>
        <v-col>
            <p>{{ detailPost.content }}</p>
        </v-col>
        <v-divider></v-divider>
        <v-col align="end" no-gutters>
            <button @click="clickLike()">좋아요</button>
        </v-col>
        <v-col>
            <textarea 
                name="" 
                id=""
                class="comment" 
                cols="100" 
                rows="5"
                v-model="comment"
            ></textarea>
        </v-col>
        <button class="mb-8" @click="commentWrite">댓글작성</button>
        <v-divider></v-divider>
        <p class="mt-10">{{ detailPost.comment_count }}개 의 댓글이 있습니다.</p>
        <v-col
            v-for="commentItem in commentList"
            :key="commentItem"
        >
            <v-row>
                <v-col 
                    cols="auto" 
                    class="mr-auto"
                >
                    <span>{{ commentItem.content }}</span>
                </v-col>
                <v-col cols="auto">
                    <span>익명의 {{ commentItem.user.age }}세 {{ commentItem.user.gender }}</span>
                    <span class="ml-5">{{ commentItem.created_at.slice(0, 10) }}</span>
                    <span class="ml-2">{{ commentItem.created_at.slice(11, 19) }}</span>
                </v-col>
            </v-row>
            <v-divider></v-divider>
        </v-col>
    </v-container>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CommunityDetailPage',
    mounted() {
        this.fetchData()
        this.fetchComment()
    },
    created() {
        },
    methods: {
        fetchData() {
            axios.get(`http://j3c202.p.ssafy.io:8000/api/community/3/post/${this.$route.params.id}`)
            .then(res => {
                console.log(res)
            this.detailPost = res.data
            this.dayTime = res.data.created_at.split('T')
            this.day = this.dayTime[0]
            this.time = this.dayTime[1].slice(0, 8)
            console.log(this.day)
            console.log(this.time)
            if (this.detailPost.community_id === 1) {
                this.community_title = '코스 추천'
            } else if (this.detailPost.community_id === 2) {
                this.community_title = '코스 평가'
            } else if (this.detailPost.community_id === 3) {
                this.community_title = '연애 조언'
            } else {
                this.community_title = '만남 게시판'
            }
            })
            .catch(err => {
            console.log(err)
            })
        },
        fetchComment() {
            axios.get(`http://j3c202.p.ssafy.io:8000/api/post/${this.$route.params.id}/comment/`)
            .then(res => {
                console.log(res.data)
                this.commentList = res.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        commentWrite() {
            
            const headers ={headers :{
                Authorization : `Token ${sessionStorage.getItem('auth-token')}`
            }}
            
            axios.post(`http://j3c202.p.ssafy.io:8000/api/post/${this.$route.params.id}/comment/`, {"content": this.comment}, headers)
            .then(res => {
                console.log(res)
                this.$router.go(0)
            })
            .catch(err => {
                console.log(err)
            })
        },
        clickLike() {
            const headers ={headers :{
                Authorization : `Token ${sessionStorage.getItem('auth-token')}`
            }}
            axios.post(`http://127.0.0.1:8000/api/post/like/${this.$route.params.id}/`, null, headers)
            .then(res => {
                console.log(res.data)
                this.detailPost.like_count += 1
            })
            .catch(err => {
                console.log(res.data)
            })
        }
    },
    data() {
        return {
            detailPost: {},
            comment: '',
            dayTime: '',
            day: '',
            time: '',
            community_title: '',
            commentList: [],
        }
    }
}
</script>

<style scoped>
    .category-badge1 {
        background-color: #F48FB1 !important;
        /* border-color: blue !important; */
    }
    .category-badge2 {
        background-color: #DF6C7E !important;
    }
    .category-badge3 {
        background-color: #c0aca8ef !important;
    }
    .comment {
        border: solid;
    }
</style>