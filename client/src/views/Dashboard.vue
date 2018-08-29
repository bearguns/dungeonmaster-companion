<template>
  <section>
    <div class="chip-container">
      <div class="row">
        <chip title="Campaigns" linkto="/campaigns" />
      </div>
    </div>
  </section>
</template>

<script>
import Chip from "../components/Chip.vue";
export default {
  name: "Dashboard",
  components: {
    Chip
  }
};
</script>
