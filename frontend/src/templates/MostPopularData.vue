<template>
  <b-container class="data">
    <div></div>
    <b-row v-if="!fetching">
      <b-col col lg="6" v-for="key in Object.keys(keys)" v-bind:key="key">
        <horizontal-bar-chart
          :labels="getLabelsForKey(key)"
          :lines="getLinesForKey(key)"
        />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import HorizontalBarChart from "../components/HorizontalBarChart.vue";
import { GET } from "../data/api";
import { getChartData } from "../utils/helpers";
export default {
  name: "MostPopularData",
  components: {
    HorizontalBarChart,
  },

  async mounted() {
    await this.getMostPopularData();
  },
  data() {
    return {
      keys: {},
      fetching: false,
    };
  },

  methods: {
    async getMostPopularData() {
      this.fetching = true;
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
      this.fetching = false;
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
      return [dataObj.lines];
    },
  },
};
</script>

<style lang="scss">
.data {
  width: 100%;
}
</style>
