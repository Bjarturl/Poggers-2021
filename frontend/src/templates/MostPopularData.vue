<template>
  <div>
    <horizontal-bar-chart :labels="labels" :lines="lines" />
  </div>
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
    this.setPlots();
  },
  data() {
    return {
      labels: [],
      lines: [],
      currKey: "flest_skilaboð_send",
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

    setPlots() {
      const dataObj = getChartData(
        this.$store.mostPopularData.find((obj) => obj[this.currKey])[
          this.currKey
        ],
        this.currKey,
        this.keys[this.currKey][1],
        this.keys[this.currKey][0]
      );
      this.labels = dataObj.labels.slice(0, 5);
      this.lines = [dataObj.lines].slice(0, 5);
    },
  },
};
</script>

<style lang="scss">
</style>
