<template>
<div class="active-encounter" v-if="encounterLoaded">
  <h2 class="title centered">{{encounter.name}}</h2>
  <p>{{encounter.description}}</p>
  <div v-if="isCombat">
    <ul class="initiative-list">
      <p class="title is-3 centered">Initiative</p>
      <li v-for="creature in sortedInitiative" :key="creature.roll">
        <span>{{creature.name}}</span>
        <span>{{creature.roll}}</span>
      </li>
    </ul>
    <form action="" @submit.prevent="addInitiative">
      <input name="name" type="text" value="" placeholder="Creature"/>
      <input name="roll" type="number" value="1" />
      <button class="save-initiative-button">
        <font-awesome-icon icon="plus"></font-awesome-icon>
      </button>
    </form>
    <monster-list :monsters="encounter.monsters" />
    <hr />
  </div>
</div>
</template>

<script>
import { mapState } from "vuex";
import * as _ from "lodash";
import MonsterList from "./MonsterList.vue";
export default {
  name: "ActiveEncounter",
  components: {
    MonsterList
  },
  data() {
    return {
      initiative: []
    };
  },
  computed: {
    ...mapState({
      encounter: state => state.activeEncounter,
      players: state => state.players
    }),
    sortedInitiative() {
      return _.sortBy(this.initiative, i => -i.roll);
    },
    encounterLoaded() {
      return !_.isEmpty(this.encounter);
    },
    isCombat() {
      return this.encounter.encounterType === "COMBAT";
    }
  },
  methods: {
    addInitiative(e) {
      const name = e.target.name.value;
      const roll = Number(e.target.roll.value);
      if (!name) return null;
      this.initiative = [...this.initiative, { name, roll }];
      e.target.reset();
      e.target.name.focus();
    }
  }
};
</script>

<style>
.active-encounter {
}

ul.initiative-list {
  margin: 0 auto;
  padding: 4px;
}

ul.initiative-list li {
  list-style: none;
  text-transform: uppercase;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 0px 16px 0px 16px;
  border: 1px solid var(--black);
}

ul.initiative-list li:not(:first-of-type) {
  border-top: none;
}
ul.initiative-list li span {
  color: var(--black);
}

form {
  padding: 4px;
  display: flex;
  align-items: center;
}
form input {
  height: 24px;
  border: none;
  font-size: 16px;
  border-radius: 2px;
  color: var(--black);
  margin-left: 4px;
}

form input[type="number"] {
  width: 32px;
}

form button {
  background-color: var(--green);
  margin-left: 4px;
  height: 24px;
  line-height: 24px;
  width: 24px;
  border: none;
  border-radius: 2px;
}

.monster-list {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.monster-hitpoints {
  width: 120px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

button.hp {
  width: 42px;
  height: 34px;
  line-height: 34px;
  border: none;
  border-radius: 2px;
}

button.hp.hp-down {
  background-color: tomato;
}

button.hp.hp-up {
  background-color: var(--green);
}
span.hitpoints {
  color: var(--pink);
  font-size: 1.3rem;
}
</style>
