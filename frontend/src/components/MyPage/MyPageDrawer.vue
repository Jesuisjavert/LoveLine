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
      {
        to: "/mycourse",
        icon: "mdi-google-maps",
        text: "내 코스"
      },
      // {
      //   to: "/accountupdate",
      //   icon: "mdi-account-circle",
      //   text: "회원정보수정"
      // },
      // {
      //   to: "/passwordchange",
      //   icon: "mdi-key",
      //   text: "비밀번호변경"
      // },
      // {
      //   to: "/signout",
      //   icon: "mdi-account-off",
      //   text: "회원탈퇴"
      // },
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