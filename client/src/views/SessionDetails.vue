<template>
  <div>
    <h3>{{session.sessionName}}</h3>
    <p class="session.subtitle">{{session.startDate | friendlyDate}}</p>

    <section class="session-notes">
      <article v-html="mdNotes"></article>
    </section>
  </div>
</template>

<script>
import moment from "moment";
import { markdown } from "markdown";

export default {
  name: "SessionDetails",
  computed: {
    session() {
      return this.$route.params.session;
    },
    mdNotes() {
      return markdown.toHTML(this.session.sessionNotes);
    }
  },
  filters: {
    friendlyDate(date) {
      return moment(date).format("MM/DD/YYYY hh:mma");
    }
  }
};
</script>

<style>
</style>
