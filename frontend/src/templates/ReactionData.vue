<template>
  <div>
    <data-container
      :data-function="dataFunction"
      :data-components="dataComponents"
      :colWidth="[6, 6, 12]"
    />
  </div>
</template>

<script>
import HorizontalBarChart from "../components/HorizontalBarChart.vue";
import { GET } from "../data/api";
import DataContainer from "../components/DataContainer.vue";
export default {
  name: "ReactionData",
  components: {
    DataContainer,
  },

  data() {
    return {
      dataComponents: [
        HorizontalBarChart,
        HorizontalBarChart,
        HorizontalBarChart,
      ],
      dataFunction: GET.reactionData,
    };
  },

  mounted() {},

  methods: {},
};
</script>
