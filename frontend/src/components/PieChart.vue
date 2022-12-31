<template>
  <mdb-container>
    <mdb-pie-chart :data="pieChartData" :options="pieChartOptions" :width="width" :height="height"></mdb-pie-chart>
  </mdb-container>
</template>

<script>
import { mdbPieChart, mdbContainer } from "mdbvue";
import { getTrueLabel } from "../utils/helpers";

export default {
  name: "PieChart",
  components: {
    mdbPieChart,
    mdbContainer,
  },

  props: {
    labels: {
      type: Array,
      required: true,
    },
    lines: {
      type: Array,
      required: true,
    },
    options: {
      type: Object,
      default: () => { },
      required: false,
    },
    width: {
      type: Number,
      default: 600,
    },
    height: {
      type: Number,
      default: 300,
    },
  },

  data() {
    return {};
  },

  computed: {
    pieChartData() {
      return {
        labels: this.labels,
        datasets: this.lines.map((dataset) => ({
          backgroundColor: [
            "#F7464A",
            "#46BFBD",
            "#FDB45C",
            "#949FB1",
            "#4D5360",
          ],
          hoverBackgroundColor: [
            "#FF5A5E",
            "#5AD3D1",
            "#FFC870",
            "#A8B3C5",
            "#616774",
          ],
          ...dataset,
          label: getTrueLabel(dataset.label)
        })),
      };
    },

    pieChartOptions() {
      return {
        responsive: false,
        maintainAspectRatio: false,
        plugins: {
          datalabels: {
            color: "white",
            align: "center",
            font: {
              size: 16,
            },
            formatter: (value) => {
              const [dataset] = this.pieChartData.datasets;
              const setValue = dataset.data.reduce((a, b) => a + b);

              return `${Math.round((value / setValue) * 100)}%`;
            },
          },
        },
        ...this.options,
      };
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
