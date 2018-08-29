<template>
  <div class="monster-list">
    <div class="monster-list-item" v-for="monster in monsters" :key="monster.id">
      <a :href="monster.url" target="_blank" class="title is-3">{{monster.name}}</a>
      <monster-hp :monster="monster"></monster-hp>
    </div>
  </div>
</template>

<script>
import _ from "lodash";
import MonsterHp from "./MonsterHP.vue";
export default {
  name: "MonsterList",
  props: ["monsters"],
  components: {
    MonsterHp
  }
};
</script>
