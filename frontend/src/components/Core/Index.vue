<template>
  <v-app>
    <core-app-bar />

    <!-- <core-drawer /> -->

    <core-view />
  </v-app>
</template>

<script>
  export default {
    name: 'Home',

    components: {
      CoreAppBar: () => import('./Appbar'),
      // CoreDrawer: () => import('./Drawer'),
      CoreView: () => import('@/App'),
    },
  }
</script>
