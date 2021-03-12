<template>
  <v-navigation-drawer
    id="app-drawer"
    v-model="inputValue"
    right
    fixed
    mobile-break-point="900"
    width="250"
    temporary
  >
    <v-layout column>
      <v-list>
        <v-list-item
          v-for="(link, i) in links"
          :key="i"
          :to="link.to"
          active-class="pink lighten-1 white--text"
          class="v-list-item ma-3"
          exact
        >
          <v-list-item-action>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-title v-text="link.text" />
        </v-list-item>
      </v-list>
    </v-layout>
      <template v-slot:append>
      <div class="py-8">
        <v-img
          :src="require('@/assets/images/logo.png')"
          class="mx-auto mb-8"
          max-width="128"
        />
      </div>
    </template>
  </v-navigation-drawer>
</template>

<script>
import { mapMutations, mapState } from "vuex";

export default {
  props: {
    opened: {
      type: Boolean,
      default: false,
    }
  },
  data: () => ({
    links: [
      {
        to: "/home",
        icon: "mdi-home",
        text: "Home"
      },
      {
        to: "/search",
        icon: "mdi-card-search",
        text: "맛집 검색"
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
