<template>
  <b-container>
    <b-row>
      <line-chart :labels="labels" :lines="lines" />
    </b-row>
  </b-container>
</template>

<script>
import LineChart from "../components/LineChart.vue";
import { GET } from "../data/api";
import { getChartData } from "../utils/helpers";
export default {
  name: "DataOverTime",
  components: {
    LineChart,
  },

  async mounted() {
    await this.getMessagesByTime();
    this.setPlots();
  },
  data() {
    return {
      labels: [],
      lines: [],
      currKey: "fjöldi_skilaboða_eftir_degi",
      keys: {},
    };
  },

  methods: {
    async getMessagesByTime() {
      await GET.messagesByTimeData(this.$store.year).then(
        function (data) {
          this.$store.dataOverTime = data;
          // Store label and data key values
          this.$store.dataOverTime.forEach((obj) => {
            const category = Object.keys(obj)[0];
            this.keys[category] = Object.keys(obj[category][0]);
          });
        }.bind(this)
      );
    },

    setPlots() {
      const dataObj = getChartData(
        this.$store.dataOverTime.find((obj) => obj[this.currKey])[this.currKey],
        this.currKey,
        this.keys[this.currKey][1],
        this.keys[this.currKey][0]
      );
      this.labels = dataObj.labels;
      this.lines = [dataObj.lines];
    },
  },
};
</script>

<style lang="scss">
@import "~@/assets/scss/vendors/bootstrap-vue/index";
</style>
