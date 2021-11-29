<template>
  <div>
    <line-chart :labels="labels" :lines="lines" />
  </div>
</template>

<script>
import LineChart from "../components/LineChart.vue";
import { GET } from "../data/api";
import { formatArrByKey, capitalizeFirstLetter } from "../utils/helpers";
export default {
  name: "DataOverTime",
  components: {
    LineChart,
  },

  async mounted() {
    await this.getMessagesByTime();
    const key = "fjöldi_skilaboða_eftir_degi";
    const dataObj = this.getChartData(
      key,
      this.keys[key][1],
      this.keys[key][0]
    );
    this.labels = dataObj.labels;
    this.lines = [dataObj.lines];
  },
  data() {
    return {
      labels: [],
      lines: [],
      keys: {},
    };
  },

  methods: {
    async getMessagesByTime() {
      if (!this.$store.dataOverTime) {
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
      }
    },

    getByTimeOfDayData() {
      const key = "fjöldi_skilaboða_eftir_tíma_dags";
      const baseObj = this.$store.dataOverTime.find((obj) => obj[key])[key];
      return {
        labels: formatArrByKey(baseObj, "Klukkutími"),
        lines: [
          {
            data: formatArrByKey(baseObj, "Skilaboð"),
            label: "Fjöldi skilaboða eftir tíma dags",
          },
        ],
      };
    },

    getByDayData() {
      const key = "fjöldi_skilaboða_eftir_degi";
      const baseObj = this.$store.dataOverTime.find((obj) => obj[key])[key];
      return {
        labels: formatArrByKey(baseObj, "Day"),
        lines: [
          {
            data: formatArrByKey(baseObj, "Skilaboð"),
            label: "Fjöldi skilaboða eftir degi",
          },
        ],
      };
    },

    getChartData(key, x, y) {
      const baseObj = this.$store.dataOverTime.find((obj) => obj[key])[key];
      return {
        labels: formatArrByKey(baseObj, x),
        lines: {
          data: formatArrByKey(baseObj, y),
          label: capitalizeFirstLetter(key),
        },
      };
    },
  },
};
</script>

<style lang="scss">
@import "~@/assets/scss/vendors/bootstrap-vue/index";
</style>
