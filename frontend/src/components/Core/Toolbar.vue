<template>
  <v-app-bar
    id="app-toolbar"
    app
    flat
    color="white lighten-3"
    style="left: 0px"
  >
    <v-btn v-if="responsive" dark icon @click.stop="onClickDrawer">
      <v-icon>mdi-view-list</v-icon>
    </v-btn>
    <span>LogoImg</span>
    <v-spacer />
    <v-btn>
      <a href="#">Course</a>
    </v-btn>
    <v-btn>
      <a href="#">Community</a>
    </v-btn>
    <v-btn>
      <a href="#">Login</a>
    </v-btn>
  </v-app-bar>
</template>

<script>
import { mapMutations, mapState } from "vuex";

export default {
  data: () => ({
    responsive: false,
  }),
  computed: {
    ...mapState("app", ["drawer"]),
  },
  mounted() {
    this.onResponsiveInverted();
    window.addEventListener("resize", this.onResponsiveInverted);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.onResponsiveInverted);
  },

  methods: {
    ...mapMutations("app", ["setDrawer"]),
    onClickDrawer() {
      this.setDrawer(!this.drawer);
    },
    onResponsiveInverted() {
      if (window.innerWidth < 900) {
        this.responsive = true;
      } else {
        this.responsive = false;
      }
    },
  },
};
</script>
<style></style>
