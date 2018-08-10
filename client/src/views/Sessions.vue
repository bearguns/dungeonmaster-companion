<template>
  <div>
    <h1>{{campaignName}} Sessions</h1>
    <div class="sessions-container">
      <SessionChip v-for="session in sessions" :key="session.id" :session="session" />
    </div>
  </div>
</template>

<script>
import SessionChip from "./SessionChip.vue";
export default {
  name: "Sessions View",
  props: {
    sessions: {
      type: Array,
      required: true
    }
  },
  components: {
    SessionChip
  }
};
</script>
