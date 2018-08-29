<template>
  <router-link :to="linkto">
    <div class="chip">
      <p class="chip-title">
        {{ title }}
      </p>
      <p class="chip-subtitle">
        {{ subtitle }}
      </p>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "Chip",
  props: {
    title: {
      type: String,
      required: true
    },
    subtitle: {
      type: String,
      required: false,
      default: ""
    },
    linkto: {
      type: String,
      required: true
    }
  }
};
</script>
