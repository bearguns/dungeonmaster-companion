<template>
  <div class="session-list-container">
    <ul class="session-list">
      <li class="session-list-item" v-for="session in sessions" :key="session.id">
        <router-link :to="`/sessions/${session.id}`">{{session.sessionName}} - {{session.startDate}}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "SessionList",
  props: {
    sessions: {
      type: Array,
      required: true
    }
  }
};
</script>
