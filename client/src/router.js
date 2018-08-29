import Vue from "vue";
import Router from "vue-router";
import App from "./App.vue";
import Campaigns from "./views/Campaigns.vue";
import CampaignDetails from "./views/CampaignDetails.vue";
import CampaignList from "./views/CampaignList.vue";
import SessionDetails from "./views/Session/SessionDetails.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: SessionDetails
    }
  ]
});
