<template>
  <div>
    <h1 class="text-center lorge">Skilaboð eftir tíma</h1>
    <data-container
      :data-function="dataFunction"
      :data-components="dataComponents"
      :colWidth="12"
    />
  </div>
</template>

<script>
import LineChart from "../components/LineChart.vue";
import { GET } from "../data/api";
import DataContainer from "../components/DataContainer.vue";
export default {
  name: "DataOverTime",
  components: {
    DataContainer,
  },

  data() {
    return {
      dataComponents: [LineChart, LineChart, LineChart],
      dataFunction: GET.messagesByTimeData,
    };
  },
};
</script>
