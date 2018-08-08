<template>
  <router-link :to="`/campaigns/${campaign.id}`">
    <div class="card">
      <p class="card-title">{{ campaign.name }}</p>
      <p class="card-subtitle">{{ campaign.sessions.length }} Sessions</p>
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
.card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 140px;
  height: 180px;
  background-color: #ffffff;
  border-radius: 8px;
  border: 1px solid wheat;
}

.card-title {
  font-size: 18px;
  font-weight: 300;
}

a {
  text-decoration: none;
}
</style>
