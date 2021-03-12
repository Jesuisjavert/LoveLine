<template>
    <v-container>
        <h1>회원정보수정</h1>
        <v-col
        >
            <v-row>
                <v-col cols="5">
                    <p>이미지</p>
                    <v-img
                        v-if="profileImg"
                        :src="profileImg"
                    ></v-img>
                    <v-img
                        v-if="!profileImg"
                        src=""
                    ></v-img>
                    <input
                        ref="imageInput" 
                        type="file"
                        @change="onChangeImage"
                        accept="image/*"
                    />
                </v-col>
                <v-col cols="7">
                    <p>이름 : {{ userData.name }}</p>
                    <p>성별 : {{ userData.gender }}</p>
                    <p>등급 : {{ userData.grade }}</p>
                </v-col>
            </v-row>
            <v-col>
                <p>자기소개는 필요없고 그 외에 넣을게 뭐가있을까</p>
            </v-col>
        </v-col>
    </v-container>
</template>

<script>
export default {
    name: 'AccountUpdate',
    methods: {
        onChangeImage() {

        },

    },
    data() {
        return {
            userData: {
                name: '',
                gender: '',
                grade: '',
            },
            profileImg: '',
        }
    },

}
</script>