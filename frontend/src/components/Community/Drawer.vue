<template>
  <v-navigation-drawer
    id="app-drawer"
    v-model="inputValue"
    app
    class="pink lighten-5"
    floating
    persistent
    mobile-break-point="900"
    width="250"
    style="top: 64px"
  >
    <v-layout column>
      <v-list rounded>
        <v-list-item
          v-for="(link, i) in links"
          :key="i"
          :to="link.to"
          active-class="pink lighten-3 white--text"
          class="v-list-item ma-3"
        >
          <v-list-item-action>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-title v-text="link.text" />
        </v-list-item>
      </v-list>
    </v-layout>
  </v-navigation-drawer>
</template>

<script>
import { mapMutations, mapState } from "vuex";

export default {
  props: {
    opened: {
      type: Boolean,
      default: false
    }
  },
  data: () => ({
    links: [
    //   {
    //     to: "/",
    //     icon: "mdi-home",
    //     text: "Home"
    //   },
    //   {
    //     to: "/search",
    //     icon: "mdi-card-search",
    //     text: "맛집 검색"
    //   },
      {
        to: "/communityhome",
        icon: "mdi-home-heart",
        text: "게시판홈"
      },
      {
        to: "/courserecommend",
        icon: "mdi-hand-heart",
        text: "코스 추천"
      },
      {
        to: "/courseevaluation",
        icon: "mdi-timeline-help",
        text: "코스 평가"
      },
      {
        to: "/lovecounseling",
        icon: "mdi-chat-processing",
        text: "연애 조언"
      },
      {
        to: "/meeting",
        icon: "mdi-battery-heart-outline",
        text: "우리 만나볼래?"
      }
    ]
  }),
  computed: {
    ...mapState("app", ["drawer"]),
    inputValue: {
      get() {
        return this.drawer;
      },
      set(val) {
        this.setDrawer(val);
      }
    }
  },

  methods: {
    ...mapMutations("app", ["setDrawer"])
  }
};
</script>