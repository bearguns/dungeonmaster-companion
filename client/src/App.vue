<template>
  <div id="app">
    <div id="nav">
      <router-link to="/campaigns">Campaigns</router-link>
      <router-link to="/sessions">Session Manager</router-link>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
import "./app.css";
import "bootstrap/dist/css/bootstrap.min.css";
export default {};
</script>

<style>
#app {
  padding: 55px;
}
#nav {
  padding: 30px;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

a {
  text-decoration: none;
}
</style>
