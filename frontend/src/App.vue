<template>
  <div id="app">
    <most-popular-data />
    <data-over-time />
  </div>
</template>

<script>
import { GET } from "./data/api";
import DataOverTime from "./templates/DataOverTime.vue";
import MostPopularData from "./templates/MostPopularData.vue";
export default {
  name: "App",
  components: {
    MostPopularData,
    DataOverTime,
  },

  data() {
    return {};
  },

  methods: {
    async getAllData() {
      const data = await GET.allData();
      this.$store.years = data.years;
      this.$store.names = data.names;
    },
  },
};
</script>

<style lang="scss">
@import "~@/assets/scss/vendors/bootstrap-vue/index";
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
