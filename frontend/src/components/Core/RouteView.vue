<template>
  <v-main>
    <div id="app-view" style="height: 100%">
      <v-fade-transition mode="out-in">
        <router-view />
        <div class="home">
          <div class="explain">
            <div class="explain-left">
              <div class="explain-box item1">
                <img
                  class="explain-img1"
                  src="@/assets/images/course1.png"
                  alt=""
                />
                <img
                  class="explain-marker1 marker"
                  src="@/assets/images/marker1.png"
                  alt=""
                />
                <div class="explain-info info1">
                  카테고리 영역에서, 테마별 데이트 명소들을 불러올 수 있어요.
                </div>
              </div>
              <div class="explain-box item2">
                <img
                  class="explain-img2"
                  src="@/assets/images/course2.png"
                  alt=""
                />
                <img
                  class="explain-marker2 marker"
                  src="@/assets/images/marker2.png"
                  alt=""
                />
                <div class="explain-info info2">
                  내가 선택한 'Loveline'을 보여드립니다.
                </div>
              </div>
              <div class="explain-box item4">
                <img
                  class="explain-img4"
                  src="@/assets/images/course4.png"
                  alt=""
                />
                <img
                  class="explain-marker4 marker"
                  src="@/assets/images/marker4.png"
                  alt=""
                />
                <div class="explain-info info4">
                  당신의 취향에 맞춰 코스를 추천해 드립니다. Taste (맛집),
                  Tour(명소), Activity(활동) 점수를 조절해가며, 다양한
                  'Loveline'을 추천 받아보세요!
                </div>
              </div>
            </div>
            <div class="explain-right">
              <div class="explain-box item3">
                <img
                  class="explain-img3"
                  src="@/assets/images/course3.png"
                  alt=""
                />
                <img
                  class="explain-marker3 marker"
                  src="@/assets/images/marker3.png"
                  alt=""
                />
                <div class="explain-info info3">
                  'Loveline'의 순서를 관리하고,
                  <br />
                  도보/차량 이동에 따라 최적의 경로를 검색하고, 내 코스로
                  등록해보세요!
                </div>
              </div>
              <div class="explain-box item5">
                <img
                  class="explain-img5"
                  src="@/assets/images/course5.png"
                  alt=""
                />
                <img
                  class="explain-marker5 marker"
                  src="@/assets/images/marker5.png"
                  alt=""
                />
                <div class="explain-info info5">
                  'Loveline' 에서 추천해주는 코스는 어떠세요?
                  <br />
                  빅데이터 알고리즘 기반으로 추천되는 'Loveline 추천코스' 기능도
                  이용해 보세요!
                </div>
              </div>
            </div>
          </div>
          <div class="district">
            <div class="district-area">
              <span
                @click="courseMake([35.190617, 126.823471])"
                class="district-name name-1"
                >광산구</span
              >
              <div class="district-info">
                <p>떡갈비, 1913 송정역시장, 애호박찌개</p>
                <br />
                <p>송산공원, 풍영정, 빙월당, 호가정</p>
                <br />
                <p>맛과 멋이 함께하는</p>
                <br />
                <h1>광산구</h1>
              </div>
              <img
                class="district-img1"
                src="@/assets/images/light.png"
                alt=""
              />
            </div>
            <div class="district-area">
              <div class="district-info">
                <p>무등산수박, 돌솥밥, 추어탕, 옻닭</p>
                <br />
                <p>광주시립미술관, 풍암정, 담양소쇄원</p>
                <br />
                <p>자연과 도시가 어우러진</p>
                <br />
                <h1>북구</h1>
              </div>
              <span
                @click="courseMake([35.176495, 126.90713])"
                class="district-name name-2"
                >북구</span
              >
              <img
                class="district-img2"
                src="@/assets/images/north.png"
                alt=""
              />
            </div>
            <div class="district-area">
              <div class="district-info">
                <p>오리탕, 홍어삼합, 한정식</p>
                <br />
                <p>풍암호수, 운천저수지, 5.18 기념공원</p>
                <br />
                <p>젊음의 열기를 느낄 수 있는</p>
                <br />
                <h1>서구</h1>
              </div>
              <span
                @click="courseMake([35.159889, 126.851453])"
                class="district-name name-3"
                >서구</span
              >
              <img
                class="district-img3"
                src="@/assets/images/west.png"
                alt=""
              />
            </div>
            <div class="district-area">
              <div class="district-info">
                <p>황태찜, 굴비한정식, 게장삼겹살</p>
                <br />
                <p>광주공원, 광주향교, 펭귄마을, 사직공원</p>
                <br />
                <p>광주의 근현대사를 느낄 수 있는</p>
                <br />
                <h1>남구</h1>
              </div>
              <span
                @click="courseMake([35.117065, 126.897264])"
                class="district-name name-4"
                >남구</span
              >
              <img
                class="district-img4"
                src="@/assets/images/south.png"
                alt=""
              />
            </div>
            <div class="district-area">
              <div class="district-info">
                <p>오리주물럭, 흑염소요리, 모리소바</p>
                <br />
                <p>국립아시아문화전당 , 5·18 사적, 주상절리대</p>
                <br />
                <p>과거와 현재가 살아숨쉬는</p>
                <br />
                <h1>동구</h1>
              </div>
              <span
                @click="courseMake([35.146681, 126.92154])"
                class="district-name name-5"
                >동구</span
              >
              <img
                class="district-img5"
                src="@/assets/images/east.png"
                alt=""
              />
            </div>
            <div class="start-button">
              <div class="centerer">
                <div class="wrap">
                  <p class="btn-0" @click="courseMake()">
                    시작하기<i class="far fa-heart"></i>
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div class="board">
            <div>게시판 글</div>
            <img src="@/assets/images/community.png" alt="" />
          </div>
          <div class="footer">
            <div class="footer-row1">
              <div class="footer-column">
                <div>
                  <h3>About Us</h3>
                  <p>LoveLine</p>
                </div>
                <div>
                  <h3>Contact Us</h3>
                  <p><i class="fas fa-phone-volume"></i> 010-1234-5678</p>
                  <p><i class="far fa-envelope"></i>ssafy@samsung.com</p>
                </div>
              </div>
              <div class="footer-column">
                <div>
                  <h3>Information</h3>
                  <p>Blog</p>
                  <p>Events</p>
                  <p>More Search</p>
                </div>
              </div>
              <div class="footer-column">
                <div>
                  <h3>Helpful Links</h3>
                  <p>Services</p>
                  <p>Supports</p>
                  <p>Privacy Policy</p>
                </div>
              </div>
            </div>
            <div class="footer-row2">
              <i class="fab fa-facebook-square"></i>
              <i class="fab fa-instagram"></i>
              <i class="fab fa-twitter"></i>
            </div>
          </div>
        </div>
      </v-fade-transition>
    </div>
  </v-main>
</template>

<script>
import "@/assets/css/home.css";

export default {
  name: "RouteView",
  data() {
    return {};
  },
  methods: {
    courseMake(res) {
      var latlng = res;
      console.log(latlng);
      this.$router.push({
        path: "course",
        query: {
          lat: latlng[0],
          lng: latlng[1],
        },
      });
    },
  },
};
</script>
<style scoped>
.start-button *:before,
.start-button *:after {
  z-index: -1;
  box-sizing: border-box;
  -webkit-transition: 0.5s ease-in-out;
  transition: 0.5s ease-in-out;
}

.start-button {
  -webkit-transition: none;
  transition: none;
}

.start-button p,
i {
  -webkit-transition: 0.5s ease-in;
  transition: 0.5s ease-in;
  text-decoration: none;
  line-height: 2vw;
  color: #f48fb1;
  padding-left: 0.7vw;
}

.start-button i {
  -webkit-transition: 0.5s;
  transition: 0s;
}

.centerer {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  padding: 0.5rem 1rem;
}

@media (min-width: 600px) {
  .wrap {
    width: 6vw;
    float: left;
  }
}
[class^="btn-"] {
  position: relative;
  display: block;
  overflow: hidden;
  width: 100%;
  height: 2vw;
  max-width: 250px;
  text-transform: uppercase;
  border: 1px solid currentColor;
}

.btn-0:before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: #e03d74;
  -webkit-transform: translateX(-100%);
  transform: translateX(-100%);
}
.btn-0:hover {
  color: #e9e6d6;
}

.btn-0:hover i {
  color: #e9e6d6;
}
.btn-0:hover:before {
  -webkit-transform: translateX(0);
  transform: translateX(0);
}
</style>