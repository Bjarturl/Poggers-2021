<template>
  <mdb-container>
    <mdb-line-chart
      :data="lineChartData"
      :options="lineChartOptions"
      :width="600"
      :height="300"
    ></mdb-line-chart>
  </mdb-container>
</template>

<script>
  import { mdbLineChart, mdbContainer } from "mdbvue";
  export default {
    name: "HelloWorld",
    components: {
      mdbLineChart,
      mdbContainer
    },

    props: {
      labels: {
        type: Array,
        required: true
      },
      lines: {
        type: Array,
        required: true
      },
      options: {
        type: Object,
        default: () => {},
        required: false
      },
    },

    data() {
      return {
      };
    },

    computed: {
      lineChartData() {
        return {
          labels: this.labels,
          datasets: this.lines.map(dataset => ({
              backgroundColor: "transparent",
              borderColor: "rgba(255, 99, 132, 1)",
              ...dataset
          }))
        }
      },

      lineChartOptions() {
        return {
          responsive: false,
          maintainAspectRatio: false,
          scales: {
            xAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                }
              }
            ],
            yAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                }
              }
            ]
          },
          ...this.options
        }
      }
    },
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
