<template>
  <div class="session-list-container">
    <SessionChip v-for="session in sessions" :key="session.id" :session="session" />
  </div>
</template>

<script>
import SessionChip from "./SessionChip.vue";
export default {
  name: "SessionList",
  components: {
    SessionChip
  },
  props: {
    sessions: {
      type: Array,
      required: true
    }
  }
};
</script>
