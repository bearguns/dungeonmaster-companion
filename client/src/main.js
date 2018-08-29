import Vue from "vue";
import { ApolloClient } from "apollo-client";
import { HttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";
import VueApollo from "vue-apollo";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faSkull,
  faUserShield,
  faPlus,
  faMinus,
  faTimesCircle
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import App from "./App.vue";
import store from "./store";
import router from "./router";

library.add(faSkull);
library.add(faUserShield);
library.add(faPlus);
library.add(faMinus);
library.add(faTimesCircle);

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

Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.config.productionTip = false;
Vue.use(VueApollo);

new Vue({
  store,
  router,
  provide: apolloProvider.provide(),
  render: h => h(App)
}).$mount("#app");
