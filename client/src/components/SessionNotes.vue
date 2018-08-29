<template>
<div class="session-notes">
  <div class="markdown">
    <p v-if="!edit">{{notes}}</p>
    <textarea cols="40" id="" name="" rows="18" v-if="edit">{{notes}}</textarea>
  </div>
</div>
</template>

<script>
import { markdown } from "markdown";
export default {
  name: "SessionNotes",
  props: ["notes"],
  computed: {
    mdNotes() {
      return markdown.toHTML(this.notes);
    },
    edit() {
      return true;
    }
  }
};
</script>

<style>
.session-notes {
  overflow-y: scroll;
}
.markdown * {
  color: var(--black);
}
</style>
