import Vue from "vue";
import Vuex from "vuex";
import uiWindows from "./store/ui-windows";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    activeEncounter: {},
    players: []
  },
  mutations: {
    setActiveEncounter(state, encounter) {
      state.activeEncounter = Object.assign({}, encounter);
    },
    setPlayers(state, players) {
      state.players = [...players];
    }
  },
  actions: {},
  modules: { uiWindows }
});
