<template>
  <div class="campaigns-container">
    <CampaignChip v-for="campaign in campaigns" :key="campaign.id" :campaign="campaign" />
  </div>
</template>

<script>
import gql from "graphql-tag";
import CampaignChip from "./CampaignChip.vue";

export default {
  name: "CampaignList",
  components: {
    CampaignChip
  },
  apollo: {
    campaigns: gql`
      {
        campaigns {
          id
          name
          players {
            id
            charName
            charClass
            charRace
            charLevel
          }
          sessions {
            id
            sessionName
          }
        }
      }
    `
  }
};
</script>

<style>
.campaigns-container {
  display: flex;
  padding: 48px;
}
</style>
