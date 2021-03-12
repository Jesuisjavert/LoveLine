<template>
    <v-app>
        <v-parallax
            height="200"
            src="../../assets/images/히어로2.jpg"
        >
            <v-row
                align="center"
                justify="center"
            >
                <v-col class="text-center" cols="12">
                    <h2 class="display-1 font-weight-thin mb-4">우리 만나볼래?</h2>
                    <h4 class="subheading">혼자가 너무 힘들어... 우리 만나볼까...?</h4>
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
                <h2 class="pt-5">만남게시판</h2>
                <v-row>
                    <v-card
                        v-for="coursepost in coursePosts"
                        :key="coursepost.title"
                        cols="3"
                        class="mx-auto my-12"
                        max-width="374"
                        @click="goCourseDetail(coursepost.id)"
                    >   
                        <v-img
                        v-if="coursepost.image"
                        height="250"
                        :src="coursepost.image[0].image"
                        ></v-img>
                        <!-- <v-img
                        v-if="coursepost.image[0].image"
                        height="250"
                        :src="coursepost.src"
                        ></v-img> -->
                        

                        <v-card-title v-text="coursepost.title"></v-card-title>
                        
                        <v-card-text>
                        <v-row
                            align="center"
                            class="mx-0"
                        >
                        </v-row>

                        <div>{{ coursepost.content.slice(0, 100) }}</div>
                        </v-card-text>

                        <v-divider class="mx-4"></v-divider>

                        <v-card-title>저 오늘 한가해요</v-card-title>

                        <v-card-text>
                        <v-chip-group
                            active-class="deep-purple accent-4 white--text"
                            column
                        >
                            <v-chip v-if="coursepost.courseTotal.activity > 7">월요일</v-chip>
                            <v-chip v-if="coursepost.courseTotal.activity > 8">화요일</v-chip>
                            <v-chip v-if="coursepost.courseTotal.taste > 8">수요일</v-chip>
                            <v-chip v-if="coursepost.courseTotal.tour > 8">목요일</v-chip>
                            <v-chip v-if="coursepost.courseTotal.tour > 7">금요일</v-chip>
                            <v-chip v-if="coursepost.created_at === coursepost.updated_at">토요일</v-chip>
                            <v-chip v-if="coursepost.created_at === coursepost.updated_at">일요일</v-chip>
                            <v-chip v-if="coursepost.courseTotal.activity > 10">언제나</v-chip>
                        </v-chip-group>
                        </v-card-text>

                        <v-card-actions>
                        <v-btn
                            color="deep-purple lighten-2"
                            text
                            @click="reserve"
                        >
                            만나러가기
                        </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-row>
            </div>
        </v-container>
    </v-app>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Meeting',
    data: () => ({
        coursePosts: [],

        loading: false,
        selection: 1,
        cards: [
            { title: '주말 한강데이트', content: '마! 나랑 라면도 먹고! 자전거도 타고! 야경도 보고! 다하자!', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg'},
            { title: '나랑 VR보러갈래?', content: '너 6층에서 판자위에 케이크 주우러 가봤어?', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg'},
            { title: 'EZ2DJ 하러갈사람?', content: '너 파이어스톰 하드 깰 줄 알아?', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg'},
        ],
    }),
    mounted() {
        this.fetchData()
    },
    methods: {
        fetchData() {
            axios.get('http://j3c202.p.ssafy.io:8000/api/coursepost?category=4')
            .then(res => {
                console.log(res.data)
                this.coursePosts = res.data
            })
            .catch(err => {
                console.log(err)
            })
        },

        // 만남게시판
        reserve () {
            this.loading = true

            setTimeout(() => (this.loading = false), 2000)
        },
        goCourseDetail(id) {
            this.$router.push({ name: 'CourseDetailPage', params: {
                id: id
            } 
            })
        },
    },
}
</script>

<style>

</style>