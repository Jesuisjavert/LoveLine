<template>
    <v-app>
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
            <v-col cols="8">
                <span>제목</span>
                <v-text-field
                    required
                    placeholder="제목을 입력해주세요."
                    v-model="title"
                ></v-text-field>
            </v-col>
            <v-col cols="8">
                <span class="mr-2">리뷰사진 :</span>
                <input
                    ref="imageInput" 
                    type="file"
                    @change="uploadImg"
                    accept="image/*"
                />
            </v-col>
            <v-row>
                <v-col
                    v-for="reviewImg in reviewImgs"
                    :key="reviewImg"
                    cols="auto"
                >
                    <v-img 
                        v-if="reviewImg"
                        :src="reviewImg"
                        class=""
                        width="200px"
                        height="200px"
                    ></v-img>
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
import axios from 'axios'

export default {
    name: 'CourseRecommendCreate',
    data() {
        return {
            id : 3,
            title: "",
            content: "",
            reviewImgs: [],
            reviewImgsFile: [],
        }
    },
    methods: {
        uploadImg(e) {
            const file = e.target.files[0]
            console.log(file)
            this.reviewImgs.push(URL.createObjectURL(file))
            console.log(this.reviewImgs)
            this.reviewImgsFile = e.target.files
        },
        submit() {
            console.log(this.$route.params.postId)
            let formdata = new FormData()
            if (!this.reviewImgsFile) {
                formdata.append('coursetotal', this.$route.params.postId)
                formdata.append('title', this.title)
                formdata.append('content', this.content)
                formdata.append('category', 1)
            } else {
                formdata.append('coursetotal', this.$route.params.postId)
                formdata.append('title', this.title)
                formdata.append('content', this.content)
                formdata.append('category', 1)
                for(var i=0; i<this.reviewImgsFile.length ; i++){
                    formdata.append('image', this.reviewImgsFile[i])
                }
            }
            console.log(this.reviewImgsFile)
            console.log(formdata)
            const headers ={headers :{
                Authorization : `Token ${sessionStorage.getItem('auth-token')}`
            }}
            axios.post("http://j3c202.p.ssafy.io:8000/api/coursepost/", formdata, headers)
            .then(res => {
                console.log(res)
                alert('게시물 작성이 완료되었습니다.')
                this.$router.push({ name: 'CourseDetailPage', params: {
                    community_id: 1,
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