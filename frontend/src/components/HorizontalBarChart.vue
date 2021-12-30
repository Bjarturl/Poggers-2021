<template>
  <mdb-container>
    <mdb-horizontal-bar-chart
      :data="horizontalBarChartData"
      :options="horizontalBarChartOptions"
      :height="600"
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
            "#2F4155",
            "#2D496D",
            "#29589E",
            "#2176FF",
            "#2A8CFE",
            "#33A1FD",
            "#98B69F",
            "#FDCA40",
            "#F79824",
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
          ].sort(() => 0.5 - Math.random()),
          borderColor: [],
          borderWidth: 1,
          ...dataset,
        })),
      };
    },

    horizontalBarChartOptions() {
      return {
        horizontalBarChartOptions: {
          responsive: false,
          maintainAspectRatio: false,
          scales: {
            xAxes: [
              {
                barPercentage: 1,
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)",
                },
              },
            ],
            yAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)",
                },
              },
            ],
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
