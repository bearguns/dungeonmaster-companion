<template>
<div class="window">
  <div class="window-title-bar">
    <h3 class="title is-3">{{ title }}</h3>
    <font-awesome-icon
      class="window-title-bar-close"
      :style="{'font-size': '1rem', 'margin-left': 'auto', 'color': 'var(--red)'}"
      icon="times-circle"
      @click="closeSelf">
    </font-awesome-icon>
  </div>
  <div class="window-body">
    <slot></slot>
  </div>
</div>
</template>

<script>
export default {
  name: "AppWindow",
  props: ["title"],
  methods: {
    closeSelf() {
      console.log(`closing window ${this.title}`);
      this.$store.commit("closeWindow", this.title);
    }
  }
};
</script>

<style>
.window {
  display: flex;
  flex-direction: column;
  background-color: white;
  border-radius: 4px;
  box-shadow: 6px 6px 20px 0px black;
  width: 33%;
  min-width: 320px;
  max-width: 600px;
  margin-bottom: 14px;
  min-height: 240px;
  max-height: 440px;
}

.window-title-bar {
  position: relative;
  top: 0;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  border-top-right-radius: 4px;
  border-top-left-radius: 4px;
  height: 26px;
  min-height: 26px;
  line-height: 26px;
  font-size: 1.35rem;
  font-family: "VT323", monospace;
  color: var(--white);
  padding-left: 7px;
  padding-right: 7px;
  background-color: var(--gray);
}

.window-title-bar .title {
  color: var(--black);
}

.window.active .window-title-bar {
  background-color: var(--pink);
}

.window-title-bar-close path {
  color: var(--red);
}
.window-body {
  padding: 2px 8px 2px 8px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  overflow-y: scroll;
  background-color: white;
}

.window-body * {
  color: var(--black);
}
</style>
