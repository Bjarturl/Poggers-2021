const store = {
  year: "2021",
  years: ["2016", "2017", "2018", "2019", "2020", "2021", "Frá byrjun"],
  currPage: 0,
};

export default {
  store,
  // we can add objects to the Vue prototype in the install() hook:
  install(Vue) {
    Vue.prototype.$store = store;
  },
};
