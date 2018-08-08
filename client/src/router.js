import Vue from "vue";
import Router from "vue-router";
import App from "./App.vue";
import Campaigns from "./views/Campaigns.vue";
import CampaignDetails from "./views/CampaignDetails.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: App
    },
    {
      path: "/campaigns",
      name: "campaigns",
      component: Campaigns
    },
    {
      path: "/campaigns/:id",
      component: CampaignDetails
    }
  ]
});
