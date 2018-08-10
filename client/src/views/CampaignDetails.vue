<template>
  <div>
    <h2>{{campaignName}}</h2>
    <SessionList :sessions="sessionList" />
  </div>
</template>

<script>
import gql from "graphql-tag";
import SessionList from "./SessionList.vue";

export default {
  name: "CampaignDetails",
  components: {
    SessionList
  },
  apollo: {
    campaign: gql`
       query {
         campaign(id: ${2}) {
           name
           sessions {
             id
             sessionName
             startDate
             sessionNotes
           }
         }
       }

     `
  },
  computed: {
    campaignName() {
      return (this.campaign && this.campaign.name) || "";
    },
    sessionList() {
      if (!this.campaign) {
        return [];
      }
      return this.campaign.sessions;
    }
  }
};
</script>
