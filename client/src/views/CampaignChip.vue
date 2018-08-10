<template>
  <router-link :to="`/campaigns/${campaign.id}`">
    <div class="chip">
      <p class="chip-title">{{ campaign.name }}</p>
      <p class="chip-subtitle">{{ campaign.players.length }} Players</p>
      <p class="chip-subtitle">{{ campaign.sessions.length }} Sessions</p>
    </div>
  </router-link>
</template>

<script>
export default {
  props: {
    campaign: {
      type: Object,
      required: true
    }
  }
};
</script>

<style>
a {
  text-decoration: none;
}
</style>
