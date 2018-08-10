<template>
  <router-link :to="{ name: 'session-details', params: { session } }" >
    <div class="chip">
      <p class="chip-title">{{ session.sessionName }}</p>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "SessionChip",
  props: {
    session: {
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
