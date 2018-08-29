import ActiveEncounter from "@/components/ActiveEncounter.vue";
import PlayerList from "@/components/PlayerList.vue";

export default {
  state: {
    players: {
      open: true,
      title: "players",
      component: PlayerList
    },
    "active encounter": {
      open: true,
      title: "active encounter",
      component: ActiveEncounter
    }
  },
  mutations: {
    closeWindow(state, windowTitle) {
      state[windowTitle].open = false;
    }
  },
  actions: {}
};
