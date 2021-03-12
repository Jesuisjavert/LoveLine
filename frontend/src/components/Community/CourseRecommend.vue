<template>
    <div>
        <v-parallax
            height="200"
            src="../../assets/images/벚꽃수정.jpg"
        >
            <v-row
                align="center"
                justify="center"
            >
                <v-col class="text-center" cols="12">
                    <h2 class="display-1 font-weight-thin mb-4">경로 추천</h2>
                    <h4 class="subheading">당신의 데이트에 날개를 달아주고 싶어요</h4>
                </v-col>
            </v-row>
        </v-parallax>
        <v-container>
            <!-- <div>
                <v-row justify="center">
                    <v-col
                        v-for="value in ['-lg']"
                        :key="value"
                        cols="12"
                    >
                        <div
                        :class="`rounded${value}`"
                        class="pa-6 text-center grey lighten-2"
                        v-text="`쓸데없는말 하지 말고 비방글 쓰지마라`"
                        ></div>
                    </v-col>
                </v-row>
            </div> -->
            <div>
                <v-container>
                    <v-row>
                        <v-col cols="auto" class="mr-auto">
                            <h2>추천 코스</h2>
                        </v-col>
                        <v-col cols="auto" class="mt-2">
                            <router-link :to="{ name: 'CourseRecommendCreate' }"><button>글쓰기</button></router-link>
                        </v-col>
                    </v-row>
                    <v-container fluid>
                        <h3>이 달의 베스트3</h3>
                        <v-row dense>
                            <v-col
                            v-for="card in cards"
                            :key="card.title"
                            :cols="4"
                            @click="goCourseDetail(card.id)"
                            >
                            <v-card
                                v-show="card.flex === 3 | card.flex === 4 | card.flex === 5"
                            >
                                <v-img
                                :src="card.src"
                                class="white--text align-end"
                                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                                height="200px"
                                >
                                <v-card-title v-text="card.title"></v-card-title>
                                </v-img>

                                <v-row>
                                    <v-col cols="auto" class="ml-5 mr-auto">
                                        <!-- {{ coursepost.username }} -->
                                        <span>작성자</span>
                                    </v-col>
                                    <v-col cols="auto" class="mr-5">
                                        <v-icon class="mx-1">mdi-eye-outline</v-icon>
                                        <!-- {{ coursepost.views_count }} -->
                                        <span>0</span>
                                        <v-icon class="mx-1">mdi-heart-outline</v-icon>
                                        <!-- {{ coursepost.like_count }} -->
                                        <span>0</span>
                                        <v-icon class="mx-1">mdi-chat-processing</v-icon>
                                        <!-- {{ coursepost.comment_count }} -->
                                        <span>0</span>
                                    </v-col>
                                </v-row>
                            </v-card>
                            </v-col>
                        </v-row>
                        <v-layout>
                            <v-row class="pt-5">
                                <v-col cols="2" class="mr-auto">
                                    <h3>전체 게시글</h3>
                                </v-col>
                                <v-col cols="auto">
                                    <span>최신순</span> 
                                    <span> | </span>
                                    <span>인기순</span>
                                </v-col>
                            </v-row>
                        </v-layout>
                        <v-row dense>
                            <v-col
                            v-for="coursepost in coursePosts"
                            :key="coursepost.title"
                            :cols="3"
                            @click="goCourseDetail(coursepost.id)"
                            >
                            <v-card>
                                <v-img
                                :src="coursepost.image[0].image"
                                class="white--text align-end"
                                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                                height="200px"
                                >
                                <v-card-title v-text="coursepost.title"></v-card-title>
                                </v-img>

                                <v-row>
                                    <v-col cols="auto" class="ml-5 mr-auto">
                                        {{ coursepost.username }}
                                    </v-col>
                                    <v-col cols="auto" class="mr-5">
                                        <v-icon class="mx-1">mdi-eye-outline</v-icon>
                                        {{ coursepost.views_count }}
                                        <v-icon class="mx-1">mdi-heart-outline</v-icon>
                                        <!-- {{ coursepost.like_count }} -->
                                        <span>0</span>
                                        <v-icon class="mx-1">mdi-chat-processing</v-icon>
                                        <!-- {{ coursepost.comment_count }} -->
                                        <span>0</span>
                                    </v-col>
                                </v-row>

                                <!-- <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn icon>
                                    <v-icon>mdi-eye-outline</v-icon>
                                </v-btn>

                                <v-btn icon>
                                    <v-icon>mdi-heart-outline</v-icon>
                                </v-btn>

                                <v-btn icon>
                                    <v-icon>mdi-chat-processing</v-icon>
                                </v-btn>
                                </v-card-actions> -->
                            </v-card>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-container> 
            </div>
        </v-container>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CourseRecommend',
    mounted() {
        this.fetchData()
    },
    methods: {
        fetchData() {
            axios.get('http://j3c202.p.ssafy.io:8000/api/coursepost?category=1')
            .then(res => {
                console.log(res.data)
                this.coursePosts = res.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        goCourseDetail(id) {
            this.$router.push({ name: 'CourseDetailPage', params: {
                id: id
            } 
            })
        },
    },
    data: () => ({
        coursePosts: [],
        cards: [
            { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 4 },
            { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 4 },
            { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 4 },
        ],
        totalCards: [
            { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 3 },
            { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 3 },
            { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3 },
            { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 3 },
            { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 3 },
            { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3 },
            { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 3 },
            { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 3 },
            { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3 },
        ]
    }),
}
</script>

<style>

</style>