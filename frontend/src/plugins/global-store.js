const store = {
  year: "2022",
  years: ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "frabyrjun"],
  currPage: 0,
};

export default {
  store,
  // we can add objects to the Vue prototype in the install() hook:
  install(Vue) {
    Vue.prototype.$store = store;
  },
};
