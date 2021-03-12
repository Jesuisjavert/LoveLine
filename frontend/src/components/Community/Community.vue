<template>
  <!-- <div class="main">
        <div class="main-page col-10">
            <h1>커뮤니티 페이지</h1>
            <router-view />
        </div>
    </div> -->
  <v-app>
    <Appbar />
    <Drawer />
    <v-row no-gutters>
      <v-col>
        <!-- <v-container>
                    <router-view />
                </v-container> -->
        <div class="community">
          <router-view />
        </div>
      </v-col>
    </v-row>
  </v-app>
</template>

<script>
import Drawer from "../Community/Drawer";
import Appbar from "../Core/Appbar";

export default {
  components: {
    Appbar,
    Drawer,
  },
};
</script>


<style scoped>
header {
  left: 0px !important;
}
nav {
  top: 96px !important;
}
</style>