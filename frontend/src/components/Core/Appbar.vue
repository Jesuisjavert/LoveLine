<template>
  <v-app-bar id="core-app-bar" app elevate-on-scroll height="96">
    <v-container>
      <v-row>
        <div class="d-flex align-center">
          <v-spacer></v-spacer>
          <v-img
            :src="require('@/assets/images/logo.png')"
            contain
            class="shrink mr-2 img-move"
            height="90"
            width="200"
            to="home"
            @click="gohome"
            style="cursor: pointer"
          />
        </div>

        <v-spacer />

        <v-toolbar-items v-if="$vuetify.breakpoint.smAndUp" class="shrink">
          <v-btn
            v-for="(link, i) in navlinks"
            :key="i"
            :to="{
              name: link,
            }"
            active-class="pink--text"
            class="subtitle-1 ml-1"
            exact
            min-width="128"
            text
            color
          >
            <span>{{ link }}</span>
          </v-btn>
        </v-toolbar-items>

        <v-app-bar-nav-icon v-else @click="setDrawer(true)" />
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script>
// Utilities
import { mapGetters, mapMutations, mapState } from "vuex";

export default {
  name: "CoreAppBar",

  computed: {
    ...mapGetters("accounts", ["navlinks"]),
  },

  methods: {
    ...mapMutations({
      setDrawer: "setDrawer",
    }),
    gohome() {
      this.$router.push("/home");
    },
  },
  mounted() {
    console.log(this.navlinks);
  },
};
</script>
<style>
.img-move {
  left: -35px;
}
</style>
