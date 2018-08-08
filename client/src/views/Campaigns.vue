<template>
  <div>
    <h1>Campaigns</h1>
    <div class="campaigns-container">
      <CampaignCard v-for="campaign in campaigns" :key="campaign.id" :campaign="campaign" />
    </div>
  </div>
</template>

<script>
import gql from "graphql-tag";
import CampaignCard from "./CampaignCard.vue";

export default {
  name: "CampaignsView",
  components: {
    CampaignCard
  },
  apollo: {
    campaigns: gql`
      {
        campaigns {
          id
          name
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
