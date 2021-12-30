<template>
  <div>
    <h1 class="text-center">Hver var virkastur?</h1>
    <data-container
      :data-function="dataFunction"
      :data-components="dataComponents"
    />
  </div>
</template>

<script>
import HorizontalBarChart from "../components/HorizontalBarChart.vue";
import { GET } from "../data/api";
import DataContainer from "../components/DataContainer.vue";
export default {
  name: "MostPopularData",
  components: {
    DataContainer,
  },

  data() {
    return {
      dataComponents: [
        HorizontalBarChart,
        HorizontalBarChart,
        HorizontalBarChart,
        HorizontalBarChart,
      ],
      dataFunction: GET.mostPopularData,
    };
  },

  methods: {},
};
</script>
