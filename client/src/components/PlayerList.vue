<template>
  <div class="player-list">
    <a class="player-list-item" v-for="player in players" :key="player.id" :href="player.charSheet" target="_blank">
      <p class="title">{{player.charName}}</p>
      <ul class="player-details">
        <li>{{player.charRace}}</li>
        <li>{{player.charClass}}</li>
        <li>{{player.charLevel}}</li>
      </ul>
    </a>
</div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "PlayerList",
  computed: {
    ...mapState({
      players: state => state.players
    })
  }
};
</script>

<style>
.player-list {
  text-transform: uppercase;
  list-style: none;
  color: var(--black);
  display: flex;
  flex-direction: column;
}

.player-list .title {
  color: var(--black);
  font-size: 1.2rem;
}

.player-list-item {
  margin-bottom: 8px;
}
.player-list p {
  margin: 2px;
}

.player-details {
  display: flex;
  justify-content: flex-start;
  margin: 2px;
  padding-left: 0px;
}

.player-details li {
  list-style: none;
  color: var(--black);
  margin-right: 2px;
  font-size: 0.75rem;
}
</style>
