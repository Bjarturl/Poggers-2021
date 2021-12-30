<template>
  <mdb-container>
    <mdb-horizontal-bar-chart
      :data="horizontalBarChartData"
      :options="horizontalBarChartOptions"
    ></mdb-horizontal-bar-chart>
  </mdb-container>
</template>

<script>
import { mdbHorizontalBarChart, mdbContainer } from "mdbvue";
export default {
  name: "HorizontalBarChart",
  components: {
    mdbHorizontalBarChart,
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
      default: () => {},
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
    horizontalBarChartData() {
      return {
        labels: this.labels,
        datasets: this.lines.map((dataset) => ({
          backgroundColor: [
            "#00ffff",
            "#ff00ff",
            "#ffff00",
            "#00ff00",
            "#0000ff",
            "#00ffff",
            "#ff00ff",
            "#ffff00",
            "#00ff00",
            "#0000ff",
            "#00ffff",
            "#ff00ff",
            "#ffff00",
            "#00ff00",
            "#0000ff",
            "#00ffff",
            "#ff00ff",
            "#ffff00",
            "#00ff00",
            "#0000ff",
          ],
          ...dataset,
        })),
      };
    },

    horizontalBarChartOptions() {
      return {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          labels: {
            fontColor: "#fff",
            fontSize: 18,
            boxWidth: 0,
          },
        },
        scales: {
          xAxes: [
            {
              barPercentage: 1,

              ticks: {
                fontColor: "#FFFFFF",
              },
            },
          ],
          yAxes: [
            {
              gridLines: {
                display: true,
              },
              ticks: {
                fontColor: "#FFFFFF",
              },
            },
          ],
        },
      };
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
