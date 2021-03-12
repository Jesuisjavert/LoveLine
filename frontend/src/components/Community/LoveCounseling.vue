<template>
    <div>
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
            <v-row>
              <v-col cols="auto" class="mr-auto">
                  <!-- <v-select
                    :items="['전체', '연애이야기', '고백이야기', '이별이야기']"
                    label="게시글보기"
                    required
                  ></v-select> -->
                  <select v-model='category' name="" id="">
                    <option :value="true">전체</option>
                    <option value="연애">연애이야기</option>
                    <option value="고백">고백이야기</option>
                    <option value="이별">이별이야기</option>
                  </select>
              </v-col>
              <v-col cols="auto">
                  <router-link :to="{ name: 'LoveCounselingCreate' }"><button>게시물작성</button></router-link>
              </v-col>
            </v-row>
            <div>
                <v-simple-table>
                  <template v-slot:default>
                    <tbody>
                      <tr v-for="item in communityselect" :key="item.name" @click="goDetail(item.id)">
                        <td>
                          <v-row>
                            <v-col cols="2" class="d-flex flex-column align-center">
                              <h3 class="mt-6 pink--text">{{ item.category }}</h3>
                            </v-col>
                            <v-col cols="9">
                              <p>{{ item.title }}</p>
                              <v-row>
                                <v-col cols="8" class="mr-5">
                                  <!-- {{ item.작성자 }} -->
                                  <span>******</span>
                                  <span class="ml-5">{{ item.created_at.slice(0, 10) }}</span>
                                  <span class="ml-2">{{ item.created_at.slice(11, 19) }}</span>
                                </v-col>
                                <v-col cols="3">
                                  <v-icon>mdi-eye-outline</v-icon>
                                  {{ item.views_count }}
                                  <v-icon>mdi-heart-outline</v-icon>
                                  {{ item.like_count }}
                                  <v-icon>mdi-chat-processing</v-icon>
                                  {{ item.comment_count }}
                                </v-col>
                              </v-row>
                            </v-col>
                          </v-row>
                        </td>
                      </tr>
                    </tbody>
                  </template>
                </v-simple-table>

                <div class="text-center">
                  <v-pagination
                    v-model="page"
                    :length="4"
                    circle
                  ></v-pagination>
                </div>
            </div>
        </v-container>
    </div>
</template>

<script>
import axios from 'axios'
import {mapGetters, mapState} from 'vuex'

export default {
    name: 'LoveCounseling',
    mounted() {
      this.fetchData()
    },
    methods: {
      goDetail(id) {
        console.log(id)
        this.$router.push({ name: 'DetailPage', params: {
          community_id: 3,
          id: id
          } 
        })
      },
      fetchData() {
        axios.get('http://j3c202.p.ssafy.io:8000/api/community/3/post/')
        .then(res => {
          console.log(res.data)
          this.communitys = res.data
        })
      }
    },
    data () {
      return {
        page: 1,
        pageCount: 0,
        itemsPerPage: 10,
        communitys: [],
        category : true,
      }
    },
    computed:{
      ...mapGetters('accounts',['isLogined']),
      ...mapState('accounts',['authToken']),
      communityselect(){
        if(this.category === true){
          return this.communitys
        } else{
          return this.communitys.filter((item)=>{
            return item.category == this.category
          })
        }
      }
    }
}
</script>

<style>

</style>