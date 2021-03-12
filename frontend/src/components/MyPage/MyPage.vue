<template>
    <v-app>
        <Appbar />
        <Drawer />
        <v-row no-gutters>
            <v-col>
                <!-- <v-container>
                    <router-view />
                </v-container> -->
                <div class="mypage">
                    <router-view />
                </div>
            </v-col>
        </v-row>
    </v-app>
</template>

<script>
import Appbar from '../Core/Appbar.vue';
import Drawer from '../MyPage/MyPageDrawer.vue';

export default {
    components: {
        Appbar,
        Drawer,
    }
}
</script>

<style scoped>
header {
  left: 0px !important;
}
nav {
  top: 96px !important;
}
</style>