import "@babel/polyfill";
import "mutationobserver-shim";
import Vue from "vue";
import "./plugins/bootstrap-vue";
import App from "./App.vue";
import store from "./plugins/global-store";

Vue.config.productionTip = false;
Vue.use(store);

new Vue({
  render: (h) => h(App),
}).$mount("#app");
