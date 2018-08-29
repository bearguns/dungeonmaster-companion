<template>
<div class="monster-hitpoints">
  <button class="hp hp-down" @click="hpDown()"><font-awesome-icon icon="minus"></font-awesome-icon></button>
  <span class="hitpoints">{{ monsterInstance.hitPoints }}</span>
  <button class="hp hp-up" @click="hpUp()"><font-awesome-icon icon="plus"></font-awesome-icon></button>
</div>
</template>

<script>
export default {
  name: "MonsterHP",
  props: ["monster"],
  data() {
    return {
      monsterInstance: Object.assign({}, this.monster)
    };
  },
  methods: {
    hpUp() {
      const hitPoints = this.monsterInstance.hitPoints + 1;
      this.monsterInstance = Object.assign({}, this.monsterInstance, {
        hitPoints
      });
    },
    hpDown() {
      const hitPoints = this.monsterInstance.hitPoints - 1;
      this.monsterInstance = Object.assign({}, this.monsterInstance, {
        hitPoints
      });
    }
  }
};
</script>
