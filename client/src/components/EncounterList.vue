<template>
<div class="encounter-list">
  <div class="encounter-list-item" v-for="encounter in encounters" :key="encounter.id">
    <div class="title-row">
      <p class="title is-3">{{encounter.name}}</p>
      <div class="checkbox-group">
        <label for="completed">Completed?</label>
        <input name="completed" type="checkbox" :checked="encounter.completed" value=""/>
      </div>
      <div class="checkbox-group">
        <label for="skipped">Skip?</label>
        <input name="skipped" type="checkbox" :checked="encounter.skipped" value=""/>
      </div>
      <button @click.prevent="setActive(encounter)" class="start-encounter">Start</button>
    </div>
    <p class="trigger">{{encounter.trigger}}</p>
  </div>
</div>
</template>

<script>
export default {
  name: "EncounterList",
  props: ["encounters"],
  methods: {
    setActive(encounter) {
      this.$store.commit("setActiveEncounter", encounter);
    }
  }
};
</script>

<style>
label {
  color: var(--black);
  font-size: 0.5rem;
}

.encounter-list {
  text-transform: uppercase;
  list-style: none;
  color: var(--black);
  display: flex;
  flex-direction: column;
}

.encounter-list-item {
  margin-bottom: 8px;
}
.encounter-list p {
  margin: 2px;
}

.encounter-details {
  display: flex;
  justify-content: flex-start;
  margin: 2px;
  padding-left: 0px;
}

.encounter-details li {
  list-style: none;
  color: var(--black);
  margin-right: 2px;
  font-size: 0.75rem;
}

.start-encounter {
  border: none;
  border-radius: 2px;
  background-color: var(--green);
}

.trigger {
  text-transform: none;
  font-size: 0.75rem;
  color: var(--black);
}
</Style>
