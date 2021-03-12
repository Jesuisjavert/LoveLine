<template>
    <v-container>
        <h1>내 코스</h1>
        <div>
            <h2 class="py-5">내가 갔다온 코스</h2>
            <v-simple-table>
                <template v-slot:default>
                <tbody>
                    <tr v-for="(item, index) in pastCourses" :key="item.name" @click="goDetail(index, item.ispastday, item)">
                    <td>
                        <v-row>
                        <v-col cols="2" class="d-flex flex-column align-center mr-auto mt-3">
                            <h3 class="mt-3 primary--text" v-if="item.visited">방문</h3>
                            <h3 class="mt-3 red--text" v-if="!item.visited">미방문</h3>
                        </v-col>
                        <v-col cols="9">
                            <v-row>
                                <v-col cols="8" class="mr-5">
                                    <v-row>
                                        <v-col cols="6">
                                            <h3>출발점 : {{ item.coursedetail[0].location.name }}</h3>
                                        </v-col>
                                        <v-col cols="6">
                                            <h3>도착점 : {{ item.coursedetail[item.coursedetail.length - 1].location.name }}</h3>
                                        </v-col>
                                    </v-row>
                                </v-col>
                                <v-col cols="3">
                                    <h3 class="mt-3">{{ item.traveldate }}</h3>
                                </v-col>
                            </v-row>
                        </v-col>
                        </v-row>
                    </td>
                    </tr>
                </tbody>
                </template>
            </v-simple-table>
        </div>
        <div class="pt-5">
            <h2 class="py-5">예정된 코스</h2>
            <v-simple-table>
                <template v-slot:default>
                <tbody>
                    <tr v-for="(item, index) in futureCourses" :key="item.name" @click="goDetail(index, item.ispastday, item)">
                    <td>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="7" class="mr-5">
                                    <v-row>
                                        <v-col cols="6">
                                            <h3>출발점 : {{ item.coursedetail[0].location.name }}</h3>
                                        </v-col>
                                        <v-col cols="6">
                                            <h3>도착점 : {{ item.coursedetail[item.coursedetail.length - 1].location.name }}</h3>
                                        </v-col>
                                    </v-row>
                                </v-col>
                                <v-col cols="4">
                                    <v-row>
                                        <v-col cols="auto" class="mr-auto">
                                            <v-icon>mdi-food-fork-drink</v-icon>
                                            <span class="mx-1">{{ item.taste }}</span>
                                            <v-icon>mdi-heart-outline</v-icon>
                                            <span class="mx-1">{{ item.tour }}</span>
                                            <v-icon>mdi-google-controller</v-icon>
                                            <span class="mx-1">{{ item.activity }}</span>
                                        </v-col>
                                        <v-col cols="auto">
                                            <h3>{{ item.traveldate }}</h3>
                                        </v-col>
                                    </v-row>
                                </v-col>
                            </v-row>
                        </v-col>
                    </td>
                    </tr>
                </tbody>
                </template>
            </v-simple-table>
        </div>
        <!-- modal -->
        <v-row justify="center">
            <v-dialog
            v-model="dialog"
            persistent
            max-width="1000"
            >
            <!-- 지난코스 -->
            <v-card v-if="choice">
                <v-card-title class="headline">
                    <v-row>
                        <v-col cols="auto" class="mr-auto">
                            <v-row>
                                <v-col cols="auto">
                                    <h2>당신의 코스</h2>
                                </v-col>
                                <v-col cols="auto" v-if="!pastCourses[selectNum].ispastday">
                                    <span v-if="pastCourses[selectNum].visited" class="mr-auto visit-badge1 px-2 text-no-wrap rounded-pill white--text">방문</span>
                                    <span v-if="!pastCourses[selectNum].visited" class="visit-badge2 px-2 text-no-wrap rounded-pill white--text">미방문</span>
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="auto">
                            <v-btn
                                color="green darken-1"
                                text
                                @click="goVisited(pastCourses[selectNum].id, selectNum)"
                                v-if="!pastCourses[selectNum].visited"
                            >
                                방문
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-card-title>
                <v-card-text>
                    <v-row>
                        <v-col cols="auto" class="mr-auto">
                            <span class="mr-2">Taste : {{ this.pastCourses[this.selectNum].taste }}</span>
                            <span class="mr-2">Tour : {{ this.pastCourses[this.selectNum].tour }}</span>
                            <span class="mr-2">Activity : {{ this.pastCourses[this.selectNum].activity }}</span>
                        </v-col>
                        <v-col cols="auto">
                            <span>{{ this.pastCourses[this.selectNum].traveldate }}</span>
                        </v-col>
                    </v-row>
                    <span>장소 :</span>
                    <v-col v-for="item in this.pastCourses[this.selectNum].coursedetail" :key="item.name">
                        <p>{{ item.location.name }} ( {{ item.location.categorygroup }} ) / 평점 ( {{ item.location.rank }} 점 ) : {{ item.location.address }}</p>
                    </v-col>
                </v-card-text>
                <v-card-actions>
                <!-- <v-spacer></v-spacer> -->
                <v-row>
                    <v-col cols="auto" class="mr-auto">
                        <v-btn
                            color="green darken-1"
                            text
                            @click="goRecommend(pastCourses[selectNum].id)"
                            v-if="pastCourses[this.selectNum].visited == true"
                        >
                            코스 추천    
                        </v-btn>
                        <v-btn
                            color="green darken-1"
                            text
                            @click="goEvaluation(pastCourses[selectNum].id)"
                            v-if="!pastCourses[this.selectNum].visited"
                        >
                            코스 평가
                        </v-btn>
                        <v-btn
                            color="green darken-1"
                            text
                            @click="goMeeting(pastCourses[selectNum].id)"
                            v-if="!pastCourses[this.selectNum].visited"
                        >
                            만남 게시판
                        </v-btn>
                    </v-col>
                    <v-col cols="auto">
                        <v-btn
                            color="green darken-1"
                            text
                            @click="dialog = false"
                        >
                            확인
                        </v-btn>
                    </v-col>
                </v-row>
                </v-card-actions>
            </v-card>
            <!-- 예정코스 -->
            <v-card v-else>
                <v-card-title class="headline">
                    <v-row>
                        <v-col cols="auto" class="mr-auto">
                            <v-row>
                                <v-col cols="auto">
                                    <h2>당신의 코스</h2>
                                </v-col>
                                <v-col cols="auto" v-if="!futureCourses[selectNum].ispastday">
                                    <span v-if="futureCourses[selectNum].visited" class="mr-auto visit-badge1 px-2 text-no-wrap rounded-pill white--text">방문</span>
                                    <span v-if="!futureCourses[selectNum].visited" class="visit-badge2 px-2 text-no-wrap rounded-pill white--text">미방문</span>
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="auto">
                            <v-btn
                                color="green darken-1"
                                text
                                @click="goVisited(futureCourses[selectNum].id)"
                                v-if="!futureCourses[selectNum].visited"
                            >
                                방문
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-card-title>
                <v-card-text>
                    <v-row>
                        <v-col cols="auto" class="mr-auto">
                            <span class="mr-2">Taste : {{ this.futureCourses[this.selectNum].taste }}</span>
                            <span class="mr-2">Tour : {{ this.futureCourses[this.selectNum].tour }}</span>
                            <span class="mr-2">Activity : {{ this.futureCourses[this.selectNum].activity }}</span>
                        </v-col>
                        <v-col cols="auto">
                            <span>{{ this.futureCourses[this.selectNum].traveldate }}</span>
                        </v-col>
                    </v-row>
                    <span>장소 :</span>
                    <v-col v-for="item in this.futureCourses[this.selectNum].coursedetail" :key="item.name">
                        <p>{{ item.location.name }} ( {{ item.location.categorygroup }} ) / 평점 ( {{ item.location.rank }} 점 ) : {{ item.location.address }}</p>
                    </v-col>
                </v-card-text>
                <v-card-actions>
                <!-- <v-spacer></v-spacer> -->
                <v-row>
                    <v-col cols="auto" class="mr-auto">
                        <v-btn
                            color="green darken-1"
                            text
                            @click="goRecommend(futureCourses[selectNum].id)"
                            v-if="futureCourses[this.selectNum].visited == true"
                        >
                            코스 추천    
                        </v-btn>
                        <v-btn
                            color="green darken-1"
                            text
                            @click="goEvaluation(futureCourses[selectNum].id)"
                            v-if="!futureCourses[this.selectNum].visited"
                        >
                            코스 평가
                        </v-btn>
                        <v-btn
                            color="green darken-1"
                            text
                            @click="goMeeting(futureCourses[selectNum].id)"
                            v-if="!futureCourses[this.selectNum].visited"
                        >
                            만남 게시판
                        </v-btn>
                    </v-col>
                    <v-col cols="auto">
                        <v-btn
                            color="green darken-1"
                            text
                            @click="dialog = false"
                        >
                            확인
                        </v-btn>
                    </v-col>
                </v-row>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>    
    </v-container>
</template>

<script>
import axios from 'axios'

export default {    
    name: 'MyCourse',
    mounted() {
        // this.fetchpastCourses()
        this.fetchCourses()
    },
    methods: {
        fetchCourses() {
            const headers ={headers :{
                Authorization : `Token ${sessionStorage.getItem('auth-token')}`
            }}
            axios.get('http://j3c202.p.ssafy.io:8000/api/course/', headers)
            .then(res => {
                console.log(res.data)
                this.totalCourses = res.data
                // console.log(this.totalCourses)
                this.pastCourses = res.data.filter((item) => {
                    return !item.ispastday
                })
                this.futureCourses = res.data.filter((item) => {
                    return item.ispastday
                })
                console.log(this.pastCourses)
                console.log(this.futureCourses)
            })
        },
        goDetail(idx, ispastday, item) {
            console.log(idx, ispastday, item)
            this.dialog = true
            this.selectNum = idx
            if (ispastday === false) {
                this.choice = 1
            } else if (ispastday === true) {
                this.choice = 0
            }
            console.log(this.choice)
        },
        goVisited(id, selectNum) {
            const headers ={headers :{
            Authorization : `Token ${sessionStorage.getItem('auth-token')}`
            }}
            axios.put(`http://j3c202.p.ssafy.io:8000/api/course/${id}/`, null, headers)
            .then(res => {
                console.log(res)
                this.pastCourses[this.selectNum].visited = true
            })
            .catch(err => {
                console.log(err)
            })
        },
        goRecommend(postId) {
            this.$router.push({ name: 'CourseRecommendCreate', params: { postId: postId } })
        },
        goEvaluation(postId) {
            console.log(postId)
            this.$router.push({ name: 'CourseEvaluationCreate', params: { postId: postId } })
        },
        goMeeting(postId) {
            this.$router.push({ name: 'MeetingCreate', params: { postId: postId } })
        },
    },
    data:() => ({
        dialog: false,
        choice: 0,
        selectNum: 0,
        totalCourses: [],
        pastCourses: [],
        futureCourses: [],
    })
}
</script>

<style scoped>
    .visit-badge1 {
        /* border: solid;
        border-color: blue;
        border-radius: 30%; */
        background-color: rgb(0, 60, 255);
    }
    .visit-badge2 {
        /* border: solid;
        border-color: red;
        border-radius: 25%; */
        background-color: red;
    }
</style>