import Vue from "vue";
import { ApolloClient } from "apollo-client";
import { HttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";
import VueApollo from "vue-apollo";

import App from "./App.vue";
import store from "./store";
import router from "./router";

const httpLink = new HttpLink({
  uri: "http://localhost:8000/graphql/"
});

const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
  connectToDevTools: true
});

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
});

Vue.config.productionTip = false;
Vue.use(VueApollo);

new Vue({
  store,
  router,
  provide: apolloProvider.provide(),
  render: h => h(App)
}).$mount("#app");
