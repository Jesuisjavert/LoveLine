<template>
    <v-container>
        <!-- <h1>커뮤니티홈</h1> -->
        <!-- <div class="d-flex justify-center"> -->
        <div>
            <v-col cols="11">
                <v-row>
                    <v-col cols="auto" class="mr-auto">
                        <h2>코스 추천</h2>
                    </v-col>
                    <v-col cols="auto" class="mt-2">
                        <a href="/courserecommend">+ 더보기</a>
                    </v-col>
                </v-row>
                <v-container fluid>
                    <v-row dense>
                        <v-col
                        v-for="data in courserecommendData"
                        :key="data.title"
                        :cols="3"
                        >
                        <v-card @click="goCourseDetail(data.id)">
                            <!-- :src="data.image[0].image" -->
                            <v-img
                            :src="data.image[0].image"
                            class="white--text align-end"
                            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                            height="200px"
                            >
                            <v-card-title v-text="data.title"></v-card-title>
                            </v-img>

                            <v-row>
                                <v-col cols="auto" class="ml-5 mr-auto">
                                    {{ data.username }}
                                </v-col>
                                <v-col cols="auto" class="mr-2">
                                    <v-icon class="mx-1">mdi-eye-outline</v-icon>
                                    {{ data.views_count }}
                                    <v-icon class="mx-1">mdi-heart-outline</v-icon>
                                    <!-- {{ data.like_count }} -->
                                    <span>0</span>
                                    <v-icon class="mx-1">mdi-chat-processing</v-icon>
                                    <!-- {{ data.comment_count }} -->
                                    <span>0</span>
                                </v-col>
                            </v-row>
                        </v-card>
                        </v-col>
                    </v-row>
                </v-container>
            </v-col>
        </div>
        <v-row>
            <v-col cols="5">
                <v-row>
                    <v-col cols="auto" class="mr-auto">
                        <h2 class="pa-2">코스 평가</h2>
                    </v-col>
                    <v-col cols="auto" class="mt-4">
                        <a href="/courseevaluation">+ 더보기</a>
                    </v-col>
                </v-row>
                <v-container>
                    <v-simple-table>
                        <template v-slot:default>
                        <!-- <thead>
                            <tr>
                            <th class="text-left">Name</th>
                            <th class="text-left">Calories</th>
                            </tr>
                        </thead> -->
                        <tbody>
                            <tr v-for="item in courseevaluationData" :key="item.name" @click="goCourseDetail(item.id)">
                            <td>
                                <v-row>
                                    <v-col cols="auto" class="mr-auto">
                                        <span>{{ item.title }}</span>
                                    </v-col>
                                <v-col cols="auto">
                                    <v-icon>mdi-eye-outline</v-icon>
                                    <span class="mx-1">{{ item.views_count }}</span>
                                    <v-icon>mdi-heart-outline</v-icon>
                                    <!-- <span class="mx-1">{{ item.like_count }}</span> -->
                                    <span class="mx-1">0</span>
                                    <v-icon>mdi-chat-processing</v-icon>
                                    <!-- <span class="mx-1">{{ item.comment_count }}</span> -->
                                    <span class="mx-1">0</span>
                                </v-col>
                                </v-row>
                            </td>
                            </tr>
                        </tbody>
                        </template>
                    </v-simple-table>
                </v-container>
            </v-col>
            <v-col offset-md="1" cols="5">
                <v-row>
                    <v-col cols="auto" class="mr-auto">
                        <h2 class="pa-2">연애 조언</h2>
                    </v-col>
                    <v-col cols="auto" class="mt-4">
                        <a href="/lovecounseling">+ 더보기</a>
                    </v-col>
                </v-row>
                <v-container>
                    <v-simple-table>
                        <template v-slot:default>
                        <!-- <thead>
                            <tr>
                            <th class="text-left">Name</th>
                            <th class="text-left">Calories</th>
                            </tr>
                        </thead> -->
                        <tbody>
                            <tr v-for="item in lovecounselingData" :key="item.name" @click="goDetail(item.community_id, item.id)">
                            <td>
                                <v-row>
                                    <v-col cols="auto" class="mr-auto">
                                        <span>{{ item.title }}</span>
                                    </v-col>
                                <v-col cols="auto">
                                    <v-icon>mdi-eye-outline</v-icon>
                                    <span class="mx-1">{{ item.views_count }}</span>
                                    <v-icon>mdi-heart-outline</v-icon>
                                    <span class="mx-1">{{ item.like_count }}</span>
                                    <v-icon>mdi-chat-processing</v-icon>
                                    <span class="mx-1">{{ item.comment_count }}</span>
                                </v-col>
                                </v-row>
                            </td>
                            </tr>
                        </tbody>
                        </template>
                    </v-simple-table>
                </v-container>
            </v-col>
        </v-row>
        <div>
            <v-col cols="11">
                <v-row>
                    <v-col cols="auto" class="mr-auto">
                        <h2 class="pa-2">만남게시판</h2>
                    </v-col>
                    <v-col cols="auto" class="mt-4">
                        <a href="/meeting">+ 더보기</a>
                    </v-col>
                </v-row>
                <v-container>
                    <v-simple-table>
                        <template v-slot:default>
                        <tbody>
                            <tr v-for="item in meetingData" :key="item.name" @click="goCourseDetail(item.id)">
                                <td>
                                    <v-row>
                                        <v-col cols="4">
                                            <span>{{ item.title }}</span>
                                            <span class="ml-10">작성자 : {{ item.username }}</span>
                                        </v-col>
                                        <v-col cols="4">
                                            <span class="ml-10 mr-5">선호도</span>
                                            <span class="mr-2"><v-icon>mdi-food-fork-drink</v-icon> : {{ item.courseTotal.taste }}</span>
                                            <span class="mr-2"><v-icon>mdi-heart-outline</v-icon> : {{ item.courseTotal.tour }}</span>
                                            <span class="mr-2"><v-icon>mdi-google-controller</v-icon> : {{ item.courseTotal.activity }}</span>
                                        </v-col>
                                        <v-col cols="4">
                                            <span class="mr-10">예정일 : {{ item.courseTotal.traveldate }}</span>
                                            <v-icon>mdi-eye-outline</v-icon>
                                            <span class="mx-1">{{ item.views_count }}</span>
                                            <v-icon>mdi-heart-outline</v-icon>
                                            <!-- <span class="mx-1">{{ item.like_count }}</span> -->
                                            <span class="mx-1">0</span>
                                            <v-icon>mdi-chat-processing</v-icon>
                                            <!-- <span class="mx-1">{{ item.comment_count }}</span> -->
                                            <span class="mx-1">0</span>
                                        </v-col>
                                    </v-row>
                                </td>
                            </tr>
                        </tbody>
                        </template>
                    </v-simple-table>
                </v-container>
            </v-col>
        </div>
    </v-container>
</template>

<script>
import axios from "axios";

export default {
    name: 'CommunityHome',
    mounted() {
        this.fetchData1()
        this.fetchData2()
        this.fetchData3()
        this.fetchData4()
    },
    methods: {
        fetchData1() {
            axios
                .get('http://j3c202.p.ssafy.io:8000/api/coursepost?category=1')
                .then(res => {
                    // console.log(res)
                    this.courserecommendData = res.data.slice(0, 4)
                    console.log(this.courserecommendData)
                })
                .catch(err => {
                    console.log(err)
                })
        },
        fetchData2() {
            axios
                .get('http://j3c202.p.ssafy.io:8000/api/coursepost?category=2')
                .then(res => {
                    // console.log(res.data)
                    this.courseevaluationData = res.data.slice(0, 5)
                    // console.log(this.courseevaluationData)
                })
                .catch(err => {
                    console.log(err)
                })
        },
        fetchData3() {
            axios
                .get('http://j3c202.p.ssafy.io:8000/api/community/3/post/')
                .then(res => {
                    // console.log(res.data)
                    this.lovecounselingData = res.data.slice(0, 10)
                })
                .catch(err => {
                    console.log(err)
                })
        },
        fetchData4() {
            axios
                .get('http://j3c202.p.ssafy.io:8000/api/coursepost?category=4')
                .then(res => {
                    // console.log(res)
                    this.meetingData = res.data.slice(0, 5)
                })
                .catch(err => {
                    console.log(err)
                })
        },
        goDetail(community_id, id) {
            console.log(id)
            this.$router.push({ name: 'DetailPage', params: {
            community_id: 3,
            // community_id: community_id,
            id: id
            } 
            })
        },
        goCourseDetail(id) {
            console.log(id)
            this.$router.push({ name: 'CourseDetailPage', params: {
                id: id
            } 
            })
        },
    },
    data: () => ({
        cards: [
            { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg'},
            { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg'},
            { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg'},
            { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg'},
        ],
        courserecommendData: {},
        courseevaluationData: {},
        lovecounselingData: {},
        meetingData: {},
        desserts: [
            {
            name: 'Frozen Yogurt',
            calories: 159,
            },
            {
            name: 'Ice cream sandwich',
            calories: 237,
            },
            {
            name: 'Eclair',
            calories: 262,
            },
            {
            name: 'Cupcake',
            calories: 305,
            },
            {
            name: 'Gingerbread',
            calories: 356,
            },
            {
            name: 'Jelly bean',
            calories: 375,
            },
            {
            name: 'Lollipop',
            calories: 392,
            },
            {
            name: 'Honeycomb',
            calories: 408,
            },
            {
            name: 'Donut',
            calories: 452,
            },
            {
            name: 'KitKat',
            calories: 518,
            },
        ],
    }),
}
</script>

<style>

</style>