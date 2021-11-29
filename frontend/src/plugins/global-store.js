const store = {
  year: "all",
  dataOverTime: null,
};

export default {
  store,
  // we can add objects to the Vue prototype in the install() hook:
  install(Vue) {
    Vue.prototype.$store = store;
  },
};
