<template>
  <b-container class="data">
    <b-row>
      <b-col col lg="6">
        <!-- <horizontal-bar-chart :labels="labels" :lines="lines" /> -->
      </b-col>
      <b-col col lg="6">
        <!-- <horizontal-bar-chart :labels="labels" :lines="lines" /> -->
      </b-col>
    </b-row>
    <b-row class="justify-content-md-center">
      <b-col col lg="6">
        <!-- <horizontal-bar-chart :labels="labels" :lines="lines" /> -->
      </b-col>
      <b-col col lg="6">
        <!-- <horizontal-bar-chart :labels="labels" :lines="lines" /> -->
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
// import HorizontalBarChart from "../components/HorizontalBarChart.vue";
import { GET } from "../data/api";
import { getChartData } from "../utils/helpers";
export default {
  name: "MostPopularData",
  components: {
    // HorizontalBarChart,
  },

  async mounted() {
    await this.getMostPopularData();
    this.setPlots();
  },
  data() {
    return {
      keys: {},
    };
  },

  methods: {
    async getMostPopularData() {
      await GET.mostPopularData(this.$store.year).then(
        function (data) {
          this.$store.mostPopularData = data;
          // Store label and data key values
          this.$store.mostPopularData.forEach((obj) => {
            const category = Object.keys(obj)[0];
            this.keys[category] = Object.keys(obj[category][0]);
          });
        }.bind(this)
      );
    },

    getPlots(key) {
      return getChartData(
        this.$store.mostPopularData.find((obj) => obj[key])[key],
        key,
        this.keys[key][1],
        this.keys[key][0]
      );
    },

    getLabelsForKey(key) {
      const dataObj = this.getPlots(key);
      return dataObj.labels.slice(0, 5);
    },

    getLinesForKey(key) {
      const dataObj = this.getPlots(key);
      return dataObj.lines.slice(0, 5);
    },
  },
};
</script>

<style lang="scss">
.data {
  width: 100%;
}
</style>
