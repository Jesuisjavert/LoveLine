<template>
  <div class="mainpage">
    <div class="box box1">
      <div class="text-box">
        <div>
          오늘도 <br />데이트 코스<br />
          고민하세요?
        </div>
      </div>
    </div>
    <div class="box box2">
      <div class="text-box">
        <div>더 이상<br />고민은<br />Stop</div>
      </div>
      <div class="img-carousel2">
        <div id="app1">
          <agile
            class="main"
            ref="main"
            :options="options1"
            :as-nav-for="asNavFor1"
          >
            <div
              class="slide"
              v-for="(slide, index) in slides"
              :key="index"
              :class="`slide--${index}`"
            >
              <img :src="slide" />
            </div>
          </agile>
          <agile
            class="thumbnails"
            ref="thumbnails"
            :options="options2"
            :as-nav-for="asNavFor2"
          >
            <div
              class="slide slide--thumbniail"
              v-for="(slide, index) in slides"
              :key="index"
              :class="`slide--${index}`"
              @click="$refs.thumbnails.goTo(index)"
            >
              <img :src="slide" />
            </div>
            <template slot="prevButton"
              ><i class="fas fa-chevron-left"></i
            ></template>
            <template slot="nextButton"
              ><i class="fas fa-chevron-right"></i
            ></template>
          </agile>
        </div>
      </div>
    </div>
    <div class="box box3">
      <div class="text-box">
        <div>당신의 사랑도</div>
        <div>'라인'이</div>
        <div>필요합니다</div>
      </div>
      <div class="img-carousel">
        <div id="app">
          <agile
            :nav-buttons="false"
            :autoplay-speed="2000"
            :speed="1000"
            fade="fade"
            pause-on-hover="pause-on-hover"
            pause-on-dots-hover="pause-on-dots-hover"
            autoplay="autoplay"
          >
            <img class="slide" src="@/assets/images/home.png" /><img
              class="slide"
              src="@/assets/images/thumb1.png" /><img
              class="slide"
              src="@/assets/images/thumb2.png" /><img
              class="slide"
              src="@/assets/images/thumb3.png" /><img
              class="slide"
              src="@/assets/images/thumb4.png"
          /></agile>
        </div>
      </div>
    </div>
    <div class="box box4">
      <div class="text-box4">
        <div>지금 바로<br />이어보세요</div>
        <div>당신의</div>
        <span>러브라인</span
        ><img
          src="@/assets/images/logo2.png"
          height="80"
          @click="gohome"
          style="cursor: pointer"
        />
        <div @click="gohome" class="click">클릭!</div>
      </div>
      <div class="img-carousel">
        <div id="app">
          <agile
            :nav-buttons="false"
            :autoplay-speed="2000"
            :speed="1000"
            fade="fade"
            pause-on-hover="pause-on-hover"
            pause-on-dots-hover="pause-on-dots-hover"
            autoplay="autoplay"
          >
            <img class="slide" src="@/assets/images/couple1.jpg" /><img
              class="slide"
              src="@/assets/images/couple2.jpg" /><img
              class="slide"
              src="@/assets/images/couple3.jpg" /><img
              class="slide"
              src="@/assets/images/couple4.jpg" /><img
              class="slide"
              src="@/assets/images/couple5.jpg"
          /></agile>
        </div>
      </div>
    </div>
    <div class="floating-menu .hidden">
      <li class="menu-0"></li>
      <li class="m menu-1"></li>
      <li class="m menu-2"></li>
      <li class="m menu-3"></li>
    </div>

    <div class="header">
      <img @click="gohome" src="/logo.png" alt />
    </div>
  </div>
</template>

<script>
import "@/assets/css/main.css";

window.onbeforeunload = function () {
  window.scrollTo(0, 0);
};
window.onload = function () {
  var elm = ".box";
  $(elm).each(function (index) {
    // 개별적으로 Wheel 이벤트 적용
    $(this).on("mousewheel DOMMouseScroll", function (e) {
      e.preventDefault();
      var delta = 0;
      if (!event) event = window.event;
      if (event.wheelDelta) {
        delta = event.wheelDelta / 120;
        if (window.opera) delta = -delta;
      } else if (event.detail) delta = -event.detail / 3;
      var moveTop = $(window).scrollTop();
      var elmSelecter = $(elm).eq(index);
      // 마우스휠을 위에서 아래로
      if (delta < 0) {
        if ($(elmSelecter).next() != undefined) {
          try {
            moveTop = $(elmSelecter).next().offset().top;
          } catch (e) {}
        }
        // 마우스휠을 아래에서 위로
      } else {
        if ($(elmSelecter).prev() != undefined) {
          try {
            moveTop = $(elmSelecter).prev().offset().top;
          } catch (e) {}
        }
      }

      // 화면 이동 0.8초(800)
      $("html,body")
        .stop()
        .animate(
          {
            scrollTop: moveTop + "px",
          },
          {
            duration: 700,
            complete: function () {},
          }
        );
    });
  });
  var $menu = $(".floating-menu li"),
    $float = $(".floating-menu"),
    $contents = $(".box"),
    $doc = $("html, body"),
    $header = $(".header .nav-list .m");

  // menu class 추가
  $(window).scroll(function () {
    var scltop = $(window).scrollTop();
    $.each($contents, function (idx, item) {
      var $target = $contents.eq(idx),
        i = $target.index(),
        targetTop = $target.offset().top;
      if (idx == 0) {
        $float.addClass("hidden");
        console.log(idx);
      } else {
        $float.removeClass("hidden");
      }
      if (Math.floor(targetTop) == Math.floor(scltop)) {
        $menu.removeClass("on");
        $menu.eq(idx).addClass("on");
        $header.removeClass("on");
        $header.eq(idx).addClass("on");
      }
    });
  });
};
import { VueAgile } from "vue-agile";

export default {
  components: {
    agile: VueAgile,
  },
  name: "Intro",
  methods: {
    gohome() {
      this.$router.push("/home");
    },
  },
  data() {
    return {
      asNavFor1: [],
      asNavFor2: [],
      options1: {
        dots: false,
        fade: true,
        navButtons: false,
      },

      options2: {
        autoplay: true,
        centerMode: true,
        dots: false,
        navButtons: false,
        slidesToShow: 3,
        responsive: [
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 5,
            },
          },

          {
            breakpoint: 1000,
            settings: {
              navButtons: true,
            },
          },
        ],
      },

      slides: [
        "https://images.unsplash.com/photo-1453831362806-3d5577f014a4?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
        "https://images.unsplash.com/photo-1496412705862-e0088f16f791?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
        "https://images.unsplash.com/photo-1506354666786-959d6d497f1a?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
        "https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
        "https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
        "https://images.unsplash.com/photo-1472926373053-51b220987527?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
        "https://images.unsplash.com/photo-1497534547324-0ebb3f052e88?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
      ],
    };
  },
  mounted() {
    this.asNavFor1.push(this.$refs.thumbnails);
    this.asNavFor2.push(this.$refs.main);
  },
};
</script>
