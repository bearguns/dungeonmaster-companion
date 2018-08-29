<template>
<div id="app">
  <menu-bar></menu-bar>
  <router-view></router-view>
  <dice-tray />
</div>
</template>

<script>
import "./assets/css/app.css";
import MenuBar from "./components/MenuBar.vue";
import DiceTray from "./components/DiceTray.vue";

export default {
  name: "App",
  components: {
    MenuBar,
    DiceTray
  },
  computed: {
    activeLink() {
      return this.$route.path;
    }
  }
};
</script>
<style>
#app {
  width: 100%;
  height: 95vh;
  margin: 0 auto;
}
</style>
