<template>
  <div>
    <v-row justify="center">
      <v-dialog v-model="dialog" persistent max-width="600px">
        <v-card>
          <v-card-title class="headline">나의 취향 선택</v-card-title>
          <hr />
          <br />
          <v-card-text>
            <div>
              <h2>Taste</h2>
              <br />
              <v-card-text>
                <v-slider
                  max="10"
                  v-model="eatValue"
                  step="1"
                  ticks="always"
                  tick-size="8"
                  track-color="#f07bae"
                  track-fill-color="#f07bae"
                  thumb-label="always"
                  thumb-size="25"
                  thumb-color="#e62378"
                ></v-slider>
              </v-card-text>
            </div>
            <div>
              <h2>Tour</h2>
              <br />
              <v-card-text>
                <v-slider
                  max="10"
                  v-model="seeValue"
                  step="1"
                  ticks="always"
                  tick-size="8"
                  track-color="#82e9de"
                  track-fill-color="#82e9de"
                  thumb-label="always"
                  thumb-size="25"
                  thumb-color="#4db6ac"
                ></v-slider>
              </v-card-text>
            </div>
            <div>
              <h2>Activity</h2>
              <br />
              <v-card-text>
                <v-slider
                  max="10"
                  v-model="actValue"
                  step="1"
                  ticks="always"
                  tick-size="8"
                  track-color="#ffbb93"
                  track-fill-color="#ffbb93"
                  thumb-label="always"
                  thumb-size="25"
                  thumb-color="#ff8a65"
                ></v-slider>
              </v-card-text>
            </div>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" text @click="dialog = false"
              >돌아가기</v-btn
            >
            <v-btn color="green darken-1" text @click="dialog = false"
              >선택완료</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
    <div class="course" id="capture">
      <div class="map-create">
        <div class="category-bar">
          <div class="category-list">
            <div class="category-item" @click="imgToggle(0, 'PC방')">
              <img
                data-id="0"
                src="http://d3v9ilm5vhs4go.cloudfront.net/lovelinecategory/0-1.png"
                alt=""
              />

              <p>pc방</p>
            </div>
            <div class="category-item" @click="imgToggle(1, '노래방')">
              <img
                data-id="1"
                src="http://d3v9ilm5vhs4go.cloudfront.net/lovelinecategory/1-1.png"
                alt=""
              />
              <p>노래방</p>
            </div>
            <div class="category-item" @click="imgToggle(2, '미술관')">
              <img
                data-id="2"
                src="http://d3v9ilm5vhs4go.cloudfront.net/lovelinecategory/2-1.png"
                alt=""
              />
              <p>미술관</p>
            </div>
            <div class="category-item" @click="imgToggle(3, '박물관')">
              <img
                data-id="3"
                src="http://d3v9ilm5vhs4go.cloudfront.net/lovelinecategory/3-1.png"
                alt=""
              />
              <p>박물관</p>
            </div>
            <div class="category-item" @click="imgToggle(4, '숙박')">
              <img
                data-id="4"
                src="http://d3v9ilm5vhs4go.cloudfront.net/lovelinecategory/4-1.png"
                alt=""
              />
              <p>숙박</p>
            </div>
            <div class="category-item" @click="imgToggle(5, '영화관')">
              <img
                data-id="5"
                src="http://d3v9ilm5vhs4go.cloudfront.net/lovelinecategory/5-1.png"
                alt=""
              />
              <p>영화관</p>
            </div>
            <div class="category-item" @click="imgToggle(6, '음식점')">
              <img
                data-id="6"
                src="http://d3v9ilm5vhs4go.cloudfront.net/lovelinecategory/6-1.png"
                alt=""
              />
              <p>음식점</p>
            </div>
            <div class="category-item" @click="imgToggle(7, '카페')">
              <img
                data-id="7"
                src="http://d3v9ilm5vhs4go.cloudfront.net/lovelinecategory/7-1.png"
                alt=""
              />
              <p>카페</p>
            </div>
            <div class="reset-category" @click="removeCommunitymarker('all')">
              <i class="fas fa-redo"></i>
              <p>초기화</p>
            </div>
          </div>
        </div>
        <div id="map_div"></div>
      </div>
      <div class="course-view">
        <div id="canvan">
          <div class="canvan-box">
            <p>선택한 경로</p>
            <div
              class="canvan-items"
              v-for="(pick, index) in pickDisplay"
              :key="pick.id"
            >
              <div class="canvan-item">
                <div class="canvan-info">{{ pick.name }}</div>
                <div class="canvan-control">
                  <span @click="pickchange(index, false, $event)">
                    <v-icon class="up" color="#ffffff"
                      >mdi-arrow-up-bold</v-icon
                    >
                  </span>
                  <span @click="pickchange(index, true, $event)">
                    <v-icon color="#ffffff">mdi-arrow-down-bold</v-icon>
                  </span>
                  <span @click="pickchange(index, '1', $event)">
                    <v-icon color="#ffffff">mdi-backspace-outline</v-icon>
                  </span>
                </div>
              </div>
            </div>
          </div>
          <div class="category-option">
            <div class="category-select">
              <select name="option" v-model="selectMethod">
                <option :value="null" selected disabled hidden>
                  선택하세요 ▼
                </option>
                <option :value="false">&nbsp;🚶‍♂️&nbsp; 도보 이동</option>
                <option :value="true">🚓 차량 이동</option>
              </select>
              <button class="button-request" @click="resetpicklist()">
                리스트 제거
              </button>
              <button class="button-request" @click="removePath()">
                경로 초기화
              </button>
              <button class="button-request" @click="getRp(selectMethod, 0)">
                <p>경로 요청</p>
                <div class="request-img"></div>
              </button>
            </div>
          </div>
          <div class="result-box">
            <p>거리 : {{ totaldistance }}km 시간 : {{ totaltime }}분</p>
          </div>
          <div class="course-calendar">
            <datetime format="YYYY-MM-DD" width="150px" v-model="date"
              >날짜</datetime
            >
            <button class="button-submit" @click="makeCourse()">
              코스 완성
              <div id="wrapper">
                <div id="pulsingheart"></div>
              </div>
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="course-recommend">
      <div class="recommend-box">
        <div class="recommend-option">
          <span @click="recommandCourse('up')"
            ><img src="@/assets/images/recommend.png" alt="" />내 취향에 맞는
            코스 추천</span
          >
          <span @click="recommandCourse('down')"
            ><img src="@/assets/images/recommend2.png" alt="" />Loveline 추천
            코스</span
          >
          <select v-model="selectPasscnt">
            <option value="" selected disabled>경로 갯수 ▼</option>
            <option :value="2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2개</option>
            <option :value="3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3개</option>
            <option :value="4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4개</option>
            <option :value="5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5개</option>
          </select>
          <select v-model="selectCoursecnt">
            <option value="" selected disabled>코스 갯수 ▼</option>
            <option :value="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1개</option>
            <option :value="2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2개</option>
            <option :value="3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3개</option>
          </select>
        </div>
        <div class="course-recommend-list">
          <div
            class="list-course"
            v-for="recommand in recommandArray"
            :key="recommand.id"
          >
            <p
              v-for="coursedetail in recommand.coursedetail"
              :key="coursedetail.id"
            >
              {{ coursedetail.location.name }}
            </p>
            <button @click="movepickdata(recommand)">적용하기</button>
          </div>
        </div>
      </div>
      <div class="slide-box">
        <div>
          <p>나의 취향</p>
        </div>
        <div class="slide-item">
          <span>Taste</span>
          <v-card-text>
            <v-slider
              max="10"
              v-model="eatValue"
              step="1"
              ticks="always"
              tick-size="8"
              track-color="#f07bae"
              track-fill-color="#f07bae"
              thumb-label="always"
              thumb-size="20"
              thumb-color="#e62378"
            ></v-slider>
          </v-card-text>
        </div>
        <div class="slide-item">
          <span>Tour</span>
          <v-card-text>
            <v-slider
              max="10"
              v-model="seeValue"
              step="1"
              ticks="always"
              tick-size="8"
              track-color="#82e9de"
              track-fill-color="#82e9de"
              thumb-label="always"
              thumb-size="20"
              thumb-color="#4db6ac"
            ></v-slider>
          </v-card-text>
        </div>

        <div class="slide-item">
          <span>Activity</span>
          <v-card-text>
            <v-slider
              max="10"
              v-model="actValue"
              step="1"
              ticks="always"
              tick-size="8"
              track-color="#ffbb93"
              track-fill-color="#ffbb93"
              thumb-label="always"
              thumb-size="20"
              thumb-color="#ff8a65"
            ></v-slider>
          </v-card-text>
        </div>
      </div>
    </div>
  </div>
</template>
<!-- <button @click="LoadMarker()">카테고리 실행 버튼</button>
    <button @click="getRp(true, 0)">차량경로요청 실행</button>
    <button @click="getRp(false, 1)">도보 요청 실행</button>
    <button @click="resetpicklist()">경로 리스트 전체 제거</button>
    <button @click="getRp(selectMethod, 1)">경</button> -->

<script>
import axios from "axios";
import "@/assets/css/course.css";
import _ from "lodash";
import datetime from "vuejs-datetimepicker";
import { mapState } from "vuex";
export default {
  name: "CourseMap",
  components: { datetime },
  data() {
    return {
      date: "",
      dialog: true,
      eatValue: 0,
      seeValue: 0,
      actValue: 0,
      map: "",
      categorydata: [[], [], [], [], [], [], [], [], []],
      markers: [[], [], [], [], [], [], [], [], []],
      infoW: "",
      pickcheck: [],
      picklist: [],
      drawInfoArr: [[], [], [], [], []],
      resultMarkerArr: [[], [], [], [], []],
      resultdrawArr: [[], [], [], [], []],
      lineColorArr: ["#7117F0", "#00B170", "#B10041", "#4C74B9", "#F7941D"],
      totaltime: 0,
      totaldistance: 0,
      imgIndex: [1, 1, 1, 1, 1, 1, 1, 1, 1],
      selectMethod: null,
      selectPasscnt: "",
      selectCoursecnt: "",
      recommandArray: [],
    };
  },
  computed: {
    pickDisplay() {
      return this.picklist;
    },
    ...mapState("accounts", ["authToken"]),
  },
  methods: {
    cap() {
      var imageDiv = document.querySelector("#canvan");

      html2canvas(imageDiv, {
        allowTaint: true,
        logging: true,
        useCORS: true,
      }).then(function (canvas) {
        var imgBase64 = canvas.toDataURL();
        // console.log("imgBase64:", imgBase64);
        var imgURL = "data:image/" + imgBase64;
        var triggerDownload = $("<a>")
          .attr("href", imgURL)
          .attr("download", "layout_" + new Date().getTime() + ".jpeg")
          .appendTo("body");
        triggerDownload[0].click();
        triggerDownload.remove();
      });
    },
    initDate() {
      var date = new Date();
      var today = date.toLocaleDateString();
      var joindate = today
        .split(".")
        .map((item, index) => {
          if (item.length > 0) {
            if (index > 0) {
              var temp = item.trim();
              console.log(item.length, index, "---");
              if (temp.length == 1) {
                return "0" + temp;
              } else {
                return temp;
              }
            }

            return item.trim();
          }
        })
        .filter((item) => {
          return item;
        });
      this.date = joindate.join("-");
    },
    movepickdata(recommand) {
      this.removePath();
      this.resetpicklist();
      this.removeCommunitymarker(8);
      if (this.categorydata[8].length > 0) {
        this.categorydata[8] = [];
      }
      recommand.coursedetail.forEach((item) => {
        var copyValue = _.cloneDeep(item.location);
        this.picklist.push(copyValue);
        this.categorydata[8].push(copyValue);
        this.pickcheck.push(item.location.id);
      });
      var lat = this.picklist[0].latitude;
      var lon = this.picklist[0].longitude;
      this.LoadMarker("음식점", 8);
      this.map.setCenter(new window.Tmapv2.LatLng(lat, lon));
    },
    recommandCourse(flag) {
      console.log("들어옴");
      if (this.selectCoursecnt !== "") {
        let params = {
          flag: flag,
          cnt: this.selectCoursecnt,
          ta: this.eatValue,
          ac: this.actValue,
          to: this.seeValue,
          order: this.selectPasscnt,
        };
        axios
          .get("http://j3c202.p.ssafy.io:8000/api/recommandcourse/", { params })
          .then((res) => {
            console.log("됬네요");
            console.log(res.data);
            this.recommandArray = [];
            res.data.forEach((item) => {
              this.recommandArray.push(item);
            });
          });
      }
    },
    invertColor(hex) {
      if (hex.indexOf("#") === 0) {
        hex = hex.slice(1);
      }
      // convert 3-digit hex to 6-digits.
      if (hex.length === 3) {
        hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2];
      }
      if (hex.length !== 6) {
        throw new Error("Invalid HEX color.");
      }
      // invert color components
      var r = (255 - parseInt(hex.slice(0, 2), 16)).toString(16),
        g = (255 - parseInt(hex.slice(2, 4), 16)).toString(16),
        b = (255 - parseInt(hex.slice(4, 6), 16)).toString(16);
      // pad each with zeros and return
      return "#" + this.padZero(r) + this.padZero(g) + this.padZero(b);
    },

    padZero(str, len) {
      len = len || 2;
      var zeros = new Array(len).join("0");
      return (zeros + str).slice(-len);
    },
    imgToggle(idx, category) {
      var targetImg = event.currentTarget.children[0];
      if (this.imgIndex[idx] % 2 == 1) {
        // ON
        targetImg.src = `http://d3v9ilm5vhs4go.cloudfront.net/lovelinecategory/${idx}-2.png`;
        this.getCategory(category, idx);
      } else {
        // OFF
        this.removeCommunitymarker(idx);
        targetImg.src = `http://d3v9ilm5vhs4go.cloudfront.net/lovelinecategory/${idx}-1.png`;
      }
      this.imgIndex[idx]++; // cnt 변수 1씩 증가 시키기
    },
    // 코스를 완성하는 list
    async makeCourse() {
      var data = {
        tour: this.seeValue,
        activity: this.actValue,
        taste: this.eatValue,
        courselist: this.picklist,
        traveldate: this.date,
        distance: this.totaldistance,
      };
      await axios
        .post("http://j3c202.p.ssafy.io:8000/api/course/", data, {
          headers: {
            Authorization: `Token ${this.authToken}`,
          },
        })
        .then((res) => {
          alert("코스생성이 완성되었습니다.");
          this.cap();
        });
    },
    async getCategory(category, idx) {
      var params = {
        category: category,
        latitude: this.map.getCenter()._lat,
        longitude: this.map.getCenter()._lng,
        zoomlevel: this.map.getZoom(),
      };
      await axios
        .get("http://j3c202.p.ssafy.io:8000/api/location/", { params })
        .then((res) => {
          this.categorydata[idx] = _.cloneDeep(res.data);
        });

      this.LoadMarker(category, idx);
    },
    resetpicklist() {
      var temp = this.picklist.length;
      for (var i = 0; i < temp; i++) {
        this.picklist.pop();
        this.pickcheck.pop();
      }
    },
    removeCommunitymarker(idx) {
      // Marker들을 초기화 해주는 Methods
      if (idx === "all") {
        var imgli = document.querySelectorAll("[data-id]");
        for (var ind in imgli) {
          if (ind != "length") {
            imgli[
              ind
            ].src = `http://d3v9ilm5vhs4go.cloudfront.net/lovelinecategory/${ind}-1.png`;
            this.imgIndex[ind] = 1;
          }
        }
        for (var j = 0; j < this.markers.length; j++) {
          if (this.markers[j].length > 0) {
            for (var k = 0; k < this.markers[j].length; k++) {
              this.markers[j][k].setMap(null);
            }
            this.markers[j] = [];
          }
        }
      } else {
        for (var i = 0; i < this.markers[idx].length; i++) {
          this.markers[idx][i].setMap(null);
        }
        this.markers[idx] = [];
        console.log(this.markers[idx], "마지막");
      }
    },
    removePath() {
      // 경로와 관련된 정보들을 초기화시켜주는곳

      for (var i = 0; i < this.resultMarkerArr.length; i++) {
        if (this.resultMarkerArr[i].length > 0) {
          for (var k = 0; k < this.resultMarkerArr[i].length; k++) {
            this.resultMarkerArr[i][k].setMap(null);
          }
        }
      }

      this.resultMarkerArr = [[], [], [], [], []];
      for (var j = 0; j < this.resultdrawArr.length; j++) {
        if (this.resultdrawArr[j].length > 0) {
          for (var t = 0; t < this.resultdrawArr[j].length; t++) {
            this.resultdrawArr[j][t].setMap(null);
          }
        }
      }
      this.resultdrawArr = [[], [], [], [], []];
      this.drawInfoArr = [[], [], [], [], []];
      this.totalTime = 0;
      this.totalDistance = 0;
    },
    changeColor(e) {
      e.style.backgroundColor = "transparent";
    },
    async pickchange(index, flag, event) {
      // picklist에 있는거의 순서를 바꿔주고, 삭제하는 메소드
      if (flag === true) {
        if (index !== this.picklist.length - 1) {
          var temp = this.picklist.splice(index, 1);
          this.picklist.splice(index + 1, 0, temp[0]);
          event.target.style.backgroundColor = "rgb(255, 255, 128)";
          await setTimeout(() => {
            this.changeColor(event.target);
          }, 500);
        }
      } else if (flag === false) {
        if (index !== 0) {
          var temp2 = this.picklist.splice(index, 1);
          this.picklist.splice(index - 1, 0, temp2[0]);
          event.target.style.backgroundColor = "rgb(255, 255, 128)";
          await setTimeout(() => {
            this.changeColor(event.target);
          }, 500);
        }
      } else {
        var removeObj = this.picklist.splice(index, 1);
        this.pickcheck.splice(this.pickcheck.indexOf(removeObj[0].id), 1);
      }
    },
    LoadMarker(category, idx) {
      this.removeCommunitymarker(idx);
      // Marker를 띄워주는거
      console.log("여기?");
      var position = [];
      for (var k of this.categorydata[idx]) {
        var title = k.name;
        var lonlat = new window.Tmapv2.LatLng(k.latitude, k.longitude);
        position.push({ title: title, lonlat: lonlat });
      }
      var cnt = 0;
      var size = new window.Tmapv2.Size(30, 30);
      for (var t of position) {
        var mlonlat = t.lonlat;
        var mtitle = t.title;
        var cate = k.category;
        var storeArray = [
          "중식",
          "술집",
          "한식",
          "분식",
          "세계음식",
          "양식",
          "뷔페",
          "일식",
        ];
        if (storeArray.includes(cate)) {
          cate = "음식점";
        }
        var marker = new window.Tmapv2.Marker({
          position: mlonlat,
          title: mtitle,
          icon: `http://d3v9ilm5vhs4go.cloudfront.net/loveline/${cate}.png`,
          iconSize: size,
        });
        marker.setMap(this.map);
        this.addMarkerClickEvent(marker, cnt, idx);
        cnt++;
        this.markers[idx].push(marker);
      }
    },
    addMarkerClickEvent(e, cnt, idx) {
      // makers에 이벤트를추가해서 info를 보여주는 곳
      e.addListener("click", () => {
        if (this.infoW != "") {
          this.infoW.setVisible(false);
        }
        var cate = this.categorydata[idx][cnt].category;
        var storeArray = [
          "중식",
          "술집",
          "한식",
          "분식",
          "세계음식",
          "양식",
          "뷔페",
          "일식",
        ];
        if (storeArray.includes(cate)) {
          cate = "음식점";
        }
        var url =
          "https://www.urbanbrush.net/web/wp-content/uploads/edd/2018/12/urbanbrush-20181213142535248709.png";
        var content =
          "<div class='m-pop' style='position: static; top: 180px; left : 320px; display: flex; flex-direction: column; font-size: 14px; border-radius: 10px; width : 320px; height:120px; background-color: #FCE4EC; align-items: center;'>" +
          "<div style='display: flex; align-items: center; height: 90px;'>" +
          `<div class='img-box' style='width: 70px; height: 70px; margin-right: 12px; border-radius: 10px; background: url(http://d3v9ilm5vhs4go.cloudfront.net/infomarker/${cate}.png) no-repeat center'></div>` +
          "<div class='info-box' style='width: 200px; margin-bottom: 7px;'>" +
          "<p style='margin-bottom: 4px;'>" +
          `<span class='tit' style='font-size: 16px; font-weight: bold;'>${this.categorydata[idx][cnt].name}</span>` +
          "</p>" +
          "<p style='margin:0px;'>" +
          `<span class='new-addr'>${this.categorydata[idx][cnt].address.slice(
            0,
            this.categorydata[idx][cnt].address.length - 8
          )}</span>` +
          "</p>" +
          "<p style='margin:0px;'>" +
          `<span class='old-addr' style='color: #707070;'>${this.categorydata[
            idx
          ][cnt].address.slice(
            this.categorydata[idx][cnt].address.length - 8
          )}</span>` +
          "</p>" +
          "</div>" +
          "</div>" +
          "<div style=''>" +
          `<button style="padding:2px; border:2px solid #f48fb1; border-radius:4px; margin-right:8px;" onclick="popupmethod(${cnt},${idx})">경로추가</button>` +
          '<button style="padding:2px; border:2px solid #f48fb1; border-radius:4px; margin-right:8px;" onclick="infoClose()">닫기</button>' +
          "</div>" +
          "</div>";

        this.infoW = new window.Tmapv2.InfoWindow({
          position: new window.Tmapv2.LatLng(
            this.categorydata[idx][cnt].latitude,
            this.categorydata[idx][cnt].longitude
          ),
          content: content,
          type: 2,
          map: this.map,
        });
      });
    },
    initTmap() {
      // 처음 맵을 띄어주는 methods
      var lat = 35.1874726;
      var lng = 126.900115;
      if (!!this.$route.query.lat && !!this.$route.query.lng) {
        lat = parseFloat(this.$route.query.lat);
        lng = parseFloat(this.$route.query.lng);
      }
      this.map = new window.Tmapv2.Map("map_div", {
        center: new window.Tmapv2.LatLng(lat, lng),
        width: "70vw",
        height: "55vh",
        zoom: 15,
        zIndexMarker: 9,
        zIndexInfoWindow: 10000,
      });
    },
    infoClose() {
      // 자세한정보 닫아주는 method
      if (this.infoW != "") {
        this.infoW.setVisible(false);
      }
    },
    popupmethod(cnt, idx) {
      // 경로에 넣는 메소드
      if (this.pickcheck.length < 6) {
        if (this.pickcheck.includes(this.categorydata[idx][cnt].id)) {
          alert("이미 경로에 있습니다.");
        } else {
          this.pickcheck.push(this.categorydata[idx][cnt].id);
          var copyValue = _.cloneDeep(this.categorydata[idx][cnt]);
          this.picklist.push(copyValue);
        }
      } else {
        alert("경로는 6개이상 만들수 없습니다.");
      }
    },
    async getRp(way, cnt) {
      // 경로요청하는 함수
      console.log(way, "--");
      var startNode = [];
      var endNode = [];
      var passString = [];
      if (this.picklist.length < 2) {
        alert("경로는 2개이상이어야합니다.");
      } else {
        if (this.picklist.length == 2) {
          startNode = [
            String(this.picklist[0].longitude),
            String(this.picklist[0].latitude),
          ];
          endNode = [
            String(this.picklist[1].longitude),
            String(this.picklist[1].latitude),
          ];
        } else {
          var picklen = this.picklist.length;
          startNode = [
            String(this.picklist[0].longitude),
            String(this.picklist[0].latitude),
          ];
          endNode = [
            String(this.picklist[picklen - 1].longitude),
            String(this.picklist[picklen - 1].latitude),
          ];
          var passArray = this.picklist.slice(1, picklen - 1);
          passString = passArray.reduce((arr, cur, ind) => {
            arr.push(String(cur.longitude) + "," + String(cur.latitude));
            return arr;
          }, []);
          var passList = _.cloneDeep(passString);
          passString = passString.join("_");
        }
        var appKey = "l7xxda1e2d4a335b47c8b7c5b933b288677d";

        var data = {};
        var urlpath = "";
        if (way === true) {
          urlpath =
            "https://apis.openapi.sk.com/tmap/routes?version=1&format=json&callback=result";
          if (passString.length == 0) {
            data = {
              startX: startNode[0],
              startY: startNode[1],
              endX: endNode[0],
              endY: endNode[1],
              reqCoordType: "WGS84GEO",
              resCoordType: "EPSG3857",
              searchOption: "0",
              trafficInfo: "N",
            };
          } else {
            data = {
              startX: startNode[0],
              startY: startNode[1],
              endX: endNode[0],
              endY: endNode[1],
              passList: passString,
              reqCoordType: "WGS84GEO",
              resCoordType: "EPSG3857",
              searchOption: "0",
              trafficInfo: "N",
            };
          }
        } else {
          urlpath =
            "https://apis.openapi.sk.com/tmap/routes/pedestrian?version=1&format=json&callback=result";
          if (passString.length == 0) {
            data = {
              startX: startNode[0],
              startY: startNode[1],
              endX: endNode[0],
              endY: endNode[1],
              reqCoordType: "WGS84GEO",
              resCoordType: "EPSG3857",
              startName: "출발지",
              endName: "도착지",
            };
          } else {
            data = {
              startX: startNode[0],
              startY: startNode[1],
              endX: endNode[0],
              endY: endNode[1],
              reqCoordType: "WGS84GEO",
              resCoordType: "EPSG3857",
              passList: passString,
              startName: "출발지",
              endName: "도착지",
            };
          }
        }
        var headers = {
          headers: {
            appKey: appKey,
          },
        };
        this.infoClose();
        await axios
          .post(urlpath, data, headers)

          .then((res) => {
            console.log("여기냐?");
            this.removePath();
            this.removeCommunitymarker("all");
            var receivedata = res.data.features;
            this.totaldistance = receivedata[0].properties.totalDistance / 1000;
            this.totaltime = (receivedata[0].properties.totalTime / 60).toFixed(
              0
            );
            var lineYn = false;
            var linecolor = this.lineColorArr[cnt];
            if (way == false) {
              linecolor = this.invertColor(linecolor);
            }
            for (var ind in receivedata) {
              var geometry = receivedata[ind].geometry;
              var properties = receivedata[ind].properties;
              if (geometry.type == "LineString") {
                for (var j in geometry.coordinates) {
                  var latlng = new window.Tmapv2.Point(
                    geometry.coordinates[j][0],
                    geometry.coordinates[j][1]
                  );
                  var convertPoint = new window.Tmapv2.Projection.convertEPSG3857ToWGS84GEO(
                    latlng
                  );
                  var convertChange = new window.Tmapv2.LatLng(
                    convertPoint._lat,
                    convertPoint._lng
                  );
                  if (lineYn) {
                    this.drawInfoArr[cnt].push(convertChange);
                  }
                }
                if (this.drawInfoArr[cnt].length > 0) {
                  this.drawLine(this.drawInfoArr[cnt], way, cnt, linecolor);
                }
              } else {
                if (
                  properties.pointType == "S" ||
                  properties.pointType == "E" ||
                  properties.pointType == "N" ||
                  properties.pointType == "SP" ||
                  properties.pointType == "PP" ||
                  properties.pointType == "GP" ||
                  properties.pointType == "EP"
                ) {
                  lineYn = true;
                } else {
                  lineYn = false;
                }
                var markerImg = "";
                var pType = "";
                if (
                  properties.pointType == "S" ||
                  properties.pointType == "SP"
                ) {
                  markerImg =
                    "http://d3v9ilm5vhs4go.cloudfront.net/loveline/start.png";
                  pType = "S";
                } else if (
                  properties.pointType == "E" ||
                  properties.pointType == "EP"
                ) {
                  //도착지 마커
                  markerImg =
                    "http://d3v9ilm5vhs4go.cloudfront.net/loveline/end.png";
                  pType = "E";
                } else {
                  //각 포인트 마커
                  markerImg = "http://topopen.tmap.co.kr/imgs/point.png";
                  pType = "P";
                }
                var latlon = new window.Tmapv2.Point(
                  geometry.coordinates[0],
                  geometry.coordinates[1]
                );
                var convertPoint = new window.Tmapv2.Projection.convertEPSG3857ToWGS84GEO(
                  latlon
                );
                var routeInfoObj = {
                  markerImage: markerImg,
                  lng: convertPoint._lng,
                  lat: convertPoint._lat,
                  pointType: pType,
                };
                this.addMarkers(routeInfoObj, cnt);
              }
            }
          })
          .catch((err) => {
            console.log(err.response);
          });
        if (passString.length > 0) {
          for (var passTemp of passList) {
            var passlonlat = passTemp.split(",");
            var lonlat = new window.Tmapv2.LatLng(
              parseFloat(passlonlat[1]),
              parseFloat(passlonlat[0])
            );
            var size = new window.Tmapv2.Size(30, 30);
            var marker = new window.Tmapv2.Marker({
              position: lonlat,
              title: "경유지",
              icon: "http://d3v9ilm5vhs4go.cloudfront.net/loveline/pass.png",
              iconSize: size,
            });
            marker.setMap(this.map);
            this.resultMarkerArr[cnt].push(marker);
          }
        }
      }
    },
    addMarkers(infoObj, cnt) {
      var size = new window.Tmapv2.Size(24, 24);
      if (infoObj.pointType == "P") {
        size = new window.Tmapv2.Size(8, 8);
      }
      var marker_p = new window.Tmapv2.Marker({
        position: new window.Tmapv2.LatLng(infoObj.lat, infoObj.lng),
        icon: infoObj.markerImage,
        iconSize: size,
        map: this.map,
      });

      this.resultMarkerArr[cnt].push(marker_p);
    },
    drawLine(arrPoint, way, cnt, linecolor) {
      var polyline_;
      polyline_ = new window.Tmapv2.Polyline({
        path: arrPoint,
        strokeColor: linecolor,
        strokeWeight: 7,
        map: this.map,
      });
      this.resultdrawArr[cnt].push(polyline_);
    },
  },

  mounted() {
    this.initTmap();
    this.initDate();
    window.infoClose = this.infoClose;
    window.popupmethod = this.popupmethod;
  },
};
</script>
