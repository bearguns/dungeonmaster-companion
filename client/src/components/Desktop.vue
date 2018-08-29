<template>
<section class="desktop">
  <slot></slot>
</section>
</template>

<script>
export default {
  name: "Desktop"
};
</script>

<style>
.desktop {
  width: 100%;
  height: 99%;
  padding: 18px;
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
  align-items: flex-start;
}
</style>
