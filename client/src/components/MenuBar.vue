<template>
<div id="menubar">
  <div class="menubar-menu">
    <font-awesome-icon class="menubar-menu-icon" icon="skull"/>
    <h3 class="title">{{ activeCampaign.name }}</h3>
  </div>
  <div class="menubar-title">Dungeon Master's Assistant</div>
</div>
</template>

<script>
import gql from "graphql-tag";
export default {
  name: "MenuBar",
  apollo: {
    campaigns
  }
};
</script>

<style>
#menubar {
  width: 100%;
  height: 34px;
  padding: 8px 14px 8px 14px;
  background-color: var(--white);
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
}

.menubar-menu {
}

.menubar-menu-icon path {
  color: var(--black);
}
.menubar-title {
  margin-left: auto;
  color: var(--black);
  font-family: "VT323", monospace;
  font-size: 1.5rem;
}
</style>
