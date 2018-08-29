<template>
<div id="dice-tray">
  <div class="dice-tray-dice" v-for="dice in dice" :key="dice.roll" @click="rollDice">
    {{ dice.name }}
  </div>
</div>
</template>

<script>
import d20 from "d20";

export default {
  name: "DiceTray",
  data() {
    return {
      dice: [
        { name: "d4", roll: "1d4" },
        { name: "d6", roll: "1d6" },
        { name: "d8", roll: "1d8" },
        { name: "d10", roll: "1d10" },
        { name: "d12", roll: "1d12" },
        { name: "d20", roll: "1d20" }
      ]
    };
  },
  methods: {
    rollDice(dieRoll) {
      console.log(d20.roll(dieRoll));
    }
  }
};
</script>

<style>
#dice-tray {
  width: 600px;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  border: 2px solid var(--green);
}
</style>
