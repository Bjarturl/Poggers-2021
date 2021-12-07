<template>
  <b-container class="data">
    <b-row v-if="!fetching && data">
      <b-col
        class="data__item"
        col
        :lg="colWidth"
        v-for="(key, idx) in Object.keys(keys)"
        v-bind:key="key"
      >
        <component
          v-if="idx < dataComponents.length"
          :is="dataComponents[idx]"
          :labels="getLabelsForKey(key)"
          :lines="getLinesForKey(key)"
        />
      </b-col>
    </b-row>
    <b-row v-else>
      <Loading />
    </b-row>
  </b-container>
</template>

<script>
import { getChartData } from "../utils/helpers";
import Loading from "./Loading.vue";

export default {
  name: "DataContainer",

  components: {
    Loading,
  },

  props: {
    dataFunction: {
      type: Function,
      required: true,
    },
    dataComponents: {
      type: Array,
      required: true,
    },
    colWidth: {
      type: Number,
      default: 6,
    },
  },

  async mounted() {
    await this.getData();
  },

  data() {
    return {
      keys: {},
      fetching: false,
      data: null,
    };
  },

  methods: {
    async getData() {
      this.fetching = true;
      await this.dataFunction(this.$store.year).then(
        function (data) {
          this.data = data;
          // Store label and data key values
          this.data.forEach((obj) => {
            const category = Object.keys(obj)[0];
            this.keys[category] = Object.keys(obj[category][0]);
          });
        }.bind(this)
      );
      this.fetching = false;
    },

    getPlots(key) {
      return getChartData(
        this.data.find((obj) => obj[key])[key],
        key,
        this.keys[key][1],
        this.keys[key][0]
      );
    },

    getLabelsForKey(key) {
      const dataObj = this.getPlots(key);
      return dataObj.labels;
    },

    getLinesForKey(key) {
      const dataObj = this.getPlots(key);
      return [dataObj.lines];
    },
  },
};
</script>

<style lang="scss">
.data {
  width: 100%;
  overflow: hidden;
  text-align: center;
  &__item {
    border: 3px solid black;
    padding: 20px;
  }
}
</style>
