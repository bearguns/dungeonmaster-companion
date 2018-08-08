<template>
  <div>
    <h2>{{ campaign.name }}</h2>
    <SessionList :sessions="campaign.sessions" />
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
           }
         }
       }

     `
  }
};
</script>
