<template>
<app-desktop v-if="session">
  <app-window v-for="uiWindow in uiWindows" :key="uiWindow.title" :title="uiWindow.title" v-if="uiWindow.open">
    <component :is="uiWindow.component" v-bind="uiWindow.data"/>
  </app-window>
</app-desktop>
</template>

<script>
import moment from "moment";
import { markdown } from "markdown";
import gql from "graphql-tag";
import { mapState } from "vuex";

import AppDesktop from "../../components/Desktop.vue";
import AppWindow from "../../components/Window.vue";
import ActiveEncounter from "../../components/ActiveEncounter.vue";
import EncounterList from "../../components/EncounterList.vue";
import PlayerList from "../../components/PlayerList.vue";
import SessionNotes from "../../components/SessionNotes.vue";

export default {
  name: "SessionDetails",
  components: {
    AppDesktop,
    AppWindow
  },
  computed: {
    ...mapState({
      uiWindows: state => state.uiWindows
    })
  },
  apollo: {
    session: gql`
      {
        session(id: 2) {
          name
          startDate
          notes
          campaign {
            name
            players {
              id
              charName
              charClass
              charRace
              charLevel
              charSheet
            }
          }
          encounters {
            name
            encounterType
            completed
            skipped
            trigger
            description
            monsters {
              id
              name
              hitPoints
              url
            }
          }
        }
      }
    `
  },
  updated() {
    this.$store.commit("setPlayers", this.session.campaign.players);
  },
  filters: {
    friendlyDate(date) {
      return moment(date).format("MM/DD/YYYY hh:mma");
    }
  }
};
</script>

<style>
#session-details-view {
  width: 100%;
}
</style>
