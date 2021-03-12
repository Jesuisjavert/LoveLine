<template>
    <v-app>
        <v-parallax
            height="200"
            src="../../assets/images/히어로3.jpg"
        >
            <v-row
                align="center"
                justify="center"
            >
                <v-col class="text-center" cols="12">
                    <h2 class="display-1 font-weight-thin mb-4">코스 평가</h2>
                    <h4 class="subheading">정신분열증 올거같은데 도와주실분?</h4>
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
                <span class="mr-2">코스사진 :</span>
                <input
                    ref="imageInput" 
                    type="file"
                    @change="uploadImg"
                    multiple accept="image/*"
                />
            </v-col>
            <v-row>
                <v-col
                    v-for="courseImg in courseImgs"
                    :key="courseImg"
                    cols="auto"
                >
                    <v-img 
                        v-if="courseImg"
                        :src="courseImg"
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
    name: 'CourseEvaluationCreate',
    data() {
        return {
            id : 2,
            title: "",
            content: "",
            courseImgs: [],
            courseImgsFile: [],
        }
    },
    methods: {
        uploadImg(e) {
            const file = e.target.files[0]
            this.courseImgs.push(URL.createObjectURL(file))
            this.courseImgsFile = e.target.files
        },
        submit() {
            console.log(this.$route.params.postId)
            let formdata = new FormData()
            if (!this.courseImgsFile) {
                formdata.append('coursetotal', this.$route.params.postId)
                formdata.append('title', this.title)
                formdata.append('content', this.content)
                formdata.append('category', 2)
            } else {
                formdata.append('coursetotal', this.$route.params.postId)
                formdata.append('title', this.title)
                formdata.append('content', this.content)
                formdata.append('category', 2)
                for(var i=0; i<this.courseImgsFile.length ; i++){
                    formdata.append('image', this.courseImgsFile[i])
                }
            }
            const headers ={headers :{
                Authorization : `Token ${sessionStorage.getItem('auth-token')}`
            }}
            axios.post("http://j3c202.p.ssafy.io:8000/api/coursepost/", formdata, headers)
            .then(res => {
                console.log(res)
                alert('게시물 작성이 완료되었습니다.')
                this.$router.push({ name: 'CourseDetailPage', params: {
                    community_id: 2,
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